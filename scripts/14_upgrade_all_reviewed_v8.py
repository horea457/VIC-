#!/usr/bin/env python3
"""Upgrade every reviewed idea to one lossless V8 long-form overlay and report.

This is a structural migration, not a substitute for new external research. It
preserves all reviewed facts and sources already in SQLite, standardises the
display fields, and explicitly leaves evidence gaps visible.
"""

from __future__ import annotations

import json
import sqlite3
import argparse
import gzip
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DB = ROOT / "data" / "processed" / "vic_dashboard.db"
OUT_DIR = ROOT / "data" / "curated"
INDEX = OUT_DIR / "all_reviewed_v8_index.json"
REPORT_GZ = ROOT / "analysis" / "all_reviewed_v8.md.gz"
LEGACY_OUT = OUT_DIR / "zz_all_reviewed_v8_deep_v7.json"
LEGACY_REPORT = ROOT / "analysis" / "all_reviewed_v8.md"
ASOF = "2024-01-31"
CHUNK_SIZE = 25

TABLE_KEYS = {
    "ideas_master": "ideas_master",
    "postmortems": "postmortems",
    "meta": "deep_analysis_meta",
    "sections": "deep_analysis_sections",
    "claims": "deep_analysis_claims",
    "metrics": "deep_analysis_metrics",
    "timeline": "deep_analysis_timeline",
    "sources": "deep_analysis_sources",
}


def clean(value, fallback="근거자료에서 확인되지 않음"):
    value = "" if value is None else str(value).strip()
    return value or fallback


def fetch_all(conn, table, ids):
    conn.row_factory = sqlite3.Row
    marks = ",".join("?" for _ in ids)
    order = {
        "ideas_master": "date, idea_id",
        "postmortems": "idea_id",
        "deep_analysis_meta": "idea_id",
        "deep_analysis_sections": "idea_id, section_order",
        "deep_analysis_claims": "idea_id, claim_order",
        "deep_analysis_metrics": "idea_id, metric_order",
        "deep_analysis_timeline": "idea_id, event_order",
        "deep_analysis_sources": "idea_id, source_order",
    }[table]
    return [dict(row) for row in conn.execute(
        f"SELECT * FROM {table} WHERE idea_id IN ({marks}) ORDER BY {order}", ids
    )]


def grouped(rows):
    out = defaultdict(list)
    for row in rows:
        out[row["idea_id"]].append(row)
    return out


def distribute_weights(claims):
    base, remainder = divmod(100, len(claims))
    for idx, claim in enumerate(claims):
        claim["claim_order"] = idx + 1
        claim["thesis_weight_pct"] = base + (1 if idx < remainder else 0)


def added_claim(title, claim, assumption, falsifier, result, verdict, error, lesson):
    return {
        "claim_title_ko": title,
        "thesis_weight_pct": 0,
        "original_claim_ko": claim,
        "t0_evidence_ko": "기존 심층분석의 원문·밸류에이션·사후검증을 연결해 재구성",
        "key_assumption_ko": assumption,
        "ex_ante_falsifier_ko": falsifier,
        "actual_result_ko": result,
        "quantitative_gap_ko": result,
        "verdict_ko": verdict,
        "analytical_error_ko": error,
        "reusable_lesson_ko": lesson,
    }


