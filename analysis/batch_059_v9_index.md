# Batch 059 — Adient / ADP / American Dental Partners / Adaptec / Aduro / Alliance Data V9 Index

> **기준:** Batch 042 이후 V9 원칙 유지. 아이디어 1건 = canonical Markdown 1개.
> **Research as-of:** 2026-09-10.
> **Batch boundary:** Batch 058 마지막 ADNT 2020-08-17 이후, reviewed idea_id를 제외한 다음 10건.
> **핵심 데이터 품질:** raw direction correction 5건 + ADPT 2004 pair-security correction 1건. ADPT·ADRO는 corporate action이 복잡하여 simple price return 금지.

---

## 1. Canonical Idea Units

| # | 날짜 | Ticker | Raw 방향 | 실제 security / 방향 | Canonical | 최종 판정 |
|---:|---|---|---|---|---|---|
| 1 | 2022-05-19 | ADNT | **Short** | Common **Long** | [ADNT 2022](ideas/2022/2022-05-19_ADNT_long.md) | **운영회복 일부 성공 / FCF·주가 thesis 실패** |
| 2 | 2020-06-03 | ADP | **Short** | Common **Long** | [ADP 2020](ideas/2020/2020-06-03_ADP_long.md) | **강한 성공 — quality compounding** |
| 3 | 2008-03-26 | ADPI | **Short** | Common **Long** | [ADPI 2008](ideas/2008/2008-03-26_ADPI_long.md) | **강한 성공 — ~$10 → $19 cash takeout** |
| 4 | 2001-04-09 | ADPT | Long | Pre-spin common **Long** | [ADPT/Roxio 2001](ideas/2001/2001-04-09_ADPT_roxio_spin_long.md) | **corporate-action 강한 성공 / exact return 미복원** |
| 5 | 2004-06-15 | ADPT | Short | **Long ADPT / Short ELX pair** | [ADPT-ELX Pair](ideas/2004/2004-06-15_ADPT_ELX_pair.md) | **ADPT Long leg 실패 / pair IRR 미복원** |
| 6 | 2010-02-03 | ADPT | Long | Common **Long** | [ADPT 2010 Feb](ideas/2010/2010-02-03_ADPT_long.md) | **asset-sale catalyst 성공 / liquidation thesis 혼합** |
| 7 | 2010-08-17 | ADPT | **Short** | Common **Long** | [ADPT 2010 Aug](ideas/2010/2010-08-17_ADPT_long.md) | **static NAV 맞음 / realization route 혼합** |
| 8 | 2020-01-27 | ADRO | Long | Common **Long** | [ADRO 2020](ideas/2020/2020-01-27_ADRO_long.md) | **security outcome 강한 성공 / legacy pipeline thesis 혼합** |
| 9 | 2008-12-30 | ADS | **Short** | Common **Long** | [ADS 2008](ideas/2008/2008-12-30_ADS_long.md) | **매우 강한 성공** |
| 10 | 2010-04-15 | ADS | Short | Common **Short** | [ADS 2010 Short](ideas/2010/2010-04-15_ADS_short.md) | **매우 강한 실패** |

---

# PART A — Metadata / Security Audit

## 2. Direction corrections

raw Short → actual Long:
- ADNT 2022
- ADP 2020
- ADPI 2008
- ADPT 2010-08
- ADS 2008

raw/actual 일치:
- ADPT 2001 Long
- ADPT 2010-02 Long
- ADRO 2020 Long
- ADS 2010 Short

ADPT 2004는 단순 direction으로 저장하면 안 된다.

> **실제 포지션 = Long Adaptec / Short Emulex**

따라서 raw Short는 보존하되 overlay에서 pair security로 교정한다.

---

# PART B — ADNT 2022: “나쁜 회사의 trough trade”가 왜 충분하지 않았나

## 3. 2020 Long vs 2022 Long

2020 Adient Long의 강점은 실제 KPI 반전이었다.
- premium freight 급감
- launches 개선
- bad contracts 교체
- COVID 생존
- liquidity 확보

