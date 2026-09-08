# Nexstar Media Group (NXST) — 2016-01-29 VIC Pair/Event

> **Idea unit:** 이 게시일의 Long 1 MEG + Short 0.1249 NXST + CVR 한 건만 분석한다. 같은 회사의 다른 날짜는 별도 파일이다.  
> **평가기준일:** 2024-01-31. **분석·문서 갱신일:** 2026-09-08. 기준일 이후 사실은 현재 상태 참고로만 사용한다.

> **Direction audit:** SQL raw 방향은 `Short`이지만 원문 추천·payoff·보유공시로 재구성한 실제 방향은 **Pair/Event**이다. 원 SQL 값은 삭제하지 않고 감사추적용으로 보존한다.

---

## 0. Idea Snapshot

| 항목 | 내용 |
|---|---|
| 회사 / Ticker | Nexstar Media Group / NXST |
| VIC 게시일 / 작성자 | 2016-01-29 / jdr907 |
| 증권 / 실제 방향 | Long 1 MEG + Short 0.1249 NXST + CVR / Pair/Event |
| 원 SQL 방향 | Short |
| 기준 진입가 | 고정대가 대비 spread 약 0; CVR 내재가 약 $0.85 |
| 원문 목표 / 기대기간 | CVR $2~3, 최대 $4; 약 20~30% ROI / 거래·경매대금 지급 약 10~12개월 |
| 종합 판정 | **구조 성공·CVR 가치 과대** |

> **결론:** 주식대가를 정확히 헤지해 CVR만 사는 구조는 성공했고 경매대금도 발생했다. 그러나 gross spectrum proceeds를 distributable CVR 가치로 바꾸는 공제·세금·지급단위 분석이 약해 $2~3 기대는 높았다.

---

## 1. 회사는 정확히 무엇을 하는가

Nexstar Media Group은 미국 각 지역의 지상파 TV 방송국을 소유·운영하고, ABC·CBS·NBC·FOX·The CW 같은 전국 네트워크 프로그램과 자체 지역뉴스를 편성해 배포하는 방송사다. 2000년대의 Nexstar는 중소도시 방송국 묶음에 가까웠지만, Media General과 Tribune을 인수하면서 전국 최대 규모의 지역방송 플랫폼으로 변했다. 이후 The CW 지분, NewsNation, The Hill, BestReviews 같은 전국·디지털 자산도 보유했다.

고객은 둘이다. 광고주는 지역 시청자에게 도달하기 위해 광고비를 내고, 케이블·위성·가상 유료방송 사업자는 Nexstar 방송 신호를 상품에 넣기 위해 distribution 또는 retransmission fee를 낸다. Nexstar는 이 총 retrans 중 일부를 제휴 전국 네트워크에 reverse retrans 또는 affiliation fee로 지급한다. 따라서 중요한 것은 총 distribution revenue가 아니라 `가입자 수 × 가입자당 단가 - 네트워크 지급액`인 net retrans profit이다.

지역뉴스는 제작비가 큰 고정비 사업이지만, 이미 만들어진 뉴스·송출설비 위에 정치광고나 높은 단가의 retrans가 붙으면 증분마진이 높다. 반대로 core 광고가 급락해도 뉴스룸 비용을 즉시 줄이기 어렵다. M&A는 본사·영업·뉴스·송출 중복비용을 제거하고 인수 방송국의 retrans 단가를 매수자 수준으로 올릴 수 있어 강력한 레버가 된다. 그러나 거래를 부채로 사기 때문에 EBITDA가 예상보다 작거나 cord-cutting이 빨라지면 손실은 보통주에 증폭된다.

### 가치사슬과 현금의 이동

시청자·지역콘텐츠 → 방송국/뉴스룸 → 지상파·MVPD·vMVPD 배포 → 시청률/가입자 도달 → 광고·retrans 수익 → 네트워크 fee·제작비·이자 차감 → FCF

### 반드시 봐야 할 KPI

동일 방송국 core 광고, 정치광고, distribution revenue, reverse retrans/affiliation expense, net retrans profit, 유료방송 가입자 감소율, 디지털 매출·마진, pro forma EBITDA, FCF, 순레버리지, 주식수와 평균 매입가격

