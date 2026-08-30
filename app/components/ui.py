import streamlit as st

CSS = """
<style>
.block-container {padding-top: 1.4rem; padding-bottom: 3rem; max-width: 1500px;}
[data-testid="stSidebar"] {border-right: 1px solid rgba(128,128,128,.18);}
.vic-eyebrow {font-size:.78rem; letter-spacing:.08em; text-transform:uppercase; opacity:.62; margin-bottom:.2rem;}
.vic-title {font-size:2.05rem; font-weight:760; line-height:1.14; margin:0 0 .35rem 0;}
.vic-subtitle {font-size:.98rem; opacity:.68; max-width:960px; line-height:1.55; margin-bottom:1.25rem;}
.vic-pill {display:inline-block; border:1px solid rgba(128,128,128,.25); border-radius:999px; padding:.14rem .5rem; margin:.08rem .12rem .08rem 0; font-size:.77rem;}
hr {margin:1.15rem 0 1rem 0 !important;}
</style>
"""

# Pattern hub 추가 스타일
CSS_PATTERN = """
<style>
.pattern-card {border:1px solid rgba(128,128,128,.22); border-radius:14px; padding:14px 15px 12px 15px; min-height:172px; margin-bottom:8px; background:rgba(128,128,128,.035);}
.pattern-kicker {font-size:.72rem; text-transform:uppercase; letter-spacing:.06em; opacity:.58; margin-bottom:.35rem;}
.pattern-name {font-size:1.03rem; font-weight:720; line-height:1.28; margin-bottom:.38rem;}
.pattern-meta {font-size:.76rem; opacity:.66; margin-bottom:.52rem;}
.pattern-desc {font-size:.83rem; opacity:.78; line-height:1.45;}
</style>
"""


def apply_css():
    st.markdown(CSS, unsafe_allow_html=True)
    if 'CSS_PATTERN' in globals():
        st.markdown(CSS_PATTERN, unsafe_allow_html=True)

def page_header(kicker, title, subtitle):
    st.markdown(
        f'<div class="vic-eyebrow">{kicker}</div>'
        f'<div class="vic-title">{title}</div>'
        f'<div class="vic-subtitle">{subtitle}</div>',
        unsafe_allow_html=True,
    )

def pills(items):
    if not items:
        return
    html = ''.join(f'<span class="vic-pill">{x}</span>' for x in items)
    st.markdown(html, unsafe_allow_html=True)

def empty_analysis():
    st.info('이 항목은 아직 정밀 검증 전입니다. 자동 1차 태그와 원본 메타데이터는 탐색용이며, 성공·실패 최종 판정으로 사용하지 않습니다.')