2022 writer는 오히려 회사를 구조적으로 낮게 평가했다.

> capital-inefficient widget maker이지만 supply-chain/commodity trough가 너무 심해 recovery trade가 가능하다.

### 원문 2022
- LTM adj EBITDA **$541m**
- FY22 FCF **-$56m**
- FY23 EBITDA **$970m**
- FY23 FCF **$500m**
- FY24~26 avg FCF **>$500m**
- sub-3x FY26E EBITDA

### 실제
FY23 EBITDA는 약 $938m으로 꽤 근접.

하지만 FY25:
- sales ~$14.5bn
- adjusted EBITDA **$881m**
- FCF 약 **$204m**

주가도 2025말 2022말보다 낮은 수준.

### 핵심
**EBITDA cycle recovery ≠ sustainable FCF recovery.**

fixed-price OEM contracts와 낮은 through-cycle ROIC가 multiple을 계속 제한했다.

---

# PART C — ADP 2020: 특별한 이벤트가 없어도 좋은 VIC 아이디어가 될 수 있다

## 4. ADP quality compounder

ADP는 이번 batch의 다른 event-driven ideas와 다르다.

핵심은:
- Employer Services client retention ~11년
- PEO ~6년
- 810k clients
- payroll reach 26m U.S. + 15m ex-U.S.
- 6,500 sellers
- 20k referral partners

이었다.

2020 bear case:
- Workday/Paycom/Paylocity 등 cloud-native 경쟁
- COVID employment shock

원문은 “UI가 오래됐다”와 **customer economics가 약하다**를 구분했다.

### Valuation
보수적 7Y EPS CAGR 약 6.7%에서:
- 25x endpoint → ~9% IRR
- 29x → ~11%

opening return framework는 **9~15% annualized**.

FY25 실제:
- revenue **$20.56bn**
- net earnings **$4.08bn**

### 교훈
> **Quality compounding에서 가장 중요한 것은 product fashion보다 mission criticality, retention, distribution, cross-sell이다.**

---

# PART D — ADPI 2008: Litigation uncertainty가 bounded 되는 순간

## 5. American Dental Partners

Park Dental verdict 이후:
- 52주 고점 $29.50
- post-verdict low $4.22
- VIC entry 약 $10

settlement 이후에도 stock은:
- 7.6x Cash EPS
- 5.3x EBITDA
- 4.2x normalized FCF

수준.

원문:
**50~100% upside / 12~18M**.

실제:
2011 JLL Partners가 **$19/share cash**에 acquisition.

$10 → $19 ≈ +90%.

### 중요한 차이
value는 맞았지만 timing은 12~18개월보다 길었다.

> **법적 tail이 유한해진 뒤에도 시장가격이 verdict 당시의 무한한 불확실성을 유지할 때 special-situation alpha가 생긴다.**

---

# PART E — ADAPTEC: 한 ticker가 네 개의 완전히 다른 투자로 변한다

## 6. ADPT 2001 — hidden software spin

@ $8.50.

- net cash $3.71/share
- Roxio sales $115m, +77%
- Roxio EBITDA $32.6m
- residual hardware stub ~$2.53/share

공식 spin:
**ADPT 1주 → Roxio 0.1646주**
2001-05-11 distribution.

### 판정
**corporate-action success.**

단, ADPT-only chart는 Roxio 분배가치를 누락하므로 exact return 금지.

---

## 7. ADPT 2004 — Right technology, wrong beneficiary

Pair:
- Long ADPT
- Short Emulex

Thesis:
iSCSI/storage-over-IP가 Fibre Channel economics를 압박.

ADPT valuation:
- EV $445m
- unlevered FCF $47m
- EV/FCF 9.4x
- value ~$7.90

하지만 실제 ADPT:
- FY05 revenue $402.5m
- FY07 $255.2m
- FY05~06 operating loss 합계 ~$188.4m