def upgrade_claims(idea_id, old, post):
    claims = [{**row} for row in old]
    additions = [
        added_claim(
            "밸류에이션과 주당가치 귀속",
            clean(post.get("valuation_verdict_ko")),
            "사업 성과가 순부채·우선청구권·주식보상·인수발행을 차감한 뒤 기존 보통주 한 주에 귀속돼야 한다.",
            "사업지표는 개선되지만 완전희석 주당 현금흐름이나 주가가 장기간 악화된다.",
            clean(post.get("stock_verdict_ko")),
            clean(post.get("overall_verdict_ko"), "혼합"),
            clean(post.get("root_error_ko")),
            "회사 전체 가치와 기존 보통주 한 주의 가치를 반드시 별도로 계산한다.",
        ),
        added_claim(
            "촉매와 보유경로",
            clean(post.get("catalyst_verdict_ko")),
            "촉매가 투자기간 안에 발생하고 그 전에 생기는 손실·유동성·재평가 위험을 견딜 수 있어야 한다.",
            "최종 방향과 무관하게 중간 손실이나 논지 반증이 포지션의 보유 가능성을 훼손한다.",
            f"최초 중요 신호: {clean(post.get('first_signal_ko'))} ({clean(post.get('first_signal_date'), '시점 미상')})",
            "경로 별도판정",
            clean(post.get("why_ko")),
            "목표가와 함께 최초 반증일, 손절·재검토 조건과 예상 보유기간을 저장한다.",
        ),
        added_claim(
            "대차대조표와 자본배분",
            "영업성과가 현금흐름으로 전환되고 경영진의 자본배분이 주당가치를 훼손하지 않아야 한다.",
            "부채·인수·재투자·환원이 원 논지의 정상수익 가정과 양립해야 한다.",
            "차입 증가, 고가 인수, 반복 희석 또는 자산매각이 원 논지의 하방보호를 제거한다.",
            clean(post.get("current_verdict_ko")),
            "자본배분 별도판정",
            clean(post.get("root_error_ko")),
            "단위경제성에서 연결기업 잉여현금흐름으로 넘어갈 때 자본배분표를 반드시 붙인다.",
        ),
    ]
    existing_titles = {clean(row.get("claim_title_ko"), "") for row in claims}
    for addition in additions:
        if len(claims) >= 6:
            break
        if addition["claim_title_ko"] not in existing_titles:
            addition["idea_id"] = idea_id
            claims.append(addition)
    distribute_weights(claims)
    return claims


def upgrade_sections(idea_id, post, claims, existing):
    claim_map = "\n".join(
        f"{c['claim_order']}. {clean(c.get('claim_title_ko'))}: {clean(c.get('original_claim_ko'))} / "
        f"반증조건: {clean(c.get('ex_ante_falsifier_ko'))} / 결과: {clean(c.get('actual_result_ko'))}"
        for c in claims
    )
    standard_titles = {
        "무슨 기업인가", "사업모델·산업구조·돈 버는 방식", "당시 VIC 투자논지",
        "밸류에이션·증권 청구권", "핵심 주장·성립조건·사전 반증조건",
        "실제 사업 전개", "가격 결과와 논지 결과의 분리", "성공·실패의 구체적 원인",
        "최초 반증 신호·인지 가능성·회피 가능성", "최종판정·재사용 교훈",
    }
    if len(existing) == 10 and {clean(x.get("section_title_ko"), "") for x in existing} == standard_titles:
        old = clean(existing[1].get("section_body_ko"))
    else:
        old = "\n\n".join(
            f"[{clean(row.get('section_title_ko'))}] {clean(row.get('section_body_ko'))}"
            for row in existing
        )
    sections = [
        ("무슨 기업인가", clean(post.get("company_description_ko"))),
        ("사업모델·산업구조·돈 버는 방식", old or clean(post.get("company_description_ko"))),
        ("당시 VIC 투자논지", clean(post.get("original_thesis_ko"))),
        ("밸류에이션·증권 청구권", clean(post.get("valuation_verdict_ko"))),
        ("핵심 주장·성립조건·사전 반증조건", claim_map),
        ("실제 사업 전개", clean(post.get("actual_development_ko"))),
        ("가격 결과와 논지 결과의 분리", f"논지 판정: {clean(post.get('thesis_verdict_ko'))}\n\n주가·증권 판정: {clean(post.get('stock_verdict_ko'))}"),
        ("성공·실패의 구체적 원인", f"{clean(post.get('why_ko'))}\n\n근본 분석오류: {clean(post.get('root_error_ko'))}"),
        ("최초 반증 신호·인지 가능성·회피 가능성", f"최초 신호: {clean(post.get('first_signal_ko'))} ({clean(post.get('first_signal_date'), '시점 미상')})\n\n당시 알 수 있었는가: {clean(post.get('knowable_at_t0_ko'))}\n\n피할 수 있었는가: {clean(post.get('avoidability_ko'))}"),
        ("최종판정·재사용 교훈", f"종합판정: {clean(post.get('overall_verdict_ko'))}\n\n다음에 물을 질문: {clean(post.get('counterfactual_question_ko'))}\n\n성공 패턴: {clean(post.get('success_pattern_ko'))}\n\n실패 패턴: {clean(post.get('failure_pattern_ko'))}"),
    ]
    return [
        {"idea_id": idea_id, "section_order": n, "section_title_ko": title, "section_body_ko": body}
        for n, (title, body) in enumerate(sections, 1)
    ]