---

## 2. 당시 시장상황과 가격에 들어 있던 기대

Nexstar의 Media General 인수대가는 MEG 1주당 현금 $10.55, NXST 0.1249주, FCC incentive auction proceeds에 연동된 CVR 1개였다. 고정대가와 MEG 주가의 spread가 거의 없어 원문은 NXST 0.1249주를 short해 시장·합병회사 위험을 제거하고 CVR을 약 $0.85 내재가에 취득하는 spectrum trade를 제안했다.

### Reverse expectations

시장가격은 auction clearing·station surrender가 불확실하고, 거래종결·지급까지 시간이 걸리며, spectrum gross value에서 세금·비용·계약공제가 빠진다고 봤다. 수익은 NXST 방향이 아니라 CVR당 실제 현금분배가 $0.85를 얼마나 넘는지에 달렸다.

---

## 3. 원 투자논지를 구성한 6개 핵심 Claim

### C1. 0.1249 NXST short가 합병주가 위험을 제거한다 — 성공

**원문 주장**  
MEG 1주당 받을 NXST 0.1249주를 short하면 고정 cash와 CVR만 남는다.

**T0에서 확인 가능했던 근거**  
확정 exchange ratio 0.1249.

**경제적 전달경로**  
주식교환분을 헤지해 고정대가를 잠그고 CVR만 보유하면 경매 spectrum proceeds라는 특정 사건의 확률가중 payoff를 분리할 수 있다.

**숨은 가정**  
헤지비율·차입비용·배당조정이 정확하고, CVR 계약상 공제·세금·지급시기가 분석과 일치한다는 가정이다.

**사전 반증조건**  
경매가 실패하거나 순수취액이 시장내재가보다 낮고 지급이 크게 지연되면 반증한다.

**실제 결과**  
거래가 종결돼 주식대가 hedge 구조가 작동했다.

**정량 gap과 판정 이유**  
기본 hedge ratio 적중; borrow·배당은 별도. 계약변경·배당조정 조항까지 반영해야 완전 hedge다.

**재사용 교훈**  
CVR은 headline asset value가 아니라 계약서상 distributable proceeds와 지급단위 수로 계산한다.
### C2. 시장내재 CVR은 약 $0.85다 — 부분 성공

**원문 주장**  
고정대가에 6% deal discount를 적용하면 MEG 가격 속 CVR은 약 $0.85다.

**T0에서 확인 가능했던 근거**  
cash $10.55 + 0.1249 NXST와 당시 MEG 가격.

**경제적 전달경로**  
주식교환분을 헤지해 고정대가를 잠그고 CVR만 보유하면 경매 spectrum proceeds라는 특정 사건의 확률가중 payoff를 분리할 수 있다.

**숨은 가정**  
헤지비율·차입비용·배당조정이 정확하고, CVR 계약상 공제·세금·지급시기가 분석과 일치한다는 가정이다.

**사전 반증조건**  
경매가 실패하거나 순수취액이 시장내재가보다 낮고 지급이 크게 지연되면 반증한다.

**실제 결과**  
CVR에 실제 지급가치가 생겼다.

**정량 gap과 판정 이유**  
0보다 컸으나 정확 per-CVR 실현값은 자료제약. 시장내재가 계산은 유용하지만 확정 cash-flow table이 필요하다.

**재사용 교훈**  
CVR은 headline asset value가 아니라 계약서상 distributable proceeds와 지급단위 수로 계산한다.
### C3. CVR은 $2~3, 최대 $4다 — 부분 실패

**원문 주장**  
고가 opening bid station과 낮은 방송가치를 이용하면 CVR당 $2~3이 보수적이다.

**T0에서 확인 가능했던 근거**  
KRON opening bid $395m 등 station-level 자료.

**경제적 전달경로**  
영업에 필요하지 않은 주파수를 FCC 경매에 팔거나 채널 공유하면 EBITDA 훼손을 제한하면서 일회성 현금을 주주에게 이전할 수 있다.

**숨은 가정**  
opening bid가 clearing price와 유사하고, 간섭·채널공유·세금·규제공제 후에도 대부분의 가치가 남는다는 가정이다.