즉 iSCSI trend와 별개로 **Adaptec이 value를 포착하지 못했다.**

### 핵심
> **Technology thesis와 beneficiary thesis는 별도다.**

---

## 8. ADPT 2010-02 — operating company에서 asset shell로 재정의

@ $3.07.

- cash ~$380m
- market cap ~$370m
- NOL ~$150m
- book ~$3.40/share
- target ~$3.90
- Steel Partners control
- Blackstone asset-sale process

실제:
legacy business → **PMC-Sierra $34.3m sale**.

즉 asset-sale catalyst는 정확히 발생.

그런데 현금은 순수 liquidation으로 가지 않고 Steel Excel의 새 사업 seed capital로 바뀌었다.

---

## 9. ADPT 2010-08 — negative EV 이후에는 capital allocation 투자

@ $2.80.

- cash ~$394m
- market cap ~$335m
- EV -$59m
- land ~$20m
- DTA ~$45m after haircut
- value ~$3.75

수학은 맞았다.

하지만 회사는 이후:
- youth sports
- oilfield services

등 새로운 businesses에 capital을 배치.

### 2010-02 → 2010-08의 thesis 변화

**asset sale → cash shell → capital allocator**

따라서 같은 ticker라도 완전히 다른 투자다.

---

# PART F — ADRO 2020: negative-EV biotech의 가치가 어디서 나왔나

## 10. Aduro

@ $1.50.

- cash **$235m / $2.93 per share**
- market cap $121m
- debt 0
- materially negative EV

legacy pipeline:
- BION-1301
- ADU-S100
- partnered Merck/Lilly/Novartis assets
- potential milestones $1.5bn+

핵심은 pipeline에 높은 값을 준 것이 아니라:
**cash의 약 50% 가격에 options를 받는다**는 것.

### 실제 realization
2020:
Aduro + private Chinook reverse merger.

- 1-for-5 reverse split
- prior Aduro holders 약 **39.9%** combined ownership
- legacy CVR

2023:
Novartis가 Chinook을:
**$40/share cash + up to $4 CVR**
에 인수.

### 판정
security result는 강한 성공.

하지만 최종 큰 가치의 상당부분은 **새 Chinook assets**에서 나왔다.

> **Post-merger success를 original Aduro science의 성공으로 재작성하면 안 된다.**

---

# PART G — Alliance Data: 같은 회사에서 Long과 Short가 정반대 결과

## 11. ADS 2008 Long

시장:
“consumer credit company.”

writer:
“credit는 한 segment일 뿐이고 AIR MILES/Epsilon/private-label services가 별도 valuable cash engines.”

당시:
- Cash EPS $4.40
- 10.3x 2008E / 8.8x 2009E
- 2009 FCF yield ~10%
- target **$67**

credit charge-offs는 10.5%까지 stress한 후 recovery를 모델링.

실제:
- 2009 ~$64.6
- 2010 ~$71
- 2011 ~$104
- 2012 ~$145
- 2013 ~$263

**강한 성공.**

---

## 12. ADS 2010 Short

Short는:
- nonprime credit
- CARD Act
- SFAS 166/167 consolidation
- AIR MILES accounting
- Cash EPS add-backs
- governance

를 집중 분석.

writer는 SFAS consolidation 이후 adjusted EV 약 **$6.69bn**, EV/EBITDA 약 **13x**, stock downside >50%를 주장.

실제는 반대.

2010~13 주가가 몇 배 상승.

### 왜 실패했나

가장 중요한 오류:
**accounting recognition ≠ new economic obligation.**

SFAS가 securitized receivables를 balance sheet에 올린다고 underlying economic exposure가 갑자기 새로 생긴 것은 아니었다.

또 credit-loss normalization과 non-credit businesses를 과소평가.

---

## 13. ADS 2008 Long vs 2010 Short — B59 최고의 forensic 비교

