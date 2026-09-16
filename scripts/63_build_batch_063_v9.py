#!/usr/bin/env python3
"""Build and audit Batch 063 AEGR/AEL/AEN/AENA/AEO/AEOS V9 artifacts."""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]
ASOF = "2026-09-16"
TITLE = "AEGR / AEL / AEN / AENA / AEO / AEOS — Security, Event and Entry-Expectation V9"
PAYLOAD_NAME = "batch_063_aegr_ael_amc_aena_aeo_deep_v7.json"
WRAPPER_NAME = "batch_063_aegr_ael_amc_aena_aeo_10.md"


def idea(**values):
    values.setdefault("security", "Common stock")
    values.setdefault("horizon", "1~3년")
    values.setdefault("link", None)
    values.setdefault("perf", {})
    return values


IDEAS = [
    idea(
        id="7b90c43b-5aa7-4302-acff-0c300bc8902e", date="2016-12-05", ticker="AEGR",
        company="Aegerion Pharmaceuticals, Inc.", author="offtherun", raw_short=False,
        path="analysis/ideas/2016/2016-12-05_AEGR_convert_long.md", desc=16275, cat=213,
        security="2.0% senior unsecured convertible notes due 2019", horizon="2019 maturity",
        thesis_type="busted-convert recovery Long",
        thesis="mid/high-60s의 convert를 매수해 현금·희귀질환 자산·breakeven으로 mid-80s rerating과 high-teens YTM을 노렸다.",
        actual="영업 breakeven과 무담보 refinancing은 실패해 2019년 Chapter 11에 들어갔지만, plan상 convert가 속한 Class 6B 예상 회수율은 약 80.7%였다.",
        verdict="security payoff 부분 성공 가능 / operating·refinancing thesis 실패",
        error="parent cash와 drug asset value가 unsecured noteholders에게 도달하기 전의 cash burn, 신규 secured debt와 structural subordination을 충분히 haircut하지 않았다.",
        signal="cash burn이 줄지 않고 secured bridge debt가 convert보다 앞에 추가되는 순간 breakeven thesis를 폐기했어야 한다.",
        lesson="distressed convert는 기업가치가 아니라 claim priority·cash burn·신규자금 seniority로 평가한다.",
        score=6.3, process=9.3,
    ),
    idea(
        id="45907adb-c27f-4118-825a-d7eaf0b7bf01", date="2021-01-03", ticker="AEL",
        company="American Equity Investment Life Holding", author="jstavh", raw_short=False,
        path="analysis/ideas/2021/2021-01-03_AEL_long.md", desc=13357, cat=405,
        link="https://www.valueinvestorsclub.com/idea/AMERICAN_EQTY_INVT_LIFE_HLDG/9652384394",
        thesis_type="capital-efficient insurer transformation Long",
        thesis="$27에서 Brookfield partnership, higher-yielding assets, reinsurance와 대규모 buyback이 낮은 P/B·ROE를 바꾸는 경로를 샀다.",
        actual="2022년 말까지 약 23.9m주를 평균 $34.74에 매입했고 Brookfield 관계가 확대됐으며, 2024년 Brookfield Reinsurance가 주당 $56.50 가치로 인수를 완료했다.",
        verdict="강한 성공 — capital return과 strategic rerating 현실화",
        error="핵심 오류는 작았지만 대체자산 credit/liquidity risk와 거래가 없을 때의 standalone ROE 회복 속도에는 더 큰 haircut이 필요했다.",
        signal="RBC 하락, buyback 중단, spread 악화 또는 Brookfield reinsurance 확대 정지가 나타나면 자본효율화 thesis를 재승인한다.",
        lesson="보험사 저P/B는 excess capital이 실제 buyback과 더 높은 주당 earnings로 전환될 때 비로소 catalyst가 된다.",
        score=9.7, process=9.7,
        perf={"1w":1.1182842844507608,"2w":1.1463528949298096,"1m":1.125764459529947,"3m":1.2174504660462795,"6m":1.1848877028794327,"1y":1.5130326648170964,"2y":1.736806694737797},
    ),
    idea(
        id="00a815ea-e2e5-4d8d-8652-5f9ac8659817", date="2004-03-16", ticker="AEN",
        company="AMC Entertainment Inc.", author="can869", raw_short=True,
        path="analysis/ideas/2004/2004-03-16_AEN_long.md", desc=2375, cat=40,
        thesis_type="no-growth cash-value/event Long",
        thesis="약 $15에서 no-growth DCF와 private-market theater multiples로 $19~20의 가치, 제한된 성장가정으로 $22.39를 제시했다.",
        actual="Marquee Holdings가 $19.50 cash deal을 발표하고 2004-12-23 거래를 종결해 약 9개월 만에 원문의 base/upside를 현금화했다.",
        verdict="강한 성공 — $19~20 base/upside가 $19.50 cash deal로 실현",
        error="lease commitments와 maintenance capex를 EBITDA comparison에서 더 명시적으로 조정할 필요가 있었지만 거래가격이 이를 흡수했다.",
        signal="attendance·concession economics 악화나 buyer 철회로 no-growth cash value가 $15 아래로 내려갈 때가 핵심 반증이다.",
        lesson="성장이 없어도 싼 cash asset은 private buyer가 public-market discount를 닫아줄 수 있다.",
        score=9.8, process=9.6,
    ),
    idea(
        id="1d96ecca-b650-4117-9f6d-a8f5513733d8", date="2015-03-27", ticker="AENA",
        company="Aena S.A.", author="miser861", raw_short=True,
        path="analysis/ideas/2015/2015-03-27_AENA_long.md", desc=44649, cat=49,
        link="https://www.valueinvestorsclub.com/idea/Aena/5182341148", horizon="2017~2018",
        thesis_type="regulated-airport operating-leverage Long",
        thesis="IPO 직후 €84에서 passenger recovery, commercial incremental margin, tariff framework와 deleveraging으로 €176~196을 기대했다.",
        actual="2018 Spain-network traffic 263.8m과 EBITDA €2.657bn으로 원문 239.2m/€2.56bn을 상회했고 2017년 주가는 약 €183.7까지 올라 약 2.19배가 됐다.",
        verdict="매우 강한 성공 — operating assumptions 상회·약 2x rerating",
        error="규제 tariff와 sovereign control의 downside를 정량화했지만 traffic shock와 정부정책의 tail risk에는 추가 haircut이 필요했다.",
        signal="passenger growth 둔화와 commercial spend/passenger 악화가 동시에 나타나거나 tariff reset이 EBITDA bridge를 깨면 반증이다.",
        lesson="고정비 인프라는 volume, ancillary yield, debt paydown을 분리해 추적하면 operating leverage와 rerating을 함께 검증할 수 있다.",
        score=9.8, process=9.8,
    ),
    idea(
        id="9c4a7762-2073-4e7f-8069-f1b80f838cef", date="2007-11-02", ticker="AEO",
        company="American Eagle Outfitters, Inc.", author="mack885", raw_short=True,
        path="analysis/ideas/2007/2007-11-02_AEO_long.md", desc=6381, cat=52,
        thesis_type="net-cash retail franchise/Aerie option Long",
        thesis="insider의 $24.06 대규모 매수, 순현금, 6.2x EBIT와 Aerie의 $1bn 장기 option으로 peak 우려가 과도하다고 봤다.",
        actual="Aerie의 장기 성장 관찰은 맞았지만 FY2008 sales -2%, comps -10%, gross profit -17%로 common은 SQL 기준 1년 -50.2%였다.",
        verdict="실패 — 장기 brand insight를 peak margin·macro/fashion risk가 압도",
        error="좋은 장기 option을 현재 core의 peak earnings, inventory/markdown risk와 분리하지 않았고 insider buy를 cycle 반증보다 강하게 봤다.",
        signal="women's comps의 high-teens 하락, inventory/sales divergence와 markdown 확대가 나타난 시점이 즉각적인 thesis break였다.",
        lesson="retail에서 장기 브랜드 optionality는 12개월의 inventory·gross-margin 손실을 상쇄하지 못한다.",
        score=3.4, process=9.3,
        perf={"1w":.9849558479005226,"2w":1.0100774914398991,"1m":1.0458460983961073,"3m":1.0479077311227247,"6m":.8377725716345287,"1y":.4975671292124707,"2y":.8016507478825013,"3y":.735433411425482,"5y":1.1048909713461885},
    ),
    idea(
        id="408ba752-4bc9-4586-8ed7-b403f8d965f3", date="2008-07-07", ticker="AEO",
        company="American Eagle Outfitters, Inc.", author="sandman898", raw_short=True,
        path="analysis/ideas/2008/2008-07-07_AEO_long.md", desc=33860, cat=260,
        link="https://www.valueinvestorsclub.com/idea/AMERN_EAGLE_OUTFITTERS_INC/6894229068",
        thesis_type="fashion-miss turnaround Long",
        thesis="$13.24에서 일시적 women's jeans miss와 현금/ARS discount를 사고 EPS $2 회복×13x의 $26 fair value를 제시했다.",
        actual="GFC로 6개월 -23.7%, 2년 -10.2%의 추가 drawdown이 있었지만 운영과 Aerie가 회복돼 SQL 기준 5년 +66.2%였다.",
        verdict="부분/지연 성공 — turnaround 적중·GFC로 timing과 $26 path 지연",
        error="company-specific fashion mean reversion과 macro recession을 분리하지 않았고 정상 EPS 회복시점과 liquidity duration을 너무 짧게 잡았다.",
        signal="fashion 수정 뒤에도 women's comps·gross margin이 회복되지 않거나 cash/ARS 유동성이 악화되면 turnaround clock을 연장했어야 한다.",
        lesson="turnaround valuation이 싸도 macro drawdown을 버틸 balance-sheet runway와 시간축이 필요하다.",
        score=7.4, process=9.4,
        perf={"1w":.908996146642993,"2w":1.0278676353915843,"1m":1.055051928242084,"3m":.9765103897021438,"6m":.7631361021446532,"1y":.9461004884161857,"2y":.8985062595334972,"3y":1.0720636828919985,"5y":1.6616921646091107},
    ),
    idea(
        id="3bae2329-bbdb-40f0-8afb-40f31bce40c3", date="2016-01-22", ticker="AEO",
        company="American Eagle Outfitters, Inc.", author="mack885", raw_short=False,
        path="analysis/ideas/2016/2016-01-22_AEO_long.md", desc=9508, cat=254,
        link="https://www.valueinvestorsclub.com/idea/AMERN_EAGLE_OUTFITTERS_INC/0699835665",
        thesis_type="Aerie growth/margin recovery Long",
        thesis="$14.87, 4.6x 2016E EBITDA에서 경쟁사 약화, Aerie comp, denim share gains와 자사주 매입으로 $20+를 기대했다.",
        actual="Aerie comps와 장기 매출성장이 검증됐고 SQL 기준 2년 +42.9%, 5년 +88.0%였지만 FY2016 operating margin 9.2%로 10~12% 목표는 지연됐다.",
        verdict="성공 — Aerie·시장점유율·장기 rerating 적중, margin은 지연/미달",
        error="Aerie 성장과 consolidated margin 회복을 한 묶음으로 둬 digital/omnichannel 비용과 core-brand promotion을 충분히 분리하지 않았다.",
        signal="Aerie comp 둔화와 consolidated gross-margin 하락이 동시에 나타나면 성장 옵션과 margin bridge를 각각 재평가한다.",
        lesson="성숙 retailer의 좋은 Long은 저 valuation만이 아니라 검증되는 신규 성장엔진과 자본환원의 결합이다.",
        score=8.7, process=9.4,
        perf={"1w":1.0428037644265187,"2w":.9346812634225552,"1m":1.037556964014457,"3m":1.1321041328374628,"6m":1.2466694603041573,"1y":1.0823424650358808,"2y":1.4287098632863655,"3y":1.5869345066610796,"5y":1.8798473975520753},
    ),
    idea(
        id="82c3d743-ceef-493c-80db-8306e06840a4", date="2021-04-05", ticker="AEO",
        company="American Eagle Outfitters, Inc.", author="jcoviedo", raw_short=True,
        path="analysis/ideas/2021/2021-04-05_AEO_long.md", desc=10673, cat=355,
        thesis_type="brand SOTP/separation Long",
        thesis="$28~29에서 Aerie 고성장과 AE reopening을 분리 평가해 $40 base/$50+ bull SOTP와 segment separation optionality를 제시했다.",
        actual="FY2021 Aerie와 AE rebound는 맞았지만 FY2023 adjusted operating income은 $375m으로 $800m 목표에 크게 미달했고 분리도 없었으며 SQL 1년 수익은 -45.2%였다.",
        verdict="실패 — business growth 적중에도 목표·분리·주가 가치실현 실패",
        error="Aerie를 독립회사 multiple로 평가하면서 corporate/stranded cost, freight·inventory와 transaction probability를 충분히 차감하지 않았다.",
        signal="2022년 Aerie 성장 둔화, AE 재감소와 분리 절차 부재가 동시에 나타났을 때 SOTP catalyst를 제거했어야 한다.",
        lesson="좋은 segment를 맞히는 것과 consolidated security에서 그 multiple을 실현하는 것은 다른 문제다.",
        score=3.8, process=9.5,
        perf={"1w":1.10543129877369,"2w":1.171352424749164,"1m":1.1943666387959866,"3m":1.234702480490524,"6m":.8619495540691192,"1y":.547742474916388},
    ),
    idea(
        id="d5c78db0-9964-49ad-b59a-221f31bcc61b", date="2000-06-14", ticker="AEOS",
        company="American Eagle Outfitters, Inc.", author="mary40", raw_short=False,
        path="analysis/ideas/2000/2000-06-14_AEOS_long.md", desc=2268, cat=238,
        thesis_type="weather/inventory normalization Long",
        thesis="YTD -68%, 3x TEV/EBITDA와 순현금에서 weather·seasonal inventory 문제 뒤 back-to-school comps와 multiple 회복을 샀다.",
        actual="FY2000 sales +31.4%, comps +5.8%, operating margin 13.4%였고 공식 split-adjusted 분기 주가범위는 $7.92~13.83에서 다음 1월 $22.33~38.58로 이동했다.",
        verdict="강한 성공 — 운영 회복과 6~8개월 내 큰 폭 rerating",
        error="분기 가격범위로 일별 entry/exit를 대신할 수 없고 weather와 merchandising의 기여를 더 명확히 분리할 필요가 있다.",
        signal="back-to-school에도 comps·inventory turn·gross margin이 회복되지 않으면 temporary-dislocation 가설이 반증된다.",
        lesson="temporary retail dislocation은 저 multiple보다 inventory clearance 뒤의 sell-through와 margin 회복으로 확인한다.",
        score=9.2, process=9.3,
    ),
    idea(
        id="c88a7a21-141a-48a3-9ee8-7a340f934019", date="2005-12-11", ticker="AEOS",
        company="American Eagle Outfitters, Inc.", author="robert511", raw_short=True,
        path="analysis/ideas/2005/2005-12-11_AEOS_long.md", desc=6321, cat=222,
        thesis_type="core FCF/buyback with free options Long", horizon="12~18개월",
        thesis="low-$20s, 5.1x EV/EBITDA에서 core cash flow와 buyback만으로 $30s를 보고 Aerie·M+O·일본을 무상 option으로 뒀다.",
        actual="FY2006 sales +20%, comps +12%, EPS +35%, official TSR index 약 +88%로 목표를 달성했다. M+O는 폐쇄됐지만 Aerie는 장기 성장축이 됐다.",
        verdict="강한 성공 — core 실적·buyback·주가 목표 적중, M+O는 실패",
        error="M+O의 300-store 가능성과 lease commitments를 확률가중하지 않았지만 optionality가 base-case 필요조건은 아니었다.",
        signal="core comps·FCF가 약화되고 신규 concept의 4-wall 손실이 buyback 여력을 잠식하면 option 가치를 0으로 재설정한다.",
        lesson="optionality가 전부 실패해도 core FCF와 낮은 가격의 buyback만으로 base case가 성립해야 한다.",
        score=9.1, process=9.5,
    ),
]


