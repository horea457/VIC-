# Batch 007 — Chesapeake Energy Full History V9 Index

> 기존 `analysis/batch_007_chesapeake_full_history.md`와 `analysis/batch_007_chesapeake_v2_deep.md`는 archive/reference로 유지한다.  
> V9에서는 **VIC 투자 아이디어 1건 = Markdown 1개**를 canonical report로 사용한다.

## Canonical idea files

| VIC 게시일 | Security / 방향 | 파일 | 핵심 판정 |
|---|---|---|---|
| 2001-04-05 | Common Long | [2001 CHK Long](ideas/2001/2001-04-05_CHK_long.md) | 저배수 gas cycle Long으로 성공 |
| 2006-06-24 | Common Long | [2006 CHK Long](ideas/2006/2006-06-24_CHK_long.md) | 목표가 성공, asset NAV→equity bridge는 부분 실패 |
| 2008-10-12 | Common Long | [2008 CHK Long](ideas/2008/2008-10-12_CHK_long.md) | forced-selling 반등은 성공, takeout·governance는 실패 |
| 2009-11-15 | Common Short | [2009 CHK Short](ideas/2009/2009-11-15_CHK_short.md) | 장기 기업논지 적중, 2년 timing/catalyst 실패 |
| 2011-02-08 | Common Long | [2011 Feb CHK Long](ideas/2011/2011-02-08_CHK_long.md) | 25/25·JV·governance 촉매 발생에도 old equity 0 |
| 2011-10-07 | Common Long | [2011 Oct CHK NAV Long](ideas/2011/2011-10-07_CHK_long.md) | $68.43 NAV 논리의 waterfall 오류, 치명적 실패 |
| 2015-12-11 | 6.5% 2017 Senior Note Long | [2015 CHK 2017 Note Long](ideas/2015/2015-12-11_CHK_2017_note_long.md) | $70 → par 회수, 매우 성공 |
| 2016-06-13 | 2020 Senior Note Long | [2016 CHK 2020 Note Long](ideas/2016/2016-06-13_CHK_2020_note_long.md) | 만기 전 Chapter 11, 실패 |
| 2021-02-17 | Post-Reorg Common Long | [2021 CHK Post-Reorg Long](ideas/2021/2021-02-17_CHK_post_reorg_long.md) | 1Y +62%, 2Y +115.5%, 매우 성공 |

---

# Batch 007의 핵심

Chesapeake를 하나의 회사 역사로만 보면 투자결과를 설명하기 어렵다.

실제로 중요한 것은:

**Asset quality  
× Commodity price  
× Maintenance/Growth Capex  
× Capital structure  
× Security seniority  
× Maturity  
× Entry valuation**

이다.

같은 지하자산이어도 어떤 증권을 언제 샀는지에 따라 결과가 완전히 달랐다.

---

# 1. Common Equity Long의 반복 오류

## 1.1 Reserve / Acreage value를 common equity value로 바로 연결

E&P 자산가치는 다음 waterfall을 통과해야 한다.

**Gross asset value  
- future development capex  
- net debt  
- secured claims  
- preferred  
- VPP / production obligations  
- transport commitments  
- corporate G&A PV  
- taxes / transaction costs  
- dilution  
= common equity value**

2006·2011 Long은 앞단 asset appraisal은 강했지만 뒤 waterfall이 약했다.

## 1.2 생산량 성장을 주당가치 성장으로 오해

생산량이 늘어도:

- drilling/completion capex
- lease retention drilling
- transport commitments
- financing cost

가 더 커지면 FCF/share는 늘지 않는다.

## 1.3 JV와 drilling carry를 cash처럼 해석

Drilling carry는 특정 개발비를 partner가 대신 내주는 구조다.

**Restricted development funding ≠ unrestricted cash**

이다.

---

# 2. 2009 Short가 가장 교육적인 이유

2009 Short는 실제로 많은 것을 맞혔다.

- shale 공급 증가
- 낮은 gas price
- HBP drilling burden
- 구조적 FCF 적자
- 반복 외부자본 조달
- governance 문제

그리고 결국 CHK는 2020년에 Chapter 11을 신청했다.

그런데도 **2년 Short로는 실패**했다.

왜냐하면:

- JV
- VPP
- asset sales
- equity issuance
- refinancing

이 장기 주주가치를 훼손하면서도 **단기 survival runway를 계속 늘렸기 때문**이다.

### 핵심 교훈

> **기업의 경제성이 나쁘다는 것과 equity가 곧 무너진다는 것은 다르다.**