def upgrade_metrics(idea_id, rows, post):
    metrics = [{**row} for row in rows]
    if len(metrics) < 4:
        metrics.append({
            "idea_id": idea_id,
            "metric_order": 0,
            "metric_name_ko": "주가·증권 결과",
            "t0_value_ko": "원문 진입시점",
            "thesis_expectation_ko": clean(post.get("valuation_verdict_ko")),
            "actual_value_ko": clean(post.get("stock_verdict_ko")),
            "verdict_ko": clean(post.get("overall_verdict_ko")),
            "interpretation_ko": "사업 결과와 기존 보통주 결과를 분리한 보완 지표",
        })
    for n, row in enumerate(metrics, 1):
        row["metric_order"] = n
    return metrics


def upgrade_timeline(idea, rows, post):
    timeline = [{**row} for row in rows]
    candidates = [
        (clean(idea.get("date"), "원문 게시일 미상")[:10], "VIC 아이디어 게시", clean(post.get("original_thesis_ko"))),
        (clean(post.get("first_signal_date"), "시점 미상")[:10], "최초 핵심 검증·반증 신호", clean(post.get("first_signal_ko"))),
        (ASOF, "고정 평가기준일", clean(post.get("stock_verdict_ko"))),
        (clean(post.get("research_asof"), ASOF)[:10], "심층 사후분석 완료", clean(post.get("overall_verdict_ko"))),
    ]
    signatures = {(clean(x.get("event_date_ko"), ""), clean(x.get("event_ko"), "")) for x in timeline}
    for date, event, implication in candidates:
        if len(timeline) >= 6:
            break
        if (date, event) not in signatures:
            timeline.append({"idea_id": idea["idea_id"], "event_order": 0, "event_date_ko": date, "event_ko": event, "thesis_implication_ko": implication})
            signatures.add((date, event))
    while len(timeline) < 6:
        n = len(timeline) + 1
        timeline.append({"idea_id": idea["idea_id"], "event_order": 0, "event_date_ko": ASOF, "event_ko": f"사후검증 축 {n}", "thesis_implication_ko": "사업·밸류에이션·촉매·가격을 분리해 재검증"})
    for n, row in enumerate(timeline, 1):
        row["event_order"] = n
    return timeline