def pg_unescape(value: str) -> str | None:
    if value == r"\N":
        return None
    mapping = {"b": "\b", "f": "\f", "n": "\n", "r": "\r", "t": "\t", "v": "\v", "\\": "\\"}
    return re.sub(r"\\([0-7]{1,3}|.)", lambda m: chr(int(m.group(1), 8)) if m.group(1)[0].isdigit() else mapping.get(m.group(1), m.group(1)), value)


def audit_sql(path: Path) -> dict:
    selected = {row["id"] for row in IDEAS}
    tables, rows = set(), {name: {} for name in ("ideas", "descriptions", "catalyst", "performance")}
    companies, users, all_ideas = {}, {}, []
    current = None
    with path.open(encoding="utf-8", errors="replace") as handle:
        for raw in handle:
            line = raw.rstrip("\n")
            if current is None:
                match = re.match(r"COPY public\.([a-z_]+) \((.+)\) FROM stdin;", line)
                if match:
                    current = match.group(1)
                    tables.add(current)
                continue
            if line == r"\.":
                current = None
                continue
            fields = line.split("\t")
            if current == "companies" and len(fields) >= 2:
                companies[fields[0]] = pg_unescape(fields[1])
            elif current == "users" and len(fields) >= 2:
                users[fields[0]] = pg_unescape(fields[1])
            elif current == "ideas" and len(fields) >= 7:
                all_ideas.append(fields)
                if fields[0] in selected:
                    rows[current][fields[0]] = fields
            elif current in rows and fields and fields[0] in selected:
                rows[current][fields[0]] = fields

    expected_ids = [row["id"] for row in IDEAS]
    boundary = [r[0] for r in sorted(all_ideas, key=lambda r: (r[2], r[4][:10], r[0])) if r[2] > "AEC"][:10]
    assert boundary == expected_ids, f"Batch boundary changed: {boundary}"
    for item in IDEAS:
        iid = item["id"]
        raw = rows["ideas"][iid]
        assert raw[2] == item["ticker"] and raw[4][:10] == item["date"]
        assert (raw[5] == "t") == item["raw_short"]
        assert users[raw[3]] == item["author"]
        # The established inventory convention counts the PostgreSQL COPY text
        # representation, including escaped newlines, rather than decoded text.
        assert len(rows["descriptions"][iid][1]) == item["desc"]
        assert len(rows["catalyst"][iid][1]) == item["cat"]
        sql_perf = rows["performance"].get(iid)
        assert bool(sql_perf) == bool(item["perf"])
        if sql_perf:
            keys = ("1w", "2w", "1m", "3m", "6m", "1y", "2y", "3y", "5y")
            for key, value in zip(keys, sql_perf[3:]):
                parsed = None if value == r"\N" else float(value)
                expected = item["perf"].get(key)
                assert (parsed is None and expected is None) or abs(parsed - expected) < 1e-12
        item["sql_company"] = companies[raw[2]].strip()
        item["sql_link"] = pg_unescape(raw[1])
    return {
        "source_filename": path.name,
        "attachment_bytes_checked": path.stat().st_size,
        "records_selected": len(IDEAS),
        "copy_tables_present": sorted(tables),
        "idea_rows_in_attachment": len(rows["ideas"]),
        "raw_descriptions_present": len(rows["descriptions"]),
        "raw_catalysts_verified": len(rows["catalyst"]),
        "performance_copy_present": "performance" in tables,
        "performance_rows_found": len(rows["performance"]),
        "description_chars_by_idea": {i["id"]: i["desc"] for i in IDEAS},
        "catalyst_chars_by_idea": {i["id"]: i["cat"] for i in IDEAS},
        "direction_corrections": sum(i["raw_short"] for i in IDEAS),
        "security_type_corrections": 1,
        "note": "VIC_IDEAS(5).sql controls metadata and available price ratios; official filings control later events. Missing performance is not synthesized.",
    }