Short에서는 반드시:

**Cash burn  
vs  
Available financing / monetizable assets**

를 시간축으로 계산해야 한다.

---

# 3. VPP를 반드시 별도 항목으로 보는 이유

VPP는:

**미래 일정 생산량을 넘기고 오늘 현금을 받는 거래**

다.

따라서:

**현재 liquidity +  
미래 production / cash flow -**

로 기록해야 한다.

단기에는:
- debt maturity 대응
- drilling funding

에 도움이 된다.

장기에는:
- future EBITDA
- collateral
- shareholder residual

을 줄일 수 있다.

이 때문에 VPP는 **Long에는 가치훼손 가능성**, **Short에는 오히려 catalyst delay 가능성**을 동시에 가진다.

---

# 4. 2015 vs 2016 Credit — 회사가 아니라 시간을 샀다

| 항목 | 2015 2017채 | 2016 2020채 |
|---|---:|---:|
| 매입가 | 약 $70 | 약 $75 |
| 원문 YTM | 약 44% | 약 15% |
| 필요한 생존기간 | 약 20개월 | 약 4년 |
| 결과 | par 회수 | Chapter 11 |
| 핵심 | short runway | duration risk |

2015채는 principal 기준:

**$70 → $100 = +42.9%**

에 coupon까지 받았다.

반면 2020채는 par을 현금으로 회수하지 못했다.

이 비교는 distressed credit에서 **maturity 자체가 핵심 투자변수**임을 보여준다.

---

# 5. 2011 Old Equity vs 2021 New Equity

## 2011 Old Equity

- 좋은 acreage
- 거대한 gross NAV
- JV
- liquids 전환
- 행동주의

가 있었지만:

- debt
- preferred
- transport
- capex
- VPP
- governance
- dilution

도 같이 있었다.

최종 old common recovery: **0**

## 2021 Post-Reorg Equity

Chapter 11 이후:
- old common 제거
- 상당한 debt 제거
- cost base 감소
- 새 equity 발행

후 약 $40에서 매수.

실제:
- 1년 **+62.0%**
- 2년 **+115.5%**
- 2년 가격 CAGR 약 **46.8%**

### 핵심 교훈

> **Same rocks, different claims.**

같은 지하자산이더라도 누가 그 현금흐름을 먼저 가져가느냐가 바뀌면 전혀 다른 주식이다.

---

# 6. CHK형 E&P에서 반드시 볼 항목

## Operations
1. Production by commodity
2. Decline rate
3. Maintenance drilling
4. Cash cost / boe
5. Realized price after hedges

## Capital intensity
6. Maintenance capex
7. Growth capex
8. HBP drilling requirement
9. Future development cost

## Capital structure
10. Net debt
11. Secured vs unsecured debt
12. Preferred
13. VPP
14. Transport minimum-volume commitments
15. Lease obligations
16. Fully diluted shares

## Liquidity / Survival
17. Cash
18. Revolver / ABL
19. Borrowing-base redetermination
20. Asset-sale inventory
21. Maturity ladder
22. Interest burden

## Equity value
23. FCF after maintenance capex
24. FCF/share
25. Debt-adjusted NAV
26. Commodity-normalized NAV
27. Reverse DCF / implied gas price

---

# 7. Batch 007에서 추출되는 가장 중요한 원칙

### 원칙 1
**좋은 지하자산 ≠ 좋은 보통주**

### 원칙 2
**좋은 asset sale ≠ 모든 asset sale**
부채보다 더 큰 미래 FCF를 팔면 장기 가치는 줄 수 있다.

### 원칙 3
**JV carry ≠ cash**

### 원칙 4
**VPP는 미래현금흐름의 선취**

### 원칙 5
**Short는 terminal insolvency가 아니라 financing clock을 산다**

### 원칙 6
**Distressed credit은 issuer가 아니라 maturity별로 분석한다**

### 원칙 7
**파산 후에는 같은 ticker history를 버리고 새 capital structure를 처음부터 분석한다**

---

# 추가 보강 항목

- 2001·2006·2008·2009·2011 common stock의 exact daily entry/exit series
- 각 common idea의 MFE / MAE
- 2009 Short의 목표기간 실제 short return
- 2015 note의 exact coupon-date / accrued-interest 반영 realized IRR
- 2016 note의 reorganization security 실제 recovery value
- transport minimum-volume commitments의 연도별 PV
- VPP 누적 proceeds와 sold-production value bridge
- annual CFO / capex / asset-sale / debt issuance waterfall
- commodity-normalized FCF/share 시계열