| 항목 | 2008 Long | 2010 Short |
|---|---|---|
| Credit | severe stress 후 recovery | prolonged structural impairment |
| Non-credit | valuable separate cash engines | valuation skepticism |
| Accounting | secondary | central bear thesis |
| Framework | SOTP | adjusted consolidated EV |
| Outcome | **매우 강한 성공** | **매우 강한 실패** |

둘 다 credit/accounting facts를 봤다.

차이는 **어떤 사실을 economic value driver로 두었는가**였다.

### 핵심 교훈
> **Forensic red flag는 현금·자본·유동성으로 연결되지 않으면 Short catalyst가 아니다.**

---

# PART H — Cross-Batch Framework

## 14. B59의 여섯 가지 투자유형

1. **ADNT:** cyclical recovery
2. **ADP:** quality compounder
3. **ADPI:** litigation special situation
4. **ADPT:** spin / pair / asset shell / allocator
5. **ADRO:** negative-EV biotech / reverse merger
6. **ADS:** conglomerate SOTP vs forensic Short

서로 완전히 다른 valuation language가 필요하다.

- ADNT → normalized FCF / contract economics
- ADP → long-run IRR / retention
- ADPI → legal payoff tree
- ADPT → SOTP / corporate actions / controller
- ADRO → cash burn / dilution / CVR
- ADS → segment SOTP / credit stress / accounting-to-cash bridge

---

## 15. 정보의 질 순서

낮은 것부터:
1. technology trend
2. headline P/E
3. accounting red flag
4. management target
5. segment economics
6. customer retention / unit economics
7. legal settlement
8. actual asset sale / spin ratio
9. cash distribution / takeout
10. observed post-stress FCF

B59에서도 **실제 현금·계약·corporate action에 가까운 증거**일수록 thesis가 강했다.

---

## 16. Batch 059 재사용 체크리스트 22개

1. raw Long/Short는 원문으로 확인한다.
2. pair trade는 별도 security type으로 저장한다.
3. spin은 모든 distributed securities를 복원한다.
4. technology trend와 beneficiary economics를 분리한다.
5. cash-rich tech는 burn rate를 본다.
6. net-net은 controller의 capital allocation을 본다.
7. asset-sale 뒤 thesis를 새로 작성한다.
8. NOL value는 실제 활용가능성을 discount한다.
9. reverse merger에서 legacy ownership dilution을 계산한다.
10. CVR을 누락하지 않는다.
11. negative-EV biotech의 cash는 liquidation value가 아니라 acquisition currency일 수 있다.
12. litigation settlement는 liability range를 bounded 하는지 본다.
13. target value와 target timing을 별도 판정한다.
14. quality compounder는 terminal target보다 IRR을 본다.
15. technology-debt bear thesis는 retention/churn으로 검증한다.
16. PEO passthrough처럼 경제적 의미가 다른 revenue를 분리한다.
17. conglomerate는 segment별 multiple을 쓴다.
18. credit stress를 whole-company identity로 과대확장하지 않는다.
19. accounting consolidation과 economic leverage를 구분한다.
20. forensic red flag를 cumulative cash consequence로 연결한다.
21. cyclical EBITDA recovery와 FCF recovery를 분리한다.
22. corporate-action 오염이 있으면 nominal price return을 금지한다.

---

## 17. Batch 059 핵심 한 줄

> **좋은 투자분석은 ‘무슨 일이 일어날까’를 맞히는 것보다 어떤 자산·계약·고객·현금흐름이 실제 주주가치로 귀속되는지를 정확히 연결하는 일이다. Adaptec의 iSCSI와 ADS의 회계 red flag처럼 사실을 맞혀도 가치귀속 경로를 틀리면 투자결론은 반대가 될 수 있다.**

---

## 18. 앱 / DB 반영

- Wrapper: `analysis/batch_059_adnt_adp_adpi_adpt_adro_ads_10.md`
- Overlay: `data/curated/batch_059_adnt_adp_adpi_adpt_adro_ads_deep_v7.json`
- Canonical source of truth: 위 10개 Markdown.