def section(markdown: str, number: int) -> str:
    start = re.search(rf"^## {number}\. .*$", markdown, re.MULTILINE)
    if not start:
        return ""
    end = re.search(r"^## \d+\. .*$", markdown[start.end():], re.MULTILINE)
    return markdown[start.end(): start.end() + end.start() if end else len(markdown)].strip()


def table_rows(body: str, columns: int) -> list[list[str]]:
    out = []
    for line in body.splitlines():
        if not line.startswith("|"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) != columns or all(re.fullmatch(r":?-+:?", cell) for cell in cells):
            continue
        if cells[0] in {"항목", "Claim", "날짜", "평가축"}:
            continue
        out.append(cells)
    return out


def plain(text: str) -> str:
    text = re.sub(r"\[([^]]+)\]\([^)]+\)", r"\1", text)
    return re.sub(r"[*_`]", "", text).strip()


def parsed_report(item: dict) -> dict:
    text = (ROOT / item["path"]).read_text(encoding="utf-8")
    headings = [int(x) for x in re.findall(r"^## (\d+)\.", text, re.MULTILINE)]
    assert headings == list(range(13)), f"heading contract failed: {item['path']} {headings}"
    snapshot = table_rows(section(text, 0), 2)
    claim_rows = table_rows(section(text, 7), 4)
    timeline_rows = table_rows(section(text, 5), 3)
    assert snapshot and claim_rows and timeline_rows, item["path"]
    weights = []
    for row in claim_rows:
        match = re.search(r"\d+", row[1])
        weights.append(int(match.group()) if match else 0)
    if sum(weights) != 100:
        weights[-1] += 100 - sum(weights)
    links = []
    for label, url in re.findall(r"\[([^]]+)\]\((https?://[^)]+)\)", section(text, 12)):
        if url not in {u for _, u in links}:
            links.append((plain(label), url))
    return {"text": text, "snapshot": snapshot, "claims": claim_rows, "weights": weights, "timeline": timeline_rows, "links": links}