**사전 반증조건**  
실제 gross proceeds가 추정의 절반 미만이거나 운영손실·세금으로 주주귀속액이 급감하면 반증한다.

**실제 결과**  
gross proceeds $478.6m, 초기 CVR 지급액 $258.6m로 headline보다 큰 haircut이 발생했다.

**정량 gap과 판정 이유**  
경매 성공이나 $2~3 base는 과대. opening bid를 clearing·net distribution과 혼동했다.

**재사용 교훈**  
스펙트럼 옵션은 opening bid가 아니라 실제 경매수요와 세후 분배가능액에 큰 haircut을 적용한다.
### C4. FCC 경매는 실행된다 — 성공

**원문 주장**  
FCC incentive auction만 실행되면 별도 spectrum-use 승인보다 규제위험이 낮다.

**T0에서 확인 가능했던 근거**  
FCC의 reverse/forward auction 공식 구조.

**경제적 전달경로**  
영업에 필요하지 않은 주파수를 FCC 경매에 팔거나 채널 공유하면 EBITDA 훼손을 제한하면서 일회성 현금을 주주에게 이전할 수 있다.

**숨은 가정**  
opening bid가 clearing price와 유사하고, 간섭·채널공유·세금·규제공제 후에도 대부분의 가치가 남는다는 가정이다.

**사전 반증조건**  
실제 gross proceeds가 추정의 절반 미만이거나 운영손실·세금으로 주주귀속액이 급감하면 반증한다.

**실제 결과**  
경매가 실행되고 Nexstar는 상당한 proceeds를 받았다.

**정량 gap과 판정 이유**  
binary execution 방향 적중. auction demand·clearing target라는 가격위험은 남았다.

**재사용 교훈**  
스펙트럼 옵션은 opening bid가 아니라 실제 경매수요와 세후 분배가능액에 큰 haircut을 적용한다.
### C5. CVR이 0이어도 downside는 0에 가깝다 — 부분 실패

**원문 주장**  
고정대가 spread가 0이므로 CVR이 무가치해도 nominal 손실이 없다.

**T0에서 확인 가능했던 근거**  
당시 MEG 가격과 hedge workout price.

**경제적 전달경로**  
주식교환분을 헤지해 고정대가를 잠그고 CVR만 보유하면 경매 spectrum proceeds라는 특정 사건의 확률가중 payoff를 분리할 수 있다.

**숨은 가정**  
헤지비율·차입비용·배당조정이 정확하고, CVR 계약상 공제·세금·지급시기가 분석과 일치한다는 가정이다.

**사전 반증조건**  
경매가 실패하거나 순수취액이 시장내재가보다 낮고 지급이 크게 지연되면 반증한다.

**실제 결과**  
거래는 종결됐지만 시간·borrow·배당·break risk가 존재했다.

**정량 gap과 판정 이유**  
회계적 0과 경제적 0은 다름. 무료옵션도 carrying cost와 break loss를 확률가중한다.

**재사용 교훈**  
CVR은 headline asset value가 아니라 계약서상 distributable proceeds와 지급단위 수로 계산한다.
### C6. 10~12개월에 20~30% ROI — 부분 성공

**원문 주장**  
CVR $2~3 지급이면 내재가·시간 대비 높은 IRR이다.

**T0에서 확인 가능했던 근거**  
$0.85 implied value와 auction timing.

**경제적 전달경로**  
주식교환분을 헤지해 고정대가를 잠그고 CVR만 보유하면 경매 spectrum proceeds라는 특정 사건의 확률가중 payoff를 분리할 수 있다.

**숨은 가정**  
헤지비율·차입비용·배당조정이 정확하고, CVR 계약상 공제·세금·지급시기가 분석과 일치한다는 가정이다.

**사전 반증조건**  
경매가 실패하거나 순수취액이 시장내재가보다 낮고 지급이 크게 지연되면 반증한다.

**실제 결과**  
양의 지급은 있었으나 원문 payout base와 정확히 일치하지 않았다.

**정량 gap과 판정 이유**  
방향 성공·수익규모 과대. event IRR은 payout 분포와 지연기간별 민감도로 제시한다.

**재사용 교훈**  
CVR은 headline asset value가 아니라 계약서상 distributable proceeds와 지급단위 수로 계산한다.