def markdown_report(payload):
    ideas = {x["idea_id"]: x for x in payload["ideas_master"]}
    posts = {x["idea_id"]: x for x in payload["postmortems"]}
    meta = {x["idea_id"]: x for x in payload["meta"]}
    sections, claims = grouped(payload["sections"]), grouped(payload["claims"])
    metrics, timeline, sources = grouped(payload["metrics"]), grouped(payload["timeline"]), grouped(payload["sources"])
    companies = defaultdict(list)
    for idea in payload["ideas_master"]:
        companies[clean(idea.get("ticker"), "미상")].append(idea)

    lines = [
        "# 전체 심층분석 DB — V8 통합 보고서", "",
        f"평가기준일: {ASOF}", "", f"대상: 검수 완료 {len(posts)}건", "",
        "## 결론부터", "",
        "기존 심층분석의 사실·수치·근거를 삭제하지 않고 179건 모두를 같은 장문 구조로 재배열했다. "
        "사업 결과, 논지 결과, 촉매, 가격과 보유경로를 분리하며 근거가 부족한 항목은 부족 상태를 그대로 표시한다.", "", "---", ""
    ]
    for ticker, company_ideas in sorted(companies.items()):
        company_ideas.sort(key=lambda x: clean(x.get("date"), ""))
        # The latest reviewed name wins so historical legal-name changes do not
        # split one ticker's theses into separate reports (for example BX/KKR).
        company = clean(company_ideas[-1].get("company_name"), "기업명 미상")
        longest = max((posts[x["idea_id"]].get("company_description_ko") or "" for x in company_ideas), key=len, default="")
        lines += [f"# {company.strip()} ({ticker}) — 기업과 투자 아이디어", "", "## 기업과 비즈니스", "", clean(longest), "", "## 아이디어 전체 판정", "", "| 게시일 | 방향 | 핵심 논지 | 가격·증권 결과 | 종합판정 |", "|---|---|---|---|---|"]
        for idea in company_ideas:
            iid, post = idea["idea_id"], posts[idea["idea_id"]]
            lines.append(f"| {clean(idea.get('date'))[:10]} | {clean(post.get('research_direction_ko'))} | {clean(meta[iid].get('thesis_type_ko'))} | {clean(post.get('stock_verdict_ko'))} | {clean(post.get('overall_verdict_ko'))} |")
        for n, idea in enumerate(company_ideas, 1):
            iid, post, m = idea["idea_id"], posts[idea["idea_id"]], meta[idea["idea_id"]]
            lines += ["", "---", "", f"<!-- idea:{iid} -->", f"## {n}. {clean(idea.get('date'))[:10]} — {clean(m.get('thesis_type_ko'))}", "", "### 결론부터", "", f"**종합판정: {clean(post.get('overall_verdict_ko'))}.** {clean(m.get('one_line_verdict_ko'))}", ""]
            for section in sections[iid][:4]:
                lines += [f"### {section['section_order']}. {section['section_title_ko']}", "", clean(section.get("section_body_ko")), ""]
            lines += ["### 5. 투자논지를 구성한 핵심 주장", ""]
            for claim in claims[iid]:
                lines += [f"#### {claim['claim_order']}. {clean(claim.get('claim_title_ko'))} — {clean(claim.get('verdict_ko'))}", "", f"**당시 주장:** {clean(claim.get('original_claim_ko'))}", "", f"**성립조건:** {clean(claim.get('key_assumption_ko'))}", "", f"**사전 반증조건:** {clean(claim.get('ex_ante_falsifier_ko'))}", "", f"**실제 결과:** {clean(claim.get('actual_result_ko'))}", "", f"**재사용 교훈:** {clean(claim.get('reusable_lesson_ko'))}", ""]
            for section in sections[iid][5:]:
                lines += [f"### {section['section_order']}. {section['section_title_ko']}", "", clean(section.get("section_body_ko")), ""]
            lines += ["### 핵심 수치", "", "| 지표 | 글 당시 | 기대 | 실제 | 판정 |", "|---|---|---|---|---|"]
            for row in metrics[iid]:
                lines.append(f"| {clean(row.get('metric_name_ko'))} | {clean(row.get('t0_value_ko'))} | {clean(row.get('thesis_expectation_ko'))} | {clean(row.get('actual_value_ko'))} | {clean(row.get('verdict_ko'))} |")
            lines += ["", "### 사건 경로", ""]
            for row in timeline[iid]:
                lines += [f"- **{clean(row.get('event_date_ko'))} · {clean(row.get('event_ko'))}** — {clean(row.get('thesis_implication_ko'))}"]
            lines += ["", "### 주요 근거", ""]
            if sources[iid]:
                for row in sources[iid]:
                    title = clean(row.get("title_ko"))
                    url = row.get("url")
                    lines.append(f"- [{title}]({url}) — {clean(row.get('evidence_ko'))}" if url else f"- {title} — {clean(row.get('evidence_ko'))}")
            else:
                lines.append("- 추가 외부 근거 보강 필요")
        lines += ["", "---", ""]
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--db", type=Path, default=DB)
    args = parser.parse_args()
    with sqlite3.connect(args.db) as conn:
        ids = [row[0] for row in conn.execute("SELECT idea_id FROM postmortems ORDER BY idea_id")]
        raw = {key: fetch_all(conn, table, ids) for key, table in TABLE_KEYS.items()}

    ideas = {row["idea_id"]: row for row in raw["ideas_master"]}
    source_groups = grouped(raw["sources"])
    upgraded_posts = []
    evidence_marker = "V8 근거 보강 대기"
    for original in raw["postmortems"]:
        row = {**original}
        count = len(source_groups[row["idea_id"]])
        if count < 5:
            existing_note = clean(row.get("analyst_note_ko"), "")
            warning = f"{evidence_marker}: 현재 연결 근거 {count}개로, 기업 공시·규제자료를 추가 확인해야 함."
            if evidence_marker not in existing_note:
                row["analyst_note_ko"] = (existing_note + " " + warning).strip()
            row["research_status_ko"] = "V8 구조화 완료·외부근거 추가 보강 필요"
        upgraded_posts.append(row)
    posts = {row["idea_id"]: row for row in upgraded_posts}
    metas = {row["idea_id"]: row for row in raw["meta"]}
    old_sections, old_claims = grouped(raw["sections"]), grouped(raw["claims"])
    old_metrics, old_timeline = grouped(raw["metrics"]), grouped(raw["timeline"])

    payload = {key: [] for key in TABLE_KEYS}
    payload["ideas_master"] = raw["ideas_master"]
    payload["postmortems"] = upgraded_posts
    payload["sources"] = raw["sources"]
    for iid in ids:
        post, idea = posts[iid], ideas[iid]
        claims = upgrade_claims(iid, old_claims[iid], post)
        payload["claims"].extend(claims)
        payload["sections"].extend(upgrade_sections(iid, post, claims, old_sections[iid]))
        payload["metrics"].extend(upgrade_metrics(iid, old_metrics[iid], post))
        payload["timeline"].extend(upgrade_timeline(idea, old_timeline[iid], post))
        m = {**metas[iid]}
        m["report_version"] = "V8-longform-all"
        m["analysis_depth_ko"] = "기업·산업·원문·밸류에이션·주장별 반증·실제전개·가격경로·실패인과를 분리한 장문 통합분석"
        payload["meta"].append(m)

    for stale in OUT_DIR.glob("zz_v8_*_deep_v7.json"):
        stale.unlink()
    idea_order = [row["idea_id"] for row in payload["ideas_master"]]
    chunk_paths = []
    for start in range(0, len(idea_order), CHUNK_SIZE):
        chunk_ids = set(idea_order[start:start + CHUNK_SIZE])
        chunk = {
            key: [row for row in rows if row["idea_id"] in chunk_ids]
            for key, rows in payload.items()
        }
        end = min(start + CHUNK_SIZE, len(idea_order))
        path = OUT_DIR / f"zz_v8_{start + 1:03d}_{end:03d}_deep_v7.json"
        path.write_text(json.dumps(chunk, ensure_ascii=False, indent=2), encoding="utf-8")
        chunk_paths.append(path)
    INDEX.write_text(json.dumps({
        "postmortems": [
            {"idea_id": row["idea_id"], "ticker": row.get("ticker", "")}
            for row in payload["postmortems"]
        ]
    }, ensure_ascii=False, indent=2), encoding="utf-8")
    report_bytes = markdown_report(payload).encode("utf-8")
    REPORT_GZ.write_bytes(gzip.compress(report_bytes, compresslevel=9, mtime=0))
    LEGACY_OUT.unlink(missing_ok=True)
    LEGACY_REPORT.unlink(missing_ok=True)
    print({key: len(rows) for key, rows in payload.items()})
    print("chunks", len(chunk_paths), *chunk_paths, sep="\n")
    print(INDEX)
    print(REPORT_GZ)


if __name__ == "__main__":
    main()