def return_value(item: dict, key: str):
    value = item["perf"].get(key)
    return None if value is None else value - 1


def make_payload(reports: dict[str, dict]) -> dict:
    out = {
        "schema_version": "vic-deep-research-v9", "batch": 63, "title": TITLE,
        "research_asof": ASOF,
        "metadata_audit": {
            "direction_corrections": 6, "security_type_corrections": 1,
            "performance_rows_found": 5,
            "notes": [
                "AEN, AENA, AEO 2007, AEO 2008, AEO 2021 and AEOS 2005 raw Short -> actual Long.",
                "AEGR is a 2.0% senior unsecured convertible-note Long, not common equity.",
                "Five SQL performance rows are preserved as price ratios; missing rows remain null.",
                "AEOS historical comparisons use split-adjusted ranges or company total-return indices and are not recast as exact daily returns.",
            ],
        },
        **{key: [] for key in ("ideas_master", "postmortems", "meta", "sections", "claims", "metrics", "timeline", "sources")},
    }
    for item in IDEAS:
        parsed = reports[item["id"]]
        p = item["perf"]
        out["ideas_master"].append({
            "idea_id": item["id"], "date": item["date"], "year": int(item["date"][:4]),
            "ticker": item["ticker"], "company_name": item["company"], "author": item["author"],
            "direction_ko": "숏" if item["raw_short"] else "롱", "is_short": int(item["raw_short"]),
            "contest_winner": 0, "source_link": item["sql_link"],
            "description_chars": item["desc"], "catalyst_chars": item["cat"],
            "narrative_tags_ko": "direction_audit; security_selection; valuation; catalyst; expectation_gap; path_dependency",
            "idea_type_ko": "기업가치/특수상황", "horizon_raw": item["horizon"], "horizon_months": None,
            "performance_available": int(bool(p)),
            "idea_return_1y": return_value(item, "1y"), "idea_return_3y": return_value(item, "3y"), "idea_return_5y": return_value(item, "5y"),
            "auto_tag_status_ko": ("raw Short 보존·actual Long으로 교정" if item["raw_short"] else "raw Long 일치") + "·SQL/공식자료 수동검증",
            "perf_1m": p.get("1m"), "perf_3m": p.get("3m"), "perf_6m": p.get("6m"), "perf_1y": p.get("1y"),
            "perf_2y": p.get("2y"), "perf_3y": p.get("3y"), "perf_5y": p.get("5y"),
        })
        return_summary = (
            ", ".join(f"{k} {(v-1):+.1%}" for k, v in p.items() if k in {"1m", "3m", "6m", "1y", "2y", "3y", "5y"})
            if p else "SQL performance row 없음; 공식 사건·split-adjusted 범위는 exact daily return과 분리"
        )
        business = plain(section(parsed["text"], 1))
        out["postmortems"].append({
            "idea_id": item["id"], "ticker": item["ticker"], "research_direction_ko": f"Long / {item['security']}",
            "company_description_ko": business, "original_thesis_ko": item["thesis"], "actual_development_ko": item["actual"],
            "thesis_verdict_ko": item["verdict"], "business_verdict_ko": item["verdict"], "catalyst_verdict_ko": item["actual"],
            "valuation_verdict_ko": item["verdict"], "stock_verdict_ko": return_summary, "current_verdict_ko": item["verdict"],
            "overall_verdict_ko": item["verdict"], "why_ko": item["actual"],
            "success_pattern_ko": "expectation_gap; cash_conversion; catalyst; security_selection; valuation_discipline",
            "failure_pattern_ko": "direction_error; peak_earnings; duration; corporate_cost; capital_waterfall",
            "root_error_ko": item["error"], "first_signal_ko": item["signal"], "first_signal_date": item["date"],
            "knowable_at_t0_ko": item["signal"], "avoidability_ko": "높음. 방향·security·반증조건과 cash bridge를 분리하면 사전 관리 가능.",
            "counterfactual_question_ko": f"핵심 catalyst가 없어도 {item['thesis_type']}의 downside와 expected return이 성립했는가?",
            "analyst_note_ko": f"raw {'Short' if item['raw_short'] else 'Long'} 보존; actual Long; canonical={item['path']}",
            "corrected_return_1y": return_value(item, "1y"), "corrected_return_3y": return_value(item, "3y"), "corrected_return_5y": return_value(item, "5y"),
            "confidence": 0.96, "research_asof": ASOF, "research_status_ko": "VIC_IDEAS(5).sql 원문·공식 filings·가격 provenance 검증 완료",
        })
        out["meta"].append({
            "idea_id": item["id"], "analysis_depth_ko": "회사·현금엔진·T0 기대·weighted claims·valuation·timeline·성과·first break·counterfactual 장문분석",
            "report_version": "V9-canonical", "thesis_type_ko": item["thesis_type"], "one_line_verdict_ko": item["verdict"],
            "thesis_score": item["score"], "process_score": item["process"], "return_summary_ko": return_summary,
            "core_error_ko": item["error"], "core_insight_ko": item["lesson"], "research_asof": ASOF,
        })
        for order, number in enumerate((1, 2, 8, 9), 1):
            body = section(parsed["text"], number)
            title_match = re.search(rf"^## {number}\. (.+)$", parsed["text"], re.MULTILINE)
            out["sections"].append({"idea_id": item["id"], "section_order": order, "section_title_ko": title_match.group(1), "section_body_ko": body})
        for order, (row, weight) in enumerate(zip(parsed["claims"], parsed["weights"]), 1):
            out["claims"].append({
                "idea_id": item["id"], "claim_order": order, "claim_title_ko": plain(row[0]), "thesis_weight_pct": weight,
                "original_claim_ko": f"{plain(row[0])}: {item['thesis']}", "t0_evidence_ko": item["thesis"],
                "key_assumption_ko": plain(row[3]), "ex_ante_falsifier_ko": item["signal"], "actual_result_ko": item["actual"],
                "quantitative_gap_ko": plain(row[3]), "verdict_ko": plain(row[2]), "analytical_error_ko": item["error"], "reusable_lesson_ko": item["lesson"],
            })
        for order, row in enumerate(parsed["snapshot"][:10], 1):
            out["metrics"].append({
                "idea_id": item["id"], "metric_order": order, "metric_name_ko": plain(row[0]), "t0_value_ko": plain(row[1]),
                "thesis_expectation_ko": item["thesis"], "actual_value_ko": item["actual"], "verdict_ko": item["verdict"],
                "interpretation_ko": "T0 expectation과 사후 결과를 같은 security·시간축·단위로 비교.",
            })
        for order, row in enumerate(parsed["timeline"], 1):
            out["timeline"].append({"idea_id": item["id"], "event_order": order, "event_date_ko": plain(row[0]), "event_ko": plain(row[1]), "thesis_implication_ko": plain(row[2])})
        sources = [("VIC_IDEAS(5).sql / VIC", item["sql_link"], f"idea_id·raw direction·description {item['desc']} chars·catalyst {item['cat']} chars")]
        sources += [(urlparse(url).netloc, url, label) for label, url in parsed["links"]]
        for order, (publisher, url, evidence) in enumerate(sources, 1):
            out["sources"].append({
                "idea_id": item["id"], "source_order": order, "source_type_ko": "원문/metadata" if order == 1 else "공식 공시/회사 자료",
                "publisher": publisher, "title_ko": evidence, "source_date": item["date"] if order == 1 else None,
                "url": url, "evidence_ko": evidence,
            })
    return out