---

## 4. Valuation과 Payoff Structure

원문은 KRON 등 일부 station의 FCC opening bid와 방송현금가치 차이를 보고 CVR 최대 $4, 보수적 $2~3을 제시했다. 6% merger discount를 적용하면 시장내재 CVR 약 $0.85, $2 지급 시 약 20%, $3 시 약 30% ROI라고 계산했다. 약점은 opening bid를 clearing proceeds로 연결하고 CVR 계약상 순분배 bridge를 충분히 공개하지 않은 것이다.

### 원문 수치와 실제 결과

| 지표 | T0 | VIC 기대 | 실제 | 판정 |
|---|---|---|---|---|
| 고정대가 | $10.55+0.1249 NXST | hedge로 잠금 | 거래 종결 | 성공 |
| 내재 CVR | 약 $0.85 | $2~3 | 양의 지급 | 부분 성공 |
| Gross spectrum | opening bids | 높은 proceeds | 약 $478.6m | 성공 |
| CVR 초기 지급 | 미상 | $2~3/권리 | 총 약 $258.6m | 부분 실패 |
| ROI | 20~30% | 10~12개월 | 정확 spread 자료 없음 | 미검증 |

---

## 5. 실제로 무슨 일이 일어났는가

| 날짜 | 사건 | 논지에 미친 의미 |
|---|---|---|
| 2016-01 | MEG-NXST 합병계약 | cash·stock·CVR 구조 확정 |
| 2016-01-29 | VIC pair trade | CVR 내재가 $0.85 |
| 2017-01-17 | 합병 종결 | 고정대가 지급 |
| 2017 | FCC auction 결과 | gross proceeds $478.6m |
| 2017 | CVR 초기 지급 | 총 약 $258.6m |
| 이후 | 관련 liability 약 $12.4m | 추가 정산 잔액 |

---

## 6. 실제 투자결과와 실행 가능성

| 기간 | 실제 방향 기준 가격수익률 |
|---|---:|
| 전 기간 | SQL performance row 없음 |

이 10건은 제공 SQL에 가격성과 행이 없다. 임의 외부가격을 섞지 않았으며, 사업·촉매 판정과 가격수익률 판정을 분리한다.

Pair trade였으므로 MEG 또는 NXST 단독 가격수익률로 판정하면 안 된다. 정확한 성과는 MEG 매입가, NXST short 체결가·배당·borrow, cash consideration, CVR 배분액과 지급일을 합산해야 한다. 제공 SQL에는 해당 spread performance가 없다.

---

## 7. Claim별 사후 판정

| Claim | 내용 | 비중 | 판정 | 핵심 gap |
|---|---|---:|---|---|
| C1 | 0.1249 NXST short가 합병주가 위험을 제거한다 | 18% | 성공 | 기본 hedge ratio 적중; borrow·배당은 별도. |
| C2 | 시장내재 CVR은 약 $0.85다 | 16% | 부분 성공 | 0보다 컸으나 정확 per-CVR 실현값은 자료제약. |
| C3 | CVR은 $2~3, 최대 $4다 | 22% | 부분 실패 | 경매 성공이나 $2~3 base는 과대. |
| C4 | FCC 경매는 실행된다 | 14% | 성공 | binary execution 방향 적중. |
| C5 | CVR이 0이어도 downside는 0에 가깝다 | 16% | 부분 실패 | 회계적 0과 경제적 0은 다름. |
| C6 | 10~12개월에 20~30% ROI | 14% | 부분 성공 | 방향 성공·수익규모 과대. |

---

## 8. 무엇이 실제 수익 또는 손실을 만들었는가

성과는 방향성 방송주 Long이 아니라 계약설계에서 나왔다. 0.1249 hedge가 주식대가 변동을 상쇄하고, 거래종결로 $10.55 cash가 확정되며, 경매수익이 CVR에 별도 귀속됐다. 오차는 경매성공 여부가 아니라 net distributable amount 추정에서 발생했다.

### Counterfactual

opening bid가 50% haircut되고 gross proceeds의 40%만 계약상 CVR에 배분되며 지급이 6개월 지연돼도 $0.85 내재가보다 높은 IRR인가?

---

