# Batch 045 — PLUS / Brink's — V9 Index

> 기준: Batch 003 V9 canonical format. 공통 기업 설명은 여기에서 한 번만 제공하고, 각 투자시점은 독립 Idea Unit으로 분리한다.

## 0. 이번 배치의 핵심 교정

이 배치는 SQL-derived `source_true_unreviewed`에서 Batch 043·044에서 이미 사용한 idea_id를 제외한 다음 10건을 선택했다. 결과는 **남은 PLUS 4건 + Brink's(BCO) 6건**이다.

가장 중요한 데이터 이슈는 두 가지다.

1. `PLUS` ticker collision: 2008·2010은 **ePlus Inc.**지만 2019·2021은 실제로 **Plus500 Ltd.**다. SQL의 company lookup이 모두 `ePLUS`로 붙어 있어 entity를 반드시 분리해야 한다.
2. SQL direction flag는 신뢰하지 않는다. ePlus 2010과 Plus500 2019는 raw `Short`지만 원문은 명백한 **Long**이다. Brink's 6건도 raw flag가 모두 Short라 원문 방향을 별도 검증 대상으로 둔다.

## 1. 공통 기업 설명

### ePlus Inc.

ePlus는 미국 기업·공공기관에 서버, 네트워크, 보안, 데이터센터, 클라우드 인프라를 설계·조달·구축하는 **value-added reseller(VAR) + IT services + financing** 사업자다. 단순 하드웨어 유통처럼 보이지만 실제 경제성은 `제품 매출 × 낮은 gross margin + 서비스 gross profit + 금융/리스 수익 - 영업비용 - 운전자본 비용`으로 결정된다. 장비 리스에는 non-recourse financing이 많아 회계상 gross debt를 모두 기업가치 계산에 넣으면 실질 leverage를 과대평가할 수 있다.

### Plus500 Ltd.

Plus500은 온라인 CFD/파생상품 중개 플랫폼이다. 고객 수, ARPU, customer acquisition cost, churn, 규제별 leverage cap, market P&L이 핵심이다. 경제성은 대략 `active customers × ARPU - acquisition/marketing - platform/compliance - market P&L 변동`이다. 2018년 이후 ESMA leverage 제한이 유럽 사업의 구조를 바꿨고, 2019·2021 아이디어는 바로 이 규제 후 earnings power를 어떻게 볼 것인가가 핵심이다.

### The Brink's Company

Brink's는 현금·귀중품의 보안 운송, ATM replenishment, cash processing, vault outsourcing, smart safe, 국제 valuables logistics를 제공한다. 고객은 은행·리테일러·중앙은행·정부기관·보석/귀금속 업체다. 노선 밀도가 중요한 route-based logistics라서 동일 지역에서 더 많은 stop을 한 차량·인력·시설에 얹을수록 단위비용이 낮아진다.

핵심 경제성은 `route density × price/mix → revenue → labor + fleet + facility + insurance/security cost → operating profit → capex + restructuring + pension/interest → FCF`다. 따라서 단순 매출 성장보다 **organic growth, operating margin, route density, cash conversion, pension/legacy liabilities, acquisition multiple과 integration**을 같이 봐야 한다.

## 2. Idea Units

| # | 날짜 | 실제 entity | 연구 방향 | 핵심 질문 | 파일 |
|---:|---|---|---|---|---|
| 1 | 2008-06-09 | ePlus | Long | 재무 정상화와 NASDAQ 재상장이 value realization을 만들었나 | [2008 ePlus](ideas/2008/2008-06-09_PLUS_eplus_long.md) |
| 2 | 2010-02-22 | ePlus | **Long — raw Short 교정** | non-recourse debt 조정 후 실질 EV가 얼마나 쌌나 | [2010 ePlus](ideas/2010/2010-02-22_PLUS_eplus_long.md) |
| 3 | 2019-08-26 | **Plus500** | **Long — raw Short/entity 교정** | ESMA 후 earnings power가 실제로 안정됐나 | [2019 Plus500](ideas/2019/2019-08-26_PLUS500_long.md) |
| 4 | 2021-09-03 | **Plus500** | Long — entity 교정 | 코로나 peak 이후에도 base earnings와 신규 옵션이 남았나 | [2021 Plus500](ideas/2021/2021-09-03_PLUS500_long.md) |
| 5 | 2007-02-12 | Brink's | 원문 방향 재검증 | activism/SOTP가 common equity에 실제 귀속됐나 | [2007 Brink's](ideas/2007/2007-02-12_BCO.md) |
| 6 | 2010-06-13 | Brink's | 원문 방향 재검증 | pure-play cash logistics 정상화가 가능한가 | [2010 Brink's](ideas/2010/2010-06-13_BCO.md) |
| 7 | 2012-11-28 | Brink's | 원문 방향 재검증 | 저마진·legacy liability를 감안한 정상화 가치 | [2012 Brink's](ideas/2012/2012-11-28_BCO.md) |
| 8 | 2014-02-07 | Brink's | 원문 방향 재검증 | peer margin gap이 실제 self-help opportunity였나 | [2014 Brink's](ideas/2014/2014-02-07_BCO.md) |
| 9 | 2017-05-12 | Brink's | 원문 방향 재검증 | Pertz 체제의 margin program/roll-up이 equity FCF를 키웠나 | [2017 Brink's](ideas/2017/2017-05-12_BCO.md) |
| 10 | 2018-05-17 | Brink's | 원문 방향 재검증 | APG/CTG/IDS와 M&A가 과도한 기대였나 | [2018 Brink's](ideas/2018/2018-05-17_BCO.md) |

## 3. 이 배치에서 반복해서 볼 질문

- **Entity가 맞는가?** ticker만으로 회사를 매칭하지 않는다.
- **Debt가 진짜 corporate recourse인가?** ePlus처럼 lease-backed non-recourse debt가 섞이면 EV가 왜곡된다.
- **규제 충격 후 숫자는 새 정상인가, 일시적 반등인가?** Plus500은 ESMA 전후 cohort economics를 분리해야 한다.
- **route density가 실제 margin으로 전환되는가?** Brink's는 매출 성장보다 local density와 cost discipline이 중요하다.
- **SOTP/asset value가 common equity에 언제 귀속되는가?** activism, spin-off, asset sale은 경로와 시간이 핵심이다.
- **self-help와 multiple expansion을 중복 계산하지 않았는가?** margin improvement가 이미 주가에 반영됐는지 분리한다.

## 4. Source packet

- `data/curated/batch_045_source_packet.json`
- `data/source_batch045/` — ePlus / Plus500 원문 4건 보존
- Brink's SQL metadata idea_ids: `d65501e4...`, `d3cab447...`, `bda1795d...`, `4ac6396a...`, `88c3b3a4...`, `16123d39...`

## 5. Batch-level synthesis

이번 배치의 공통 주제는 **headline multiple보다 accounting/entity/claim 구조를 먼저 고쳐야 한다**는 것이다. ePlus에서는 non-recourse debt를 corporate leverage로 잘못 읽으면 EV가 틀리고, Plus500에서는 같은 ticker 때문에 회사 자체가 바뀌며, Brink's에서는 route-based operating leverage와 legacy liabilities를 분리하지 않으면 SOTP 또는 EBITDA multiple이 과대평가될 수 있다.

따라서 최종 판정은 항상 `Business thesis / Valuation thesis / Catalyst & timing / Security selection / Actual investment outcome`을 따로 기록한다.