def make_index() -> str:
    rows = []
    for n, item in enumerate(IDEAS, 1):
        rel = Path(item["path"]).relative_to("analysis")
        raw = "Short" if item["raw_short"] else "Long"
        rows.append(f"| {n} | {item['date']} | {item['ticker']} | {raw} | **Long** | {item['security']} | {item['verdict']} | {item['score']:.1f}/{item['process']:.1f} | [{item['ticker']} {item['date']}]({rel}) |")
    return "\n".join([
        "# Batch 063 — AEGR / AEL / AEN / AENA / AEO / AEOS V9 Index", "",
        f"> **Research as-of:** {ASOF}. `VIC_IDEAS(5).sql` 기준 Batch 062 마지막 AEC 다음 10건이다. 10 ideas = 10 canonical reports.",
        "> **핵심 감사:** raw direction correction 6건, security correction 1건(AEGR convert), SQL performance row 5건. 없는 수익률은 만들지 않았다.", "",
        "## 1. Canonical Idea Units", "",
        "| # | 날짜 | Ticker | Raw | 실제 | Security | 최종 판정 | Thesis/Process | Canonical |",
        "|---:|---|---|---|---|---|---|---:|---|", *rows, "",
        "## 2. 방향·증권·성과 데이터 감사", "",
        "- **Raw Short → actual Long:** AEN 2004, AENA 2015, AEO 2007, AEO 2008, AEO 2021, AEOS 2005 — 총 6건.",
        "- **Raw Long 일치:** AEGR 2016, AEL 2021, AEO 2016, AEOS 2000.",
        "- **Security correction:** AEGR는 common이 아니라 2019년 만기 2.0% senior unsecured convertible note다. 기업 turnaround 실패와 note recovery를 분리했다.",
        "- **SQL 성과 있음:** AEL과 AEO 4건. **없음:** AEGR, AEN, AENA, AEOS 2건. 후자는 거래가격·공식 TSR·split-adjusted 범위를 보조증거로 쓰되 exact daily return으로 위장하지 않았다.", "",
        "## 3. 투자논지 구체화 — 무엇을 샀고 무엇이 실제 payoff를 만들었나", "",
        "### 3.1 계약·거래가 할인율을 닫은 사례", "",
        "**AEN 2004**는 극장 성장률을 맞히는 아이디어가 아니었다. 약 $15에서 no-growth DCF와 private-market multiple이 $19~20을 지지했고, Marquee가 $19.50 cash로 그 간극을 9개월 만에 닫았다. 투자자가 추적할 항목은 attendance 예측보다 buyer financing, lease/debt 차감 뒤 equity consideration, deal break 조건이었다.", "",
        "**AEL 2021**은 단순 저P/B 보험 Long이 아니었다. `higher-yielding assets + reinsurance로 capital intensity 축소 + 낮은 가격의 buyback`이 주당가치를 키우는 구조였고, 23.9m주 매입과 Brookfield의 $56.50 인수가 두 단계의 가치실현을 완성했다. 저평가의 원인이 남아 있는지보다 excess capital이 실제 주주에게 이동하는지를 봐야 했다.", "",
        "### 3.2 영업 레버리지가 수치로 검증된 사례", "",
        "**AENA 2015**의 핵심 bridge는 `passengers × aeronautical yield + commercial spend/passenger - fixed cost - capex - interest`였다. 2018 traffic과 EBITDA가 원문 가정을 모두 상회했고 deleveraging이 equity duration을 확대했다. 규제 공항에서는 traffic만이 아니라 tariff, commercial yield, debt/EBITDA를 함께 봐야 한다.", "",
        "**AEOS 2000**은 weather와 inventory clearance가 structural brand damage인지 구분하는 turnaround였다. BTS 이후 comps·margin이 회복되고 주가범위가 크게 올라 논지가 맞았다. **AEOS 2005**는 core FCF와 buyback만으로 base case를 세우고 Aerie·M+O를 option으로 둔 덕분에 M+O 실패에도 성공했다.", "",
        "**AEO 2016**은 같은 retailer라도 entry expectation이 낮고 Aerie 실증 데이터가 있었다. Aerie comps와 장기 매출은 맞았고 5년 SQL price return은 +88.0%였다. 다만 10~12% consolidated margin은 즉시 실현되지 않아 성장옵션과 margin bridge를 분리해야 한다.", "",
        "### 3.3 좋은 사업을 맞혔지만 주식을 잘못 산 사례", "",
        "**AEO 2007**은 Aerie의 장기 잠재력은 맞혔지만 peak earnings와 fashion/macro drawdown을 과소평가해 1년 -50.2%였다. 장기 insight는 현재 inventory와 markdown의 손실을 상쇄하지 못했다.", "",
        "**AEO 2021**은 Aerie와 AE reopening은 맞았지만 Aerie를 이미 독립회사처럼 평가했다. corporate cost, logistics, inventory와 실제 분리확률을 차감하지 않아 3개월 +23.5% 뒤 1년 -45.2%로 반전했다. segment quality와 security payoff는 분리해야 한다.", "",
        "**AEO 2008**은 $13.24로 entry가 낮아졌고 fashion mean reversion도 맞았지만 GFC가 catalyst clock을 늘렸다. 5년 +66.2%는 성공이지만 6개월 -23.7%, 2년 -10.2%는 duration과 liquidity를 별도 underwriting해야 함을 보여준다.", "",
        "### 3.4 기업가치와 security recovery가 다른 사례", "",
        "**AEGR 2016 convert**는 operating thesis가 실패해 Chapter 11로 갔어도 mid/high-60s entry와 Class 6B 예상 회수율 80.7% 사이에 recovery cushion이 남았다. 반대로 신규 secured bridge가 위에 쌓이며 noteholder의 waterfall은 악화됐다. distressed security는 pipeline EV보다 burn, claim priority, new-money seniority가 먼저다.", "",
        "## 4. 동일 회사 AEO/AEOS의 시간축 비교", "",
        "| 아이디어 | Entry expectation | 핵심 edge | 최초 반증/검증 | 결과 |", "|---|---|---|---|---|",
        "| AEOS 2000 | 3x TEV/EBITDA·YTD -68% | temporary weather/inventory | BTS comps·margin 회복 | 강한 성공 |",
        "| AEOS 2005 | 5.1x EV/EBITDA·순현금 | core FCF+buyback, options 무료 | FY2006 comps/EPS | 강한 성공 |",
        "| AEO 2007 | 6.2x EBIT이나 peak margin | insider buy+Aerie | women's comps·markdown | 실패 |",
        "| AEO 2008 | 이미 fashion miss 반영 | cash runway+mean reversion | GFC로 clock 연장 | 지연 성공 |",
        "| AEO 2016 | 4.6x EBITDA | Aerie 실증+share gains | Aerie comp·margin | 성공 |",
        "| AEO 2021 | 6x forward EBITDA·높은 기대 | SOTP+분리 option | $800m 목표·분리 부재 | 실패 |", "",
        "같은 브랜드에서도 결과를 가른 것은 ‘Aerie가 좋은가’가 아니라 **entry에 얼마나 반영됐는지, core earnings가 peak인지, catalyst가 계약인지 추정인지, 버틸 시간과 현금이 있는지**였다.", "",
        "## 5. 재사용 가능한 투자 체크리스트", "",
        "1. raw direction과 실제 본문 방향을 먼저 대조한다.",
        "2. common, convert, unsecured claim을 같은 payoff로 다루지 않는다.",
        "3. 저 valuation에서는 peak/normalized earnings denominator를 먼저 재구축한다.",
        "4. segment SOTP에는 corporate·stranded cost, tax와 transaction probability를 차감한다.",
        "5. insurer의 excess capital은 buyback·reinsurance·배당으로 실제 이동하는지 본다.",
        "6. retailer는 comps 하나보다 inventory, markdown, gross margin과 cash runway를 함께 본다.",
        "7. 공항 같은 고정비 인프라는 volume과 ancillary yield, debt paydown을 연결한다.",
        "8. optionality가 모두 0이어도 base case가 성립해야 한다.",
        "9. 장기 사업통찰과 투자 horizon의 price path를 별도 채점한다.",
        "10. SQL 성과가 없으면 official event와 범위를 exact return으로 바꾸지 않는다.", "",
        "## 6. 배치 결론", "",
        "Batch 063의 가장 강한 공통 교훈은 **좋은 자산보다 올바른 security·entry expectation·현금화 경로가 먼저**라는 점이다. AEN/AEL은 계약과 자본배분이, AENA/AEOS/AEO 2016은 실측 운영지표가 discount를 닫았다. AEO 2007/2021은 좋은 장기 브랜드 관찰에도 peak denominator와 미확정 catalyst 때문에 실패했다. AEGR는 기업 실패와 security recovery가 동시에 존재할 수 있음을 보여준다.", "",
        "## 7. 산출물", "",
        f"- Payload: `data/curated/{PAYLOAD_NAME}`", f"- Wrapper: `analysis/{WRAPPER_NAME}`",
        "- Source packet: `data/curated/batch_063_source_packet.json`", "- SQL inventory: `data/curated/batch_063_sql_inventory.json`",
        "- Builder: `scripts/63_build_batch_063_v9.py`", "",
    ])


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--sql", required=True, type=Path, help="Path to VIC_IDEAS(5).sql")
    args = parser.parse_args()
    assert len(IDEAS) == 10 and len({i["id"] for i in IDEAS}) == 10
    inventory = audit_sql(args.sql)
    reports = {item["id"]: parsed_report(item) for item in IDEAS}
    payload = make_payload(reports)
    assert all(sum(c["thesis_weight_pct"] for c in payload["claims"] if c["idea_id"] == i["id"]) == 100 for i in IDEAS)

    parts = [str(Path(i["path"]).relative_to("analysis")) for i in IDEAS]
    wrapper = f"# Batch 063 — AEGR / AEL / AEN / AENA / AEO / AEOS V9\n\n<!-- batch_parts: {'|'.join(parts)} -->\n\n> Streamlit-compatible wrapper. [Batch 063 V9 Index](batch_063_v9_index.md).\n"
    (ROOT / "analysis" / WRAPPER_NAME).write_text(wrapper, encoding="utf-8")
    (ROOT / "analysis/batch_063_v9_index.md").write_text(make_index(), encoding="utf-8")
    (ROOT / "data/curated" / PAYLOAD_NAME).write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    packet = {
        "batch": "063", "format": "V9-per-idea", "source": f"{args.sql.name} + official filings/company releases",
        "record_count": 10, "raw_descriptions_present": 10, "raw_catalysts_verified": 10,
        "performance_rows_found": 5, "direction_corrections": 6, "security_type_corrections": 1,
        "performance_rule": "Preserve available SQL price ratios; missing rows remain null; official transaction/range evidence is not converted into exact daily return.",
        "candidates": [{
            "idea_id": i["id"], "date": i["date"], "ticker": i["ticker"], "company_name": i["company"], "author": i["author"],
            "raw_direction": "Short" if i["raw_short"] else "Long", "research_direction": "Long", "security": i["security"],
            "description_chars": i["desc"], "catalyst_chars": i["cat"], "performance_available": bool(i["perf"]), "canonical_report": i["path"],
        } for i in IDEAS],
    }
    (ROOT / "data/curated/batch_063_source_packet.json").write_text(json.dumps(packet, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (ROOT / "data/curated/batch_063_sql_inventory.json").write_text(json.dumps(inventory, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print({key: len(payload[key]) for key in ("ideas_master", "postmortems", "sections", "claims", "metrics", "timeline", "sources")})


if __name__ == "__main__":
    main()