## 9. 분석 오류와 최초 경고

FCC opening bid, gross proceeds, issuer net proceeds, CVR distributable proceeds를 혼용했다. CVR이 0이어도 downside 0이라는 말도 time value, borrow cost, deal break risk, dividend mismatch를 제외한 표현이다.

**최초 경고:** 2017 — 약 $478.6m gross proceeds 대비 CVR 초기 지급액 약 $258.6m이 공개돼 gross-to-net haircut의 크기가 드러났다.

---

## 10. 재사용 가능한 교훈과 체크리스트

특수상황은 자산의 headline 가치가 아니라 계약상 waterfall, 지급단위, 시간으로만 IRR을 계산하고 hedge cash flow까지 포함한다.

1. exchange ratio와 hedge rebalancing
2. deal break·regulatory conditions
3. gross-to-net CVR waterfall
4. 세금·거래비용·escrow
5. CVR outstanding 수와 지급순위
6. short borrow·배당·지급지연

---

## 11. 최종 Scorecard

| 평가축 | 판정 |
|---|---|
| Business thesis | 해당 없음 |
| Valuation thesis | 부분 성공 |
| Catalyst thesis | 성공 |
| Timing / path | 부분 성공 |
| Security selection | 강한 성공 |
| Thesis score | 8.0/10 |
| Process score | 8.4/10 |
| 종합 | **구조 성공·CVR 가치 과대** |

### 한 문장 교훈

> 특수상황은 자산의 headline 가치가 아니라 계약상 waterfall, 지급단위, 시간으로만 IRR을 계산하고 hedge cash flow까지 포함한다.

---

## 12. Sources / Validation Notes

1. [VIC 원 투자논지](https://www.valueinvestorsclub.com/idea/NEXSTAR_BROADCASTING_GROUP_NXST/2939181073) — 2016-01-29, jdr907. T0 주장·수치·촉매·위험 복원.
2. [Nexstar 2005 Form 10-K](https://www.sec.gov/Archives/edgar/data/1142417/000119312506055276/d10k.htm) — SEC, 2006-03. 2005 retrans 분쟁·차입·사업구조.
3. [Newport acquisition announcement](https://www.nexstar.tv/nexstar-broadcasting-and-mission-broadcasting-to-acquire-12-television-stations-in-eight-markets-and-inergize-digital-e-media-operations-from-newport-television-llc-for-285-5-million-in-cash-in-an-a/) — Nexstar, 2012-07-19. Newport 가격·구성·기대 시너지.
4. [Nexstar Q4 2012 Results](https://www.nexstar.tv/wp-content/uploads/2015/12/Nexstar-Broadcasting-Group-Q4-2012-Results.pdf) — Nexstar, 2013-02. 2012 FCF·EBITDA·거래성과.
5. [Media General acquisition completed](https://www.nexstar.tv/nexstar-broadcasting-group-completes-acquisition-of-media-general-creating-nexstar-media-group-the-nations-second-largest-television-broadcaster/) — Nexstar, 2017-01-17. 거래종결·방송국 규모·divestiture.
6. [Tribune transaction completed](https://www.nexstar.tv/nexstar_completes_tribune_transaction_2019/) — Nexstar, 2019-09-19. Tribune 거래·매각·시너지·FCF guide.
7. [Nexstar FY2020 Results](https://www.nexstar.tv/nexstar-media-group-reports-record-fourth-quarter-net-revenue-of-1377-million/) — Nexstar, 2021-02-23. 2020 record FCF와 정치광고.
8. [Nexstar FY2022 Results](https://www.nexstar.tv/wp-content/uploads/2023/02/NXST-Q4-2022-2-28-23-FINAL.pdf) — Nexstar, 2023-02-28. 2022 FCF·주주환원·CW 영향.

### 데이터 품질

- VIC 원문·방향·목표: **A/B** — 제공 SQL 원문과 링크 교차검증
- 사업·거래·재무 수치: **A** — SEC와 회사 공시 중심
- 평가기준일 내 사건 판정: **A/B** — 원문 Claim과 공시 타임라인 연결
- 기간별 가격수익률: **N/A — 제공 SQL에 행 없음
- 배당포함 total return·일별 MFE/MAE: **미검증**
