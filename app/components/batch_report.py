"""Render reviewed Batch markdown reports."""
from __future__ import annotations
import gzip, json, re
from pathlib import Path
import streamlit as st

ROOT = Path(__file__).resolve().parents[2]
BATCH_SOURCES = (
("farfetch_deep_v7.json","batch_001_farfetch.md","Batch 001"),
("hawaiian_electric_deep_v7.json","batch_002_hawaiian_electric.md","Batch 002"),
("american_express_gfc_deep_v7.json","batch_003_american_express_gfc.md","Batch 003"),
("american_express_costco_antitrust_deep_v7.json","batch_004_american_express_costco_antitrust.md","Batch 004"),
("american_express_pandemic_rewards_deep_v7.json","batch_005_american_express_pandemic_rewards.md","Batch 005"),
("western_union_full_history_deep_v7.json","batch_006_western_union_full_history.md","Batch 006"),
("chesapeake_full_history_deep_v7.json","batch_007_chesapeake_full_history.md","Batch 007"),
("batch_008_ezpw_lov_nick_cost_deep_v7.json","batch_008_ezpw_lov_nick_cost_30.md","Batch 008"),
("batch_009_nflx_adt_atvi_baba_deep_v7.json","batch_009_nflx_adt_atvi_baba_30.md","Batch 009"),
("batch_010_transport_capital_structure_deep_v7.json","batch_010_transport_capital_structure_30.md","Batch 010"),
("batch_011_apple_google_deep_v7.json","batch_011_apple_google_10.md","Batch 011"),
("batch_012_alt_managers_deep_v7.json","batch_012_alt_managers_10.md","Batch 012"),
("batch_013_payments_deep_v7.json","batch_013_payments_10.md","Batch 013"),
("batch_014_tmus_atus_deep_v7.json","batch_014_tmus_atus_10.md","Batch 014"),
("batch_015_charter_comcast_deep_v7.json","batch_015_charter_comcast_10.md","Batch 015"),
("batch_016_cigna_unitedhealth_deep_v7.json","batch_016_cigna_unitedhealth_10.md","Batch 016"),
("batch_017_sprint_att_deep_v7.json","batch_017_sprint_att_10.md","Batch 017"),
("batch_018_genworth_assured_guaranty_deep_v7.json","batch_018_genworth_assured_guaranty_10.md","Batch 018"),
("batch_019_visteon_goodyear_deep_v7.json","batch_019_visteon_goodyear_10.md","Batch 019"),
("batch_020_fossil_abercrombie_deep_v7.json","batch_020_fossil_abercrombie_10.md","Batch 020"),
("batch_021_echostar_iridium_deep_v7.json","batch_021_echostar_iridium_10.md","Batch 021"),
("batch_022_geo_corecivic_deep_v7.json","batch_022_geo_corecivic_10.md","Batch 022"),
("batch_023_hp_western_digital_deep_v7.json","batch_023_hp_western_digital_10.md","Batch 023"),
("batch_024_amazon_iac_deep_v7.json","batch_024_amazon_iac_10.md","Batch 024"),
("batch_025_ibkr_discover_deep_v7.json","batch_025_ibkr_discover_10.md","Batch 025"),
("batch_026_seritage_gyrodyne_deep_v7.json","batch_026_seritage_gyrodyne_10.md","Batch 026"),
("batch_027_tesla_carmax_deep_v7.json","batch_027_tesla_carmax_10.md","Batch 027"),
("batch_028_tripadvisor_grubhub_deep_v7.json","batch_028_tripadvisor_grubhub_10.md","Batch 028"),
("batch_029_uhal_united_rentals_deep_v7.json","batch_029_uhal_united_rentals_10.md","Batch 029"),
("batch_030_clearwater_crown_deep_v7.json","batch_030_clearwater_crown_10.md","Batch 030"),
("batch_031_rentacenter_worldacceptance_deep_v7.json","batch_031_rentacenter_worldacceptance_10.md","Batch 031"),
("batch_032_bjri_petmed_deep_v7.json","batch_032_bjri_petmed_10.md","Batch 032"),
("batch_033_pico_grace_deep_v7.json","batch_033_pico_grace_10.md","Batch 033"),
("batch_034_comstock_crocodile_franklincovey_deep_v7.json","batch_034_comstock_crocodile_franklincovey_10.md","Batch 034"),
("batch_035_plus_collision_level3_deep_v7.json","batch_035_plus_collision_level3_10.md","Batch 035"),
("batch_036_ads_cit_deep_v7.json","batch_036_ads_cit_10.md","Batch 036"),
("batch_037_cit_cacc_ally_deep_v7.json","batch_037_cit_cacc_ally_10.md","Batch 037"),
("batch_038_ally_syf_dfs_deep_v7.json","batch_038_ally_syf_dfs_10.md","Batch 038"),
("batch_039_nexstar_sinclair_deep_v7.json","batch_039_nexstar_sinclair_10.md","Batch 039"),
("batch_040_gray_townsquare_deep_v7.json","batch_040_gray_townsquare_10.md","Batch 040"),
("batch_041_local_radio_audio_deep_v7.json","batch_041_local_radio_audio_10.md","Batch 041"),
("all_reviewed_v8_index.json","all_reviewed_v8.md.gz","V8 전체 DB"),)

@st.cache_data(show_spinner=False)
def _idea_catalog():
    catalog={}
    for json_name, markdown_name, batch_name in BATCH_SOURCES:
        jp=ROOT/'data'/'curated'/json_name; mp=ROOT/'analysis'/markdown_name
        if not jp.exists() or not mp.exists(): continue
        for pos,item in enumerate(json.loads(jp.read_text(encoding='utf-8')).get('postmortems',[])):
            iid=item['idea_id']
            if iid not in catalog: catalog[iid]={'batch_name':batch_name,'markdown_path':str(mp),'position':pos,'ticker':item.get('ticker','')}
    return catalog

def _heading_starts(text,pattern): return list(re.finditer(pattern,text,flags=re.MULTILINE))

def _expand_markdown_parts(markdown_path,text):
    m=re.search(r'<!-- batch_parts:\s*(.+?)\s*-->',text)
    if not m: return text
    chunks=[text]
    for name in (x.strip() for x in m.group(1).split('|')):
        if not name: continue
        p=markdown_path.parent/name
        if p.exists(): chunks.append(p.read_text(encoding='utf-8'))
    return '\n\n'.join(chunks)

def _extract_modern_company_report(text,date):
    ideas=_heading_starts(text,rf'^## \d+\. {re.escape(date)}(?:\s|—|-).*$')
    if not ideas:
        dated_h1=_heading_starts(text,rf'^# .+ — {re.escape(date)}(?:\s|—|-).*$')
        if dated_h1:
            selected=dated_h1[0]
            all_h1=_heading_starts(text,r'^# (?!#).+$')
            end=next((h.start() for h in all_h1 if h.start()>selected.start()),len(text))
            intro_end=all_h1[0].start() if all_h1 else selected.start()
            return '\n\n---\n\n'.join(x for x in (text[:intro_end].strip(),text[selected.start():end].strip()) if x)
        return None
    selected=ideas[0]; all_h1=_heading_starts(text,r'^# (?!#).+$')
    company_heads=[h for h in all_h1 if not re.match(r'^# (?:Batch |Part |배치 )',h.group(0))]
    start=end=None
    for h in company_heads:
        nxt=next((c for c in all_h1 if c.start()>h.start()),None); ns=nxt.start() if nxt else len(text)
        if h.start()<=selected.start()<ns: start,end=h.start(),ns; break
    if start is None: return None
    intro=text[:(company_heads[0].start() if company_heads else start)].strip(); company=text[start:end].strip()
    sm=re.search(r'^# 배치 공통.*$',text,re.MULTILINE); shared=text[sm.start():].strip() if sm else ''
    return '\n\n---\n\n'.join(x for x in (intro,company,shared) if x)

def _extract_legacy_report(text,position):
    parts=_heading_starts(text,r'^# Part [A-Z]\..*$'); return text.strip() if parts and position<len(parts) else None

def _extract_v8_company_report(text,idea_id):
    marker=re.search(rf'^<!-- idea:{re.escape(idea_id)} -->$',text,re.MULTILINE)
    if not marker: return None
    heads=_heading_starts(text,r'^# .+ — 기업과 투자 아이디어$')
    start=next((h.start() for h in reversed(heads) if h.start()<marker.start()),None)
    if start is None: return None
    end=next((h.start() for h in heads if h.start()>marker.start()),len(text)); intro_end=heads[0].start() if heads else start
    return '\n\n---\n\n'.join(x for x in (text[:intro_end].strip(),text[start:end].strip()) if x)

def _escape_dollar_math(markdown): return re.sub(r'(?<!\\)\$',r'\\$',markdown)

@st.cache_data(show_spinner=False)
def batch_report_for_idea(idea_id,date):
    item=_idea_catalog().get(idea_id)
    if not item: return None
    p=Path(item['markdown_path']); text=gzip.decompress(p.read_bytes()).decode('utf-8') if p.suffix=='.gz' else p.read_text(encoding='utf-8')
    text=_expand_markdown_parts(p,text)
    if item['batch_name']=='V8 전체 DB': report=_extract_v8_company_report(text,idea_id)
    elif int(item['batch_name'].split()[-1])>=8: report=_extract_modern_company_report(text,date)
    else: report=_extract_legacy_report(text,item['position'])
    return {'batch_name':item['batch_name'],'markdown':_escape_dollar_math(report)} if report else None

def render_batch_source_report(idea):
    r=batch_report_for_idea(str(idea.get('idea_id') or ''),str(idea.get('date') or '')[:10])
    if not r: return False
    st.caption(f"{r['batch_name']} 원문 레이아웃입니다. 선택한 기업의 모든 투자논지를 생략 없이 표시합니다."); st.markdown(r['markdown']); return True

def render_batch_popup_button(idea):
    item=_idea_catalog().get(str(idea.get('idea_id') or ''))
    if not item: return False
    p=Path(item['markdown_path'])
    if item['batch_name']=='V8 전체 DB': st.caption('이 항목은 아직 전용 Batch 파일이 없어 V8 통합 보고서에만 포함되어 있습니다.'); return False
    url='https://github.com/horea457/VIC-/blob/main/analysis/'+p.name
    cols=st.columns([1,3])
    with cols[0]: st.link_button('📄 GitHub에서 Batch 원문 열기',url,use_container_width=True)
    with cols[1]: st.caption(f"{item['batch_name']} · {p.name} · 상세분석은 GitHub의 Batch markdown 원문을 기준으로 봅니다.")
    return True