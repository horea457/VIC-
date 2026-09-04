# Batch 017 — Sprint·AT&T Telecom 10건

평가기준일: 2024-01-31

분석일: 2026-09-05

대상: Sprint 6건 · AT&T 4건

## 결론부터

이번 배치는 telecom에서 **좋은 자산·좋은 현금흐름과 좋은 주식이 왜 서로 다를 수 있는지**를 본다.

- **Sprint:** 2005·2008 Long은 Nextel integration과 asset-value floor를 과신해 크게 실패했다. 2010 Short는 standalone economics를 더 정확히 봤지만 SoftBank rescue를 놓쳤다. 2014 Long은 2.5GHz spectrum과 SoftBank-era turnaround를 상당히 잘 봤다. 2016 Short는 handset-lease accounting 비판은 예리했지만 '-$4.2bn normalized FCF'와 T-Mobile takeover 확률을 크게 틀렸다. 2020 merger arb는 사업 전망이 아니라 계약조건과 closing probability만 분석해 가장 깔끔하게 성공했다.
- **AT&T:** 2018 Long은 Time Warner 인수 뒤 FCF·deleveraging을 정확히 맞혀 $40 목표에 근접했다. 2020 Short는 가격은 맞았지만 COVID가 큰 원인이어서 causal attribution이 혼합이다. 2021 두 Long은 HBO Max·fiber 같은 operating 변수는 일부 맞았지만 WarnerMedia spin이라는 corporate-structure 변화를 놓쳐 equity thesis가 무너졌다.

> 데이터 경고 1: 원 SQL ticker `S`에는 Sprint 외에 Sears·Sherritt 레코드가 섞여 있다. 이번 배치는 회사명·본문을 검수해 실제 Sprint 6건만 사용했다.
>
> 데이터 경고 2: 이번 10건은 모두 원 SQL `is_short=true`다. 그러나 실제 방향은 Sprint 2005/2008/2014 Long, 2010/2016 Short, 2020 Long S/Short TMUS merger-arb, AT&T 2018/2021.01/2021.05 Long, AT&T 2020 Short다. 원본 flag는 감사추적용으로 보존하고 research layer에서 교정한다.

---

# SPRINT / SPRINT NEXTEL (S) — 기업과 비즈니스

## 1. 무슨 기업인가

Sprint는 미국 전국 단위 이동통신 사업자였으며 2005년 Nextel과 합병한 뒤 CDMA 기반 Sprint망과 iDEN 기반 Nextel망을 동시에 운영했다. 사업의 본질은 spectrum·기지국·backhaul·core network에 대규모 고정비를 선투자한 뒤 postpaid·prepaid 가입자의 월 서비스료에서 고객획득·단말기·network·sales 비용을 차감하는 구조였다. 2005~2010년 Sprint의 핵심 문제는 단순한 가입자 감소가 아니라 서로 다른 두 망과 브랜드를 합치는 과정에서 network quality·customer service·handset lineup이 동시에 악화되며 churn이 상승했다는 점이다. 반대로 가장 중요한 자산은 전국 단위 spectrum, 특히 2.5GHz 중대역이었다. 이 자산은 Sprint 자체 운영 아래에서는 충분히 monetization되지 못했지만 훗날 T-Mobile 합병에서 핵심 전략가치가 됐다. 따라서 Sprint를 분석할 때는 postpaid net adds, churn, ARPU, service revenue, adjusted EBITDA, network CapEx, 실제 FCF, handset financing/lease accounting, gross debt·maturities, spectrum의 사용가능성과 담보가치, 그리고 전략적 buyer 가능성을 함께 봐야 한다.

## 2. 산업 가치사슬과 돈의 흐름

Sprint의 돈 흐름은 '가입자수 × ARPU → service revenue → network·sales·device·customer-care 비용 → EBITDA → network CapEx·handset cash outflow·interest → FCF' 순이다. 무선망은 고정비가 커 가입자 증가가 margin을 크게 높일 수 있지만, 반대로 churn이 올라가면 같은 고정비를 더 적은 고객에게 배분해야 해 margin이 급격히 악화된다. 2010년대의 EIP·handset lease는 회계상 EBITDA와 실제 현금흐름을 더 복잡하게 만들었다. 단말기를 leasing하면 일부 비용이 당기 EBITDA에서 자산으로 이동할 수 있지만 현금은 먼저 나가기 때문에 EBITDA 개선과 FCF 개선을 동일시하면 안 된다. Spectrum은 매우 큰 자산가치를 가질 수 있지만 operating network에 묶여 있거나 FCC ownership cap·담보·고객망 제약이 있으면 liquidation value를 즉시 equity로 전환할 수 없다.

## 3. 경쟁우위·경쟁구도·핵심 지표

Sprint의 경쟁우위 후보는 전국망, 2.5GHz spectrum depth, 대규모 customer base와 SoftBank의 자본이었다. 그러나 Verizon·AT&T·T-Mobile 대비 network perception, churn, distribution, handset portfolio, balance sheet가 약했고, 특히 Nextel 통합 실패가 수년간 브랜드와 economics를 훼손했다. 2014 이후 network modernization과 cost cutting은 실제 개선을 만들었지만 높은 부채와 낮은 scale efficiency는 여전히 제약이었다. 이 기업의 역사는 '좋은 spectrum = 좋은 독립기업'이 아님을 보여준다. 핵심은 spectrum을 실제 coverage/capacity·customer retention·FCF로 전환할 운영능력과 자본구조다.

## 4. 아이디어 전체 판정

| 게시일 | 원 SQL | 실제방향 | 핵심 논지 | 가격·증권 결과 | 종합판정 |
|---|---|---|---|---|---|
| 2005-11-17 | Short | Long | Nextel 합병 후 ILEC spin·levered buyback·$37 Long | $24.27 진입 뒤 합병 통합이 무너지며 2008년 말까지 주가가 사실상 붕괴. Sprint 2010 10-K 성과표 기준 2005년 말 $100 투자액은 2008년 말 $8.61, 2010년 말 $19.90. | 치명적 실패 |
| 2008-04-03 | Short | Long | QChat·network turnaround 또는 breakup $12~17 Long | 약 $6 부근에서 $12.44~17을 제시했지만 2008 금융위기와 Sprint 운영악화 속 주가는 $2 안팎까지 하락. 회복 thesis 실패. | 실패한 turnaround·asset-value trap |
| 2010-03-10 | Short | Short | 고비용·가입자 감소·FCF 압축 Short | 단기적으로 Sprint 주가는 2011년 $2대까지 내려 short 논지가 작동했지만, 2012 SoftBank 거래 발표 이후 생존·재자본화로 크게 반등. 파산/영구가치 훼손 thesis는 부분 실패. | 운영논지 상당 부분 적중·전략적 rescue 미반영 |
| 2014-08-06 | Short | Long | SoftBank·2.5GHz spectrum·Claure turnaround Long | 약 $6에서 FY2017 고점 $9.65까지 상승했지만 'near term $10+, 장기 2~3x'는 평가 horizon 내 미달. | 자산·운영개선 통찰 적중·목표가/시간 부분 실패 |
| 2016-03-09 | Short | Short | Handset lease accounting·-$4.2bn normalized FCF·equity zero Short | 약 $4에서 FY2017 high $9.65까지 상승. Short는 큰 adverse move를 겪었고 strategic T-Mobile exit까지 이어져 증권 thesis 실패. | 회계/FCF 통찰은 좋았지만 증권 thesis 실패 |
| 2020-02-21 | Short | Merger Arb: Long S / Short TMUS | T-Mobile merger 마지막 45~60일 spread Long | 거래는 작성자 예상 4월 6일보다 빠른 2020-04-01 종결. non-SoftBank Sprint 주주는 1주당 0.10256 TMUS를 받아 spread trade가 성공. | 깔끔한 성공 |

---

<!-- idea:c415e3a6-eaa9-4be0-901f-8877d9ee2c3d -->
## 1. 2005-11-17 — Nextel 합병 후 ILEC spin·levered buyback·$37 Long

### 결론부터

**종합판정: 치명적 실패.** 이 글은 balance sheet optionality와 spin-off mechanics를 정교하게 계산했지만 M&A 이후 가장 중요한 '결합된 고객가치가 유지되는가'를 후순위로 뒀다. 낮은 pro forma leverage는 운영이 안정적일 때만 자사주용 자원이다. 통합이 실패하면 같은 debt capacity가 liquidity buffer로 필요해진다. 또한 $2 downside라는 평가는 고정비 무선사업의 churn·network failure가 equity에 미치는 비선형성을 거의 반영하지 못했다.

**주가·증권 결과:** $24.27 진입 뒤 합병 통합이 무너지며 2008년 말까지 주가가 사실상 붕괴. Sprint 2010 10-K 성과표 기준 2005년 말 $100 투자액은 2008년 말 $8.61, 2010년 말 $19.90.

**Thesis / Process 점수:** 4.2 / 4.5

### 1. 무슨 기업인가

Sprint는 미국 전국 단위 이동통신 사업자였으며 2005년 Nextel과 합병한 뒤 CDMA 기반 Sprint망과 iDEN 기반 Nextel망을 동시에 운영했다. 사업의 본질은 spectrum·기지국·backhaul·core network에 대규모 고정비를 선투자한 뒤 postpaid·prepaid 가입자의 월 서비스료에서 고객획득·단말기·network·sales 비용을 차감하는 구조였다. 2005~2010년 Sprint의 핵심 문제는 단순한 가입자 감소가 아니라 서로 다른 두 망과 브랜드를 합치는 과정에서 network quality·customer service·handset lineup이 동시에 악화되며 churn이 상승했다는 점이다. 반대로 가장 중요한 자산은 전국 단위 spectrum, 특히 2.5GHz 중대역이었다. 이 자산은 Sprint 자체 운영 아래에서는 충분히 monetization되지 못했지만 훗날 T-Mobile 합병에서 핵심 전략가치가 됐다. 따라서 Sprint를 분석할 때는 postpaid net adds, churn, ARPU, service revenue, adjusted EBITDA, network CapEx, 실제 FCF, handset financing/lease accounting, gross debt·maturities, spectrum의 사용가능성과 담보가치, 그리고 전략적 buyer 가능성을 함께 봐야 한다.

### 2. 산업 가치사슬과 돈의 흐름

Sprint의 돈 흐름은 '가입자수 × ARPU → service revenue → network·sales·device·customer-care 비용 → EBITDA → network CapEx·handset cash outflow·interest → FCF' 순이다. 무선망은 고정비가 커 가입자 증가가 margin을 크게 높일 수 있지만, 반대로 churn이 올라가면 같은 고정비를 더 적은 고객에게 배분해야 해 margin이 급격히 악화된다. 2010년대의 EIP·handset lease는 회계상 EBITDA와 실제 현금흐름을 더 복잡하게 만들었다. 단말기를 leasing하면 일부 비용이 당기 EBITDA에서 자산으로 이동할 수 있지만 현금은 먼저 나가기 때문에 EBITDA 개선과 FCF 개선을 동일시하면 안 된다. Spectrum은 매우 큰 자산가치를 가질 수 있지만 operating network에 묶여 있거나 FCC ownership cap·담보·고객망 제약이 있으면 liquidation value를 즉시 equity로 전환할 수 없다.

### 3. 경쟁우위·경쟁구도·핵심 지표

Sprint의 경쟁우위 후보는 전국망, 2.5GHz spectrum depth, 대규모 customer base와 SoftBank의 자본이었다. 그러나 Verizon·AT&T·T-Mobile 대비 network perception, churn, distribution, handset portfolio, balance sheet가 약했고, 특히 Nextel 통합 실패가 수년간 브랜드와 economics를 훼손했다. 2014 이후 network modernization과 cost cutting은 실제 개선을 만들었지만 높은 부채와 낮은 scale efficiency는 여전히 제약이었다. 이 기업의 역사는 '좋은 spectrum = 좋은 독립기업'이 아님을 보여준다. 핵심은 spectrum을 실제 coverage/capacity·customer retention·FCF로 전환할 운영능력과 자본구조다.

### 4. 당시 VIC 원문과 핵심 숫자

Sprint-Nextel 합병 후 wireline(후일 Embarq)을 2Q06에 분리해 약 $8bn debt를 함께 넘기면 wireless balance sheet가 매우 저레버리지 상태가 되고, Nextel Partners와 Alamosa를 debt로 인수한 뒤에도 leverage가 낮다고 봤다. 이후 leverage를 1.5x까지 올려 대규모 자사주를 매입하면 2007 EPS가 $2.25까지 올라갈 수 있고, 성장성 있는 pure-play domestic wireless에 15x를 주면 $37이 가능하다는 논지였다. 원문은 downside $2/upside $13으로 손익비가 매우 좋다고 평가했다.

### 5. 밸류에이션과 기대수익의 연결

2007E pre-spin EPS $2.05, 적정 capital structure에서 $2.25. ILEC spin 가치 $3/share를 별도로 더하고 15x P/E를 적용해 2006년 중반 $37, 약 50%+ upside를 제시했다. Pro forma 2007 EBITDA 약 $16bn, leverage 0.8x에서 1.5x까지 올려 약 $11bn을 차입하고 15~17% 주식을 repurchase하는 구조였다. 사후에는 subscriber/churn/ARPU 또는 segment earnings → EBITDA → CapEx·interest → FCF → debt·corporate action → 기존 보통주 또는 merger spread payoff 순으로 다시 연결해 검증했다.

### 투자논지를 구성한 핵심 주장

#### 1. ILEC spin — 적중 · 논지 비중 18%

**당시 주장**

wireline 분리는 약 $8bn debt를 넘기고 wireless 자산을 해방시킨다.

**당시 근거**

Sprint-Nextel 합병 후 wireline(후일 Embarq)을 2Q06에 분리해 약 $8bn debt를 함께 넘기면 wireless balance sheet가 매우 저레버리지 상태가 되고, Nextel Partners와 Alamosa를 debt로 인수한 뒤에도 leverage가 낮다고 봤다. 이후 leverage를 1.5x까지 올려 대규모 자사주를 매입하면 2007 EPS가 $2.25까지 올라갈 수 있고, 성장성 있는 pure-play domestic wireless에 15x를 주면 $37이 가능하다는 논지였다. 원문은 downside $2/upside $13으로 손익비가 매우 좋다고 평가했다.

**이 주장이 성립하려면**

spin이 세금·financing 계획대로 완료되고 wireless earnings가 유지

**사전 반증조건**

spin 이후에도 wireless operating deterioration

**실제 결과**

Embarq spin은 실제 2006년 5월 완료됐다.

**정량적 괴리**

진입/목표가 / $24.27 / $37 / 2008년 사실상 붕괴

**분석 오류·핵심**

핵심 causal chain은 실제 결과에서 확인됐다. 다만 그 성공이 증권 payoff의 원인이었는지는 별도 판정한다.

**재사용할 교훈**

ILEC spin 가설은 'spin 이후에도 wireless operating deterioration'를 사전 반증조건으로 저장하고 사업·이벤트·가격 판정을 분리한다.

#### 2. NXTP/APCS accretion — 실패 · 논지 비중 18%

**당시 주장**

Nextel Partners·Alamosa 인수는 debt financing으로도 FCF accretive다.

**당시 근거**

Sprint-Nextel 합병 후 wireline(후일 Embarq)을 2Q06에 분리해 약 $8bn debt를 함께 넘기면 wireless balance sheet가 매우 저레버리지 상태가 되고, Nextel Partners와 Alamosa를 debt로 인수한 뒤에도 leverage가 낮다고 봤다. 이후 leverage를 1.5x까지 올려 대규모 자사주를 매입하면 2007 EPS가 $2.25까지 올라갈 수 있고, 성장성 있는 pure-play domestic wireless에 15x를 주면 $37이 가능하다는 논지였다. 원문은 downside $2/upside $13으로 손익비가 매우 좋다고 평가했다.

**이 주장이 성립하려면**

Nextel 고객·network economics가 유지

**사전 반증조건**

iDEN churn·integration cost가 인수가치를 상쇄

**실제 결과**

Nextel ecosystem 전체 가치가 통합실패로 크게 훼손됐다.

**정량적 괴리**

Leverage / pro forma 약 0.8x / 1.5x까지 의도적 확대 / 운영악화 속 debt 부담이 약점으로 전환

**분석 오류·핵심**

좋은 자산·평균 operating path를 equity payoff에 직접 연결하거나, debt·integration·corporate action·timing의 joint distribution을 충분히 stress하지 않았다.

**재사용할 교훈**

NXTP/APCS accretion 가설은 'iDEN churn·integration cost가 인수가치를 상쇄'를 사전 반증조건으로 저장하고 사업·이벤트·가격 판정을 분리한다.

#### 3. Balance-sheet leverage — 실패 · 논지 비중 16%

**당시 주장**

0.8x leverage를 1.5x로 올려 주식 15~17%를 사도 안전하다.

**당시 근거**

Sprint-Nextel 합병 후 wireline(후일 Embarq)을 2Q06에 분리해 약 $8bn debt를 함께 넘기면 wireless balance sheet가 매우 저레버리지 상태가 되고, Nextel Partners와 Alamosa를 debt로 인수한 뒤에도 leverage가 낮다고 봤다. 이후 leverage를 1.5x까지 올려 대규모 자사주를 매입하면 2007 EPS가 $2.25까지 올라갈 수 있고, 성장성 있는 pure-play domestic wireless에 15x를 주면 $37이 가능하다는 논지였다. 원문은 downside $2/upside $13으로 손익비가 매우 좋다고 평가했다.

**이 주장이 성립하려면**

EBITDA·FCF 안정

**사전 반증조건**

가입자 감소로 EBITDA·FCF가 급락

**실제 결과**

낮은 초기 leverage가 downside 방어를 보장하지 못했다.

**정량적 괴리**

M&A integration / Sprint+Nextel scale / 성장·FCF accretion / 4Q07 $29.7bn goodwill impairment

**분석 오류·핵심**

좋은 자산·평균 operating path를 equity payoff에 직접 연결하거나, debt·integration·corporate action·timing의 joint distribution을 충분히 stress하지 않았다.

**재사용할 교훈**

Balance-sheet leverage 가설은 '가입자 감소로 EBITDA·FCF가 급락'를 사전 반증조건으로 저장하고 사업·이벤트·가격 판정을 분리한다.

#### 4. Network integration — 치명적 실패 · 논지 비중 16%

**당시 주장**

Sprint와 Nextel의 결합이 고객경험을 크게 훼손하지 않는다.

**당시 근거**

Sprint-Nextel 합병 후 wireline(후일 Embarq)을 2Q06에 분리해 약 $8bn debt를 함께 넘기면 wireless balance sheet가 매우 저레버리지 상태가 되고, Nextel Partners와 Alamosa를 debt로 인수한 뒤에도 leverage가 낮다고 봤다. 이후 leverage를 1.5x까지 올려 대규모 자사주를 매입하면 2007 EPS가 $2.25까지 올라갈 수 있고, 성장성 있는 pure-play domestic wireless에 15x를 주면 $37이 가능하다는 논지였다. 원문은 downside $2/upside $13으로 손익비가 매우 좋다고 평가했다.

**이 주장이 성립하려면**

CDMA/iDEN 통합·handset·care 안정

**사전 반증조건**

churn 상승·망 품질 문제

**실제 결과**

실제 실패의 핵심이었다.

**정량적 괴리**

ILEC spin / 2Q06 예상 / $3/share 가치 실현 / 2006-05 Embarq spin 완료

**분석 오류·핵심**

좋은 자산·평균 operating path를 equity payoff에 직접 연결하거나, debt·integration·corporate action·timing의 joint distribution을 충분히 stress하지 않았다.

**재사용할 교훈**

Network integration 가설은 'churn 상승·망 품질 문제'를 사전 반증조건으로 저장하고 사업·이벤트·가격 판정을 분리한다.

#### 5. EPS $2.25 — 실패 · 논지 비중 16%

**당시 주장**

M&A·buyback 뒤 2007 EPS $2.25가 가능하다.

**당시 근거**

Sprint-Nextel 합병 후 wireline(후일 Embarq)을 2Q06에 분리해 약 $8bn debt를 함께 넘기면 wireless balance sheet가 매우 저레버리지 상태가 되고, Nextel Partners와 Alamosa를 debt로 인수한 뒤에도 leverage가 낮다고 봤다. 이후 leverage를 1.5x까지 올려 대규모 자사주를 매입하면 2007 EPS가 $2.25까지 올라갈 수 있고, 성장성 있는 pure-play domestic wireless에 15x를 주면 $37이 가능하다는 논지였다. 원문은 downside $2/upside $13으로 손익비가 매우 좋다고 평가했다.

**이 주장이 성립하려면**

operating EBITDA 유지와 buyback 실행

**사전 반증조건**

integration 비용·revenue decline

**실제 결과**

earnings power가 예상경로에서 크게 이탈했다.

**정량적 괴리**

$24.27 진입 뒤 합병 통합이 무너지며 2008년 말까지 주가가 사실상 붕괴. Sprint 2010 10-K 성과표 기준 2005년 말 $100 투자액은 2008년 말 $8.61, 2010년 말 $19.90.

**분석 오류·핵심**

좋은 자산·평균 operating path를 equity payoff에 직접 연결하거나, debt·integration·corporate action·timing의 joint distribution을 충분히 stress하지 않았다.

**재사용할 교훈**

EPS $2.25 가설은 'integration 비용·revenue decline'를 사전 반증조건으로 저장하고 사업·이벤트·가격 판정을 분리한다.

#### 6. $37 valuation — 치명적 실패 · 논지 비중 16%

**당시 주장**

15x EPS+$3 asset value로 50% upside, downside $2뿐이다.

**당시 근거**

Sprint-Nextel 합병 후 wireline(후일 Embarq)을 2Q06에 분리해 약 $8bn debt를 함께 넘기면 wireless balance sheet가 매우 저레버리지 상태가 되고, Nextel Partners와 Alamosa를 debt로 인수한 뒤에도 leverage가 낮다고 봤다. 이후 leverage를 1.5x까지 올려 대규모 자사주를 매입하면 2007 EPS가 $2.25까지 올라갈 수 있고, 성장성 있는 pure-play domestic wireless에 15x를 주면 $37이 가능하다는 논지였다. 원문은 downside $2/upside $13으로 손익비가 매우 좋다고 평가했다.

**이 주장이 성립하려면**

사업 안정·normal multiple

**사전 반증조건**

operating impairment가 multiple과 EPS를 동시에 훼손

**실제 결과**

실제 downside가 원문의 가정과 비교할 수 없을 정도로 컸다.

**정량적 괴리**

$24.27 진입 뒤 합병 통합이 무너지며 2008년 말까지 주가가 사실상 붕괴. Sprint 2010 10-K 성과표 기준 2005년 말 $100 투자액은 2008년 말 $8.61, 2010년 말 $19.90.

**분석 오류·핵심**

좋은 자산·평균 operating path를 equity payoff에 직접 연결하거나, debt·integration·corporate action·timing의 joint distribution을 충분히 stress하지 않았다.

**재사용할 교훈**

$37 valuation 가설은 'operating impairment가 multiple과 EPS를 동시에 훼손'를 사전 반증조건으로 저장하고 사업·이벤트·가격 판정을 분리한다.

### 6. 실제 사업의 시간순 전개

기업행위 자체는 상당 부분 실행됐다. Sprint-Nextel 거래는 2005년 8월 완료됐고 Embarq spin도 2006년 5월 완료됐다. 그러나 핵심 operating integration이 실패했다. 서로 다른 CDMA·iDEN망, customer service와 handset 문제로 가입자와 브랜드가 훼손됐고 4Q07에는 Nextel 관련 goodwill 등에 $29.7bn 비현금 손상차손을 인식했다. 즉 debt capacity와 buyback을 먼저 계산했지만, 합병 후 고객·network economics가 유지된다는 가장 중요한 선행조건이 무너졌다.

### 7. 사업 결과와 가격 결과 분리

증권 결과는 $24.27 진입 뒤 합병 통합이 무너지며 2008년 말까지 주가가 사실상 붕괴. Sprint 2010 10-K 성과표 기준 2005년 말 $100 투자액은 2008년 말 $8.61, 2010년 말 $19.90. 사업논지·촉매·valuation·corporate structure와 주가를 서로 다른 판정으로 저장한다.

### 8. 무엇을 잘 봤고 무엇을 놓쳤나

이 글은 balance sheet optionality와 spin-off mechanics를 정교하게 계산했지만 M&A 이후 가장 중요한 '결합된 고객가치가 유지되는가'를 후순위로 뒀다. 낮은 pro forma leverage는 운영이 안정적일 때만 자사주용 자원이다. 통합이 실패하면 같은 debt capacity가 liquidity buffer로 필요해진다. 또한 $2 downside라는 평가는 고정비 무선사업의 churn·network failure가 equity에 미치는 비선형성을 거의 반영하지 못했다.

### 9. 최초 검증·반증 신호와 회피 가능성

2007-02-28 — Sprint가 2006 실적과 함께 가입자·운영문제를 드러내고 Nextel 통합 부진이 단순 일시적 문제가 아님이 확인되기 시작했다. 4Q07 $29.7bn goodwill impairment에서 논지 실패가 사실상 확정됐다. 이 시점에 원 valuation bridge를 다시 만들면 operating thesis와 security thesis 중 무엇이 살아있는지 구분할 수 있었다. 회피 가능성: 매우 높음. ILEC spin과 인수 완료를 thesis confirmation으로 볼 것이 아니라 churn·postpaid net adds·network quality가 회복되지 않는 순간 levered buyback 가정을 폐기했어야 한다.

### 10. 최종 판정·반사실·재사용 교훈

치명적 실패. Telecom에서는 좋은 spectrum·좋은 콘텐츠·높은 FCF 하나만으로 equity floor를 만들지 않고, 실제 고객경제성·부채·corporate-action 귀속구조를 함께 stress해야 한다.

### 핵심 수치 — 당시 vs 실제

| 지표 | 글 당시 | VIC 기대 | 실제 | 판정 |
|---|---|---|---|---|
| 진입/목표가 | $24.27 | $37 | 2008년 사실상 붕괴 | 치명적 실패 |
| Leverage | pro forma 약 0.8x | 1.5x까지 의도적 확대 | 운영악화 속 debt 부담이 약점으로 전환 | 실패 |
| M&A integration | Sprint+Nextel scale | 성장·FCF accretion | 4Q07 $29.7bn goodwill impairment | 치명적 실패 |
| ILEC spin | 2Q06 예상 | $3/share 가치 실현 | 2006-05 Embarq spin 완료 | 촉매 적중 |

### 사건 타임라인

| 시점 | 사건 | 논지에 대한 의미 |
|---|---|---|
| 2005-11-17 | VIC 아이디어 게시 | Nextel 합병 후 ILEC spin·levered buyback·$37 Long |
| 2007-02-28 | 최초 핵심 검증·반증 신호 | Sprint가 2006 실적과 함께 가입자·운영문제를 드러내고 Nextel 통합 부진이 단순 일시적 문제가 아님이 확인되기 시작했다. 4Q07 $29.7bn goodwill impairment에서 논지 실패가 사실상 확정됐다. |
| 2007-12-31 | Nextel 통합 손상 확인 | 2007년 대규모 goodwill impairment로 합병가치 훼손이 공식화 |
| 2016-12-31 | SoftBank-era operating/FCF 재평가 | 비용·network·subscriber economics가 과거와 달라졌는지 점검 |
| 2020-04-01 | Sprint 독립기업 종료 | T-Mobile merger 종결, 2.5GHz spectrum strategic value가 결합회사로 이전 |
| 2024-01-31 | 고정 사후평가 | Sprint 독립 equity는 소멸했으므로 원 security thesis는 merger 시점까지 평가 |

### Failure / Success Anatomy

- **근본 오류:** spectrum·balance-sheet 자산가치를 operating customer economics 또는 strategic exit probability와 잘못 연결
- **최초 검증·반증 신호:** 2007-02-28 — Sprint가 2006 실적과 함께 가입자·운영문제를 드러내고 Nextel 통합 부진이 단순 일시적 문제가 아님이 확인되기 시작했다. 4Q07 $29.7bn goodwill impairment에서 논지 실패가 사실상 확정됐다.
- **당시 알 수 있었나:** 가입자 순증·churn·ARPU·service revenue·EBITDA·CapEx·FCF·gross debt·maturities·spectrum 사용·corporate-action 조건은 공시와 earnings에서 재검증 가능했다.
- **피할 수 있었나:** 매우 높음. ILEC spin과 인수 완료를 thesis confirmation으로 볼 것이 아니라 churn·postpaid net adds·network quality가 회복되지 않는 순간 levered buyback 가정을 폐기했어야 한다.
- **반사실 질문:** spectrum·segment business가 가치 있어도 integration, debt, corporate action 또는 security horizon이 반대로 움직이면 기존 보통주/스프레드의 payoff는 어떻게 달라지는가?
- **성공 패턴:** spectrum_optionality; fixed_cost_operating_leverage; event_driven_merger_arb; network_turnaround; strategic_buyer
- **실패·주의 패턴:** integration_failure; asset_value_trap; fcf_normalization_error; leverage; strategic_option_underpricing

### 주요 근거자료

- [1. VIC S 2005-11-17 원문](https://www.valueinvestorsclub.com/idea/Sprint_Nextel_Corp/4156157924) — Value Investors Club, 2005-11-17. 원 SQL description에서 당시 thesis·valuation·risk·catalyst·방향을 복원
- [2. Sprint 2006 Form 10-K](https://www.sec.gov/Archives/edgar/data/101830/000119312507040849/d10k.htm) — SEC, 2007-02-28. Nextel merger·Embarq spin·초기 통합상태 확인
- [3. Sprint Nextel 2007 Form 10-K](https://www.sec.gov/Archives/edgar/data/101830/000119312508043342/d10k.htm) — SEC, 2008-02-29. 4Q07 약 $29.7bn goodwill impairment·subscriber 문제 확인
- [4. Sprint FY2008 Results](https://www.sec.gov/Archives/edgar/data/101830/000119312509035054/dex991.htm) — Sprint/SEC, 2009-02-19. FY2008 free cash flow $1.8bn+ 확인
- [5. Sprint 2010 Form 10-K](https://www.sec.gov/Archives/edgar/data/101830/000119312511045676/d10k.htm) — SEC, 2011-02-24. 2010 operating cash flow·postpaid trends·historical shareholder performance 확인
- [6. Sprint 2014 Form 10-K](https://www.sec.gov/Archives/edgar/data/101830/000010183015000028/s-20150331x10k.htm) — SEC, 2015-05-26. network modernization·customer trends·SoftBank-era 상태 확인
- [7. Sprint FY2015 Results](https://newsroom.sprint.com/sprint-reports-fourth-quarter-and-fiscal-year-2015-results.htm) — Sprint, 2016-05-03. Adj EBITDA $8.1bn·postpaid net adds 1.2m+·churn 개선 확인
- [8. Sprint FY2016 Results](https://group.softbank/en/news/press/20170503) — Sprint/SoftBank, 2017-05-03. FY2016 adjusted FCF +$607m 등 turnaround cash flow 확인
- [9. Sprint FY2017 Results](https://newsroom.sprint.com/sprint-reports-fourth-quarter-and-fiscal-year-2017-results.htm) — Sprint, 2018-05-02. FY2017 adjusted FCF +$945m·두 해 연속 positive 확인
- [10. T-Mobile and Sprint amend merger terms](https://www.t-mobile.com/news/un-carrier/t-mobile-sprint-amend-business-combination-agreement) — T-Mobile, 2020-02-20. non-SoftBank Sprint 0.10256 exchange ratio 확인
- [11. T-Mobile completes merger with Sprint](https://www.t-mobile.com/news/un-carrier/t-mobile-sprint-one-company) — T-Mobile, 2020-04-01. 2020-04-01 종결 및 exchange ratio 확인
- 12. Sprint historical price context — Macrotrends/market history, 2020-04-01. VIC 당시 가격과 주요 저점·고점 교차검증


---

<!-- idea:772c76bc-9d62-4a64-bcb0-9a0b9271687a -->
## 2. 2008-04-03 — QChat·network turnaround 또는 breakup $12~17 Long

### 결론부터

**종합판정: 실패한 turnaround·asset-value trap.** 가장 큰 오류는 'operating turnaround'와 'breakup floor'를 독립적인 두 안전망처럼 더한 것이다. 실제로 고객이 빠지면 spectrum·network·brand의 standalone value도 낮아지고, 높은 debt와 지속 CapEx 때문에 asset sale proceeds가 기존 equity에 온전히 귀속되지 않는다. Spectrum은 가치가 있어도 operating network에 묶인 상태에서는 현금과 다르다.

**주가·증권 결과:** 약 $6 부근에서 $12.44~17을 제시했지만 2008 금융위기와 Sprint 운영악화 속 주가는 $2 안팎까지 하락. 회복 thesis 실패.

**Thesis / Process 점수:** 5.8 / 6.2

### 1. 무슨 기업인가

Sprint는 미국 전국 단위 이동통신 사업자였으며 2005년 Nextel과 합병한 뒤 CDMA 기반 Sprint망과 iDEN 기반 Nextel망을 동시에 운영했다. 사업의 본질은 spectrum·기지국·backhaul·core network에 대규모 고정비를 선투자한 뒤 postpaid·prepaid 가입자의 월 서비스료에서 고객획득·단말기·network·sales 비용을 차감하는 구조였다. 2005~2010년 Sprint의 핵심 문제는 단순한 가입자 감소가 아니라 서로 다른 두 망과 브랜드를 합치는 과정에서 network quality·customer service·handset lineup이 동시에 악화되며 churn이 상승했다는 점이다. 반대로 가장 중요한 자산은 전국 단위 spectrum, 특히 2.5GHz 중대역이었다. 이 자산은 Sprint 자체 운영 아래에서는 충분히 monetization되지 못했지만 훗날 T-Mobile 합병에서 핵심 전략가치가 됐다. 따라서 Sprint를 분석할 때는 postpaid net adds, churn, ARPU, service revenue, adjusted EBITDA, network CapEx, 실제 FCF, handset financing/lease accounting, gross debt·maturities, spectrum의 사용가능성과 담보가치, 그리고 전략적 buyer 가능성을 함께 봐야 한다.

### 2. 산업 가치사슬과 돈의 흐름

Sprint의 돈 흐름은 '가입자수 × ARPU → service revenue → network·sales·device·customer-care 비용 → EBITDA → network CapEx·handset cash outflow·interest → FCF' 순이다. 무선망은 고정비가 커 가입자 증가가 margin을 크게 높일 수 있지만, 반대로 churn이 올라가면 같은 고정비를 더 적은 고객에게 배분해야 해 margin이 급격히 악화된다. 2010년대의 EIP·handset lease는 회계상 EBITDA와 실제 현금흐름을 더 복잡하게 만들었다. 단말기를 leasing하면 일부 비용이 당기 EBITDA에서 자산으로 이동할 수 있지만 현금은 먼저 나가기 때문에 EBITDA 개선과 FCF 개선을 동일시하면 안 된다. Spectrum은 매우 큰 자산가치를 가질 수 있지만 operating network에 묶여 있거나 FCC ownership cap·담보·고객망 제약이 있으면 liquidation value를 즉시 equity로 전환할 수 없다.

### 3. 경쟁우위·경쟁구도·핵심 지표

Sprint의 경쟁우위 후보는 전국망, 2.5GHz spectrum depth, 대규모 customer base와 SoftBank의 자본이었다. 그러나 Verizon·AT&T·T-Mobile 대비 network perception, churn, distribution, handset portfolio, balance sheet가 약했고, 특히 Nextel 통합 실패가 수년간 브랜드와 economics를 훼손했다. 2014 이후 network modernization과 cost cutting은 실제 개선을 만들었지만 높은 부채와 낮은 scale efficiency는 여전히 제약이었다. 이 기업의 역사는 '좋은 spectrum = 좋은 독립기업'이 아님을 보여준다. 핵심은 spectrum을 실제 coverage/capacity·customer retention·FCF로 전환할 운영능력과 자본구조다.

### 4. 당시 VIC 원문과 핵심 숫자

Nextel rebanding과 vocoder 문제로 생긴 network quality 악화가 이미 대부분 해결됐는데 customer perception과 sell-side가 이를 늦게 반영하고 있다고 봤다. QChat으로 iDEN 고객을 CDMA로 이전하고 새 handset·Dan Hesse 광고가 gross adds와 retention을 회복시킬 것이라 예상했다. 만약 turnaround가 늦어져도 2.5GHz/iDEN spectrum, long-distance fiber, Boost와 subscriber asset을 분리 매각하면 $12 이상 가치가 있다고 주장했다.

### 5. 밸류에이션과 기대수익의 연결

운영 정상화 시 postpaid 33m, ARPU $55, wireless EBITDA $7.7bn + long distance $0.875bn을 7.5x에 평가해 $17. FCF 약 $2bn, yield 12.6%. Breakup은 2.5GHz spectrum $2.35/share, iDEN spectrum $1.46, long distance $2.44, Boost 등 합산 후 debt 차감해 약 $12.44. 사후에는 subscriber/churn/ARPU 또는 segment earnings → EBITDA → CapEx·interest → FCF → debt·corporate action → 기존 보통주 또는 merger spread payoff 순으로 다시 연결해 검증했다.

### 투자논지를 구성한 핵심 주장

#### 1. Network repair — 실패 · 논지 비중 18%

**당시 주장**

Nextel망 품질은 이미 크게 회복됐고 인식만 뒤처졌다.

**당시 근거**

Nextel rebanding과 vocoder 문제로 생긴 network quality 악화가 이미 대부분 해결됐는데 customer perception과 sell-side가 이를 늦게 반영하고 있다고 봤다. QChat으로 iDEN 고객을 CDMA로 이전하고 새 handset·Dan Hesse 광고가 gross adds와 retention을 회복시킬 것이라 예상했다. 만약 turnaround가 늦어져도 2.5GHz/iDEN spectrum, long-distance fiber, Boost와 subscriber asset을 분리 매각하면 $12 이상 가치가 있다고 주장했다.

**이 주장이 성립하려면**

실제 call quality·churn 개선

**사전 반증조건**

subscriber loss 지속

**실제 결과**

2008에도 churn과 고객손실이 이어졌다.

**정량적 괴리**

주가 / 약 $6 / $12.44~17 / $2 안팎까지 하락

**분석 오류·핵심**

좋은 자산·평균 operating path를 equity payoff에 직접 연결하거나, debt·integration·corporate action·timing의 joint distribution을 충분히 stress하지 않았다.

**재사용할 교훈**

Network repair 가설은 'subscriber loss 지속'를 사전 반증조건으로 저장하고 사업·이벤트·가격 판정을 분리한다.

#### 2. QChat migration — 실패 · 논지 비중 18%

**당시 주장**

QChat이 iDEN 고객을 CDMA로 옮겨 churn을 줄인다.

**당시 근거**

Nextel rebanding과 vocoder 문제로 생긴 network quality 악화가 이미 대부분 해결됐는데 customer perception과 sell-side가 이를 늦게 반영하고 있다고 봤다. QChat으로 iDEN 고객을 CDMA로 이전하고 새 handset·Dan Hesse 광고가 gross adds와 retention을 회복시킬 것이라 예상했다. 만약 turnaround가 늦어져도 2.5GHz/iDEN spectrum, long-distance fiber, Boost와 subscriber asset을 분리 매각하면 $12 이상 가치가 있다고 주장했다.

**이 주장이 성립하려면**

device adoption·coverage 원활

**사전 반증조건**

migration 지연·고객 이탈

**실제 결과**

기대만큼 빠른 turnaround를 만들지 못했다.

**정량적 괴리**

FCF / 약 $2bn 예상 / 12.6% yield / FY2008 $1.8bn+ FCF

**분석 오류·핵심**

좋은 자산·평균 operating path를 equity payoff에 직접 연결하거나, debt·integration·corporate action·timing의 joint distribution을 충분히 stress하지 않았다.

**재사용할 교훈**

QChat migration 가설은 'migration 지연·고객 이탈'를 사전 반증조건으로 저장하고 사업·이벤트·가격 판정을 분리한다.

#### 3. Handset/marketing — 실패 · 논지 비중 16%

**당시 주장**

새 handset와 Hesse 캠페인이 gross adds를 회복시킨다.

**당시 근거**

Nextel rebanding과 vocoder 문제로 생긴 network quality 악화가 이미 대부분 해결됐는데 customer perception과 sell-side가 이를 늦게 반영하고 있다고 봤다. QChat으로 iDEN 고객을 CDMA로 이전하고 새 handset·Dan Hesse 광고가 gross adds와 retention을 회복시킬 것이라 예상했다. 만약 turnaround가 늦어져도 2.5GHz/iDEN spectrum, long-distance fiber, Boost와 subscriber asset을 분리 매각하면 $12 이상 가치가 있다고 주장했다.

**이 주장이 성립하려면**

제품경쟁력·distribution 개선

**사전 반증조건**

경쟁사 대비 handset/network 열위 지속

**실제 결과**

회복 속도가 thesis보다 느렸다.

**정량적 괴리**

Postpaid / 33m 안정화 가정 / churn 정상화 / subscriber losses 지속

**분석 오류·핵심**

좋은 자산·평균 operating path를 equity payoff에 직접 연결하거나, debt·integration·corporate action·timing의 joint distribution을 충분히 stress하지 않았다.

**재사용할 교훈**

Handset/marketing 가설은 '경쟁사 대비 handset/network 열위 지속'를 사전 반증조건으로 저장하고 사업·이벤트·가격 판정을 분리한다.

#### 4. FCF floor — 부분 적중 · 논지 비중 16%

**당시 주장**

$2bn 수준 FCF가 equity downside를 제한한다.

**당시 근거**

Nextel rebanding과 vocoder 문제로 생긴 network quality 악화가 이미 대부분 해결됐는데 customer perception과 sell-side가 이를 늦게 반영하고 있다고 봤다. QChat으로 iDEN 고객을 CDMA로 이전하고 새 handset·Dan Hesse 광고가 gross adds와 retention을 회복시킬 것이라 예상했다. 만약 turnaround가 늦어져도 2.5GHz/iDEN spectrum, long-distance fiber, Boost와 subscriber asset을 분리 매각하면 $12 이상 가치가 있다고 주장했다.

**이 주장이 성립하려면**

FCF가 반복 가능하고 debt가 안정

**사전 반증조건**

subscriber decline로 FCF trajectory 악화

**실제 결과**

2008 FCF는 나왔지만 주가 floor가 되지 못했다.

**정량적 괴리**

2.5GHz spectrum / $2.35/share / breakup floor / 후일 전략가치 확인되지만 당시 현금화 안 됨

**분석 오류·핵심**

핵심 causal chain은 실제 결과에서 확인됐다. 다만 그 성공이 증권 payoff의 원인이었는지는 별도 판정한다.

**재사용할 교훈**

FCF floor 가설은 'subscriber decline로 FCF trajectory 악화'를 사전 반증조건으로 저장하고 사업·이벤트·가격 판정을 분리한다.

#### 5. Breakup value — 실패 · 논지 비중 16%

**당시 주장**

spectrum·fiber·Boost·subs를 팔면 $12.44/share floor가 있다.

**당시 근거**

Nextel rebanding과 vocoder 문제로 생긴 network quality 악화가 이미 대부분 해결됐는데 customer perception과 sell-side가 이를 늦게 반영하고 있다고 봤다. QChat으로 iDEN 고객을 CDMA로 이전하고 새 handset·Dan Hesse 광고가 gross adds와 retention을 회복시킬 것이라 예상했다. 만약 turnaround가 늦어져도 2.5GHz/iDEN spectrum, long-distance fiber, Boost와 subscriber asset을 분리 매각하면 $12 이상 가치가 있다고 주장했다.

**이 주장이 성립하려면**

자산이 분리 가능하고 proceeds가 equity에 귀속

**사전 반증조건**

operating asset·debt·규제 때문에 분리 현금화 어려움

**실제 결과**

실제 주가는 breakup value보다 훨씬 아래로 갔다.

**정량적 괴리**

약 $6 부근에서 $12.44~17을 제시했지만 2008 금융위기와 Sprint 운영악화 속 주가는 $2 안팎까지 하락. 회복 thesis 실패.

**분석 오류·핵심**

좋은 자산·평균 operating path를 equity payoff에 직접 연결하거나, debt·integration·corporate action·timing의 joint distribution을 충분히 stress하지 않았다.

**재사용할 교훈**

Breakup value 가설은 'operating asset·debt·규제 때문에 분리 현금화 어려움'를 사전 반증조건으로 저장하고 사업·이벤트·가격 판정을 분리한다.

#### 6. $17 turnaround target — 실패 · 논지 비중 16%

**당시 주장**

33m subs·$8.3bn EBITDA에 7.5x면 거의 3배다.

**당시 근거**

Nextel rebanding과 vocoder 문제로 생긴 network quality 악화가 이미 대부분 해결됐는데 customer perception과 sell-side가 이를 늦게 반영하고 있다고 봤다. QChat으로 iDEN 고객을 CDMA로 이전하고 새 handset·Dan Hesse 광고가 gross adds와 retention을 회복시킬 것이라 예상했다. 만약 turnaround가 늦어져도 2.5GHz/iDEN spectrum, long-distance fiber, Boost와 subscriber asset을 분리 매각하면 $12 이상 가치가 있다고 주장했다.

**이 주장이 성립하려면**

1년 내 churn·ARPU 안정

**사전 반증조건**

turnaround 지연

**실제 결과**

목표가 미달.

**정량적 괴리**

약 $6 부근에서 $12.44~17을 제시했지만 2008 금융위기와 Sprint 운영악화 속 주가는 $2 안팎까지 하락. 회복 thesis 실패.

**분석 오류·핵심**

좋은 자산·평균 operating path를 equity payoff에 직접 연결하거나, debt·integration·corporate action·timing의 joint distribution을 충분히 stress하지 않았다.

**재사용할 교훈**

$17 turnaround target 가설은 'turnaround 지연'를 사전 반증조건으로 저장하고 사업·이벤트·가격 판정을 분리한다.

### 6. 실제 사업의 시간순 전개

turnaround는 예상 시점에 오지 않았다. Sprint는 2008년에도 $1.8bn 이상의 FCF를 기록했지만 postpaid subscriber losses와 브랜드·network 문제가 지속됐다. 이미 2007년 $29.7bn goodwill impairment가 있었고, asset-value 계산과 달리 spectrum·subscriber·long-distance 자산은 독립적으로 쉽게 분리·현금화되지 않았다. 주가는 $12~17이 아니라 $2 안팎으로 내려갔다.

### 7. 사업 결과와 가격 결과 분리

증권 결과는 약 $6 부근에서 $12.44~17을 제시했지만 2008 금융위기와 Sprint 운영악화 속 주가는 $2 안팎까지 하락. 회복 thesis 실패. 사업논지·촉매·valuation·corporate structure와 주가를 서로 다른 판정으로 저장한다.

### 8. 무엇을 잘 봤고 무엇을 놓쳤나

가장 큰 오류는 'operating turnaround'와 'breakup floor'를 독립적인 두 안전망처럼 더한 것이다. 실제로 고객이 빠지면 spectrum·network·brand의 standalone value도 낮아지고, 높은 debt와 지속 CapEx 때문에 asset sale proceeds가 기존 equity에 온전히 귀속되지 않는다. Spectrum은 가치가 있어도 operating network에 묶인 상태에서는 현금과 다르다.

### 9. 최초 검증·반증 신호와 회피 가능성

2008-05-12 — Sprint의 1Q08 subscriber losses와 약한 outlook이 확인되면서 customer perception lag가 아니라 실제 영업악화가 계속되고 있음이 드러났다. 이 시점에 원 valuation bridge를 다시 만들면 operating thesis와 security thesis 중 무엇이 살아있는지 구분할 수 있었다. 회피 가능성: 높음. turnaround thesis가 실패하면 breakup value가 자동으로 floor가 된다고 두지 말고 실제 buyer, 분리가능성, 담보·debt waterfall을 재평가했어야 한다.

### 10. 최종 판정·반사실·재사용 교훈

실패한 turnaround·asset-value trap. Telecom에서는 좋은 spectrum·좋은 콘텐츠·높은 FCF 하나만으로 equity floor를 만들지 않고, 실제 고객경제성·부채·corporate-action 귀속구조를 함께 stress해야 한다.

### 핵심 수치 — 당시 vs 실제

| 지표 | 글 당시 | VIC 기대 | 실제 | 판정 |
|---|---|---|---|---|
| 주가 | 약 $6 | $12.44~17 | $2 안팎까지 하락 | 실패 |
| FCF | 약 $2bn 예상 | 12.6% yield | FY2008 $1.8bn+ FCF | 숫자 일부 적중 |
| Postpaid | 33m 안정화 가정 | churn 정상화 | subscriber losses 지속 | 실패 |
| 2.5GHz spectrum | $2.35/share | breakup floor | 후일 전략가치 확인되지만 당시 현금화 안 됨 | 자산 통찰/증권 실패 |

### 사건 타임라인

| 시점 | 사건 | 논지에 대한 의미 |
|---|---|---|
| 2008-04-03 | VIC 아이디어 게시 | QChat·network turnaround 또는 breakup $12~17 Long |
| 2008-05-12 | 최초 핵심 검증·반증 신호 | Sprint의 1Q08 subscriber losses와 약한 outlook이 확인되면서 customer perception lag가 아니라 실제 영업악화가 계속되고 있음이 드러났다. |
| 2007-12-31 | Nextel 통합 손상 확인 | 2007년 대규모 goodwill impairment로 합병가치 훼손이 공식화 |
| 2016-12-31 | SoftBank-era operating/FCF 재평가 | 비용·network·subscriber economics가 과거와 달라졌는지 점검 |
| 2020-04-01 | Sprint 독립기업 종료 | T-Mobile merger 종결, 2.5GHz spectrum strategic value가 결합회사로 이전 |
| 2024-01-31 | 고정 사후평가 | Sprint 독립 equity는 소멸했으므로 원 security thesis는 merger 시점까지 평가 |

### Failure / Success Anatomy

- **근본 오류:** spectrum·balance-sheet 자산가치를 operating customer economics 또는 strategic exit probability와 잘못 연결
- **최초 검증·반증 신호:** 2008-05-12 — Sprint의 1Q08 subscriber losses와 약한 outlook이 확인되면서 customer perception lag가 아니라 실제 영업악화가 계속되고 있음이 드러났다.
- **당시 알 수 있었나:** 가입자 순증·churn·ARPU·service revenue·EBITDA·CapEx·FCF·gross debt·maturities·spectrum 사용·corporate-action 조건은 공시와 earnings에서 재검증 가능했다.
- **피할 수 있었나:** 높음. turnaround thesis가 실패하면 breakup value가 자동으로 floor가 된다고 두지 말고 실제 buyer, 분리가능성, 담보·debt waterfall을 재평가했어야 한다.
- **반사실 질문:** spectrum·segment business가 가치 있어도 integration, debt, corporate action 또는 security horizon이 반대로 움직이면 기존 보통주/스프레드의 payoff는 어떻게 달라지는가?
- **성공 패턴:** spectrum_optionality; fixed_cost_operating_leverage; event_driven_merger_arb; network_turnaround; strategic_buyer
- **실패·주의 패턴:** integration_failure; asset_value_trap; fcf_normalization_error; leverage; strategic_option_underpricing

### 주요 근거자료

- 1. VIC S 2008-04-03 원문 — Value Investors Club, 2008-04-03. 원 SQL description에서 당시 thesis·valuation·risk·catalyst·방향을 복원
- [2. Sprint 2006 Form 10-K](https://www.sec.gov/Archives/edgar/data/101830/000119312507040849/d10k.htm) — SEC, 2007-02-28. Nextel merger·Embarq spin·초기 통합상태 확인
- [3. Sprint Nextel 2007 Form 10-K](https://www.sec.gov/Archives/edgar/data/101830/000119312508043342/d10k.htm) — SEC, 2008-02-29. 4Q07 약 $29.7bn goodwill impairment·subscriber 문제 확인
- [4. Sprint FY2008 Results](https://www.sec.gov/Archives/edgar/data/101830/000119312509035054/dex991.htm) — Sprint/SEC, 2009-02-19. FY2008 free cash flow $1.8bn+ 확인
- [5. Sprint 2010 Form 10-K](https://www.sec.gov/Archives/edgar/data/101830/000119312511045676/d10k.htm) — SEC, 2011-02-24. 2010 operating cash flow·postpaid trends·historical shareholder performance 확인
- [6. Sprint 2014 Form 10-K](https://www.sec.gov/Archives/edgar/data/101830/000010183015000028/s-20150331x10k.htm) — SEC, 2015-05-26. network modernization·customer trends·SoftBank-era 상태 확인
- [7. Sprint FY2015 Results](https://newsroom.sprint.com/sprint-reports-fourth-quarter-and-fiscal-year-2015-results.htm) — Sprint, 2016-05-03. Adj EBITDA $8.1bn·postpaid net adds 1.2m+·churn 개선 확인
- [8. Sprint FY2016 Results](https://group.softbank/en/news/press/20170503) — Sprint/SoftBank, 2017-05-03. FY2016 adjusted FCF +$607m 등 turnaround cash flow 확인
- [9. Sprint FY2017 Results](https://newsroom.sprint.com/sprint-reports-fourth-quarter-and-fiscal-year-2017-results.htm) — Sprint, 2018-05-02. FY2017 adjusted FCF +$945m·두 해 연속 positive 확인
- [10. T-Mobile and Sprint amend merger terms](https://www.t-mobile.com/news/un-carrier/t-mobile-sprint-amend-business-combination-agreement) — T-Mobile, 2020-02-20. non-SoftBank Sprint 0.10256 exchange ratio 확인
- [11. T-Mobile completes merger with Sprint](https://www.t-mobile.com/news/un-carrier/t-mobile-sprint-one-company) — T-Mobile, 2020-04-01. 2020-04-01 종결 및 exchange ratio 확인
- 12. Sprint historical price context — Macrotrends/market history, 2020-04-01. VIC 당시 가격과 주요 저점·고점 교차검증


---

<!-- idea:118b462e-e831-4d7a-8f29-1b18b7b69631 -->
## 3. 2010-03-10 — 고비용·가입자 감소·FCF 압축 Short

### 결론부터

**종합판정: 운영논지 상당 부분 적중·전략적 rescue 미반영.** 부정적 operating forecast는 당시 Long 글들보다 현실에 가까웠다. 하지만 높은 부채의 약한 사업을 short할 때는 '회사가 계속 standalone으로 남는다'는 전제도 필요하다. spectrum과 nationwide footprint는 재무적 수익성이 나빠도 strategic buyer에게 가치가 있었다. 이 rescue optionality가 equity의 tail을 만들었다.

**주가·증권 결과:** 단기적으로 Sprint 주가는 2011년 $2대까지 내려 short 논지가 작동했지만, 2012 SoftBank 거래 발표 이후 생존·재자본화로 크게 반등. 파산/영구가치 훼손 thesis는 부분 실패.

**Thesis / Process 점수:** 8 / 8

### 1. 무슨 기업인가

Sprint는 미국 전국 단위 이동통신 사업자였으며 2005년 Nextel과 합병한 뒤 CDMA 기반 Sprint망과 iDEN 기반 Nextel망을 동시에 운영했다. 사업의 본질은 spectrum·기지국·backhaul·core network에 대규모 고정비를 선투자한 뒤 postpaid·prepaid 가입자의 월 서비스료에서 고객획득·단말기·network·sales 비용을 차감하는 구조였다. 2005~2010년 Sprint의 핵심 문제는 단순한 가입자 감소가 아니라 서로 다른 두 망과 브랜드를 합치는 과정에서 network quality·customer service·handset lineup이 동시에 악화되며 churn이 상승했다는 점이다. 반대로 가장 중요한 자산은 전국 단위 spectrum, 특히 2.5GHz 중대역이었다. 이 자산은 Sprint 자체 운영 아래에서는 충분히 monetization되지 못했지만 훗날 T-Mobile 합병에서 핵심 전략가치가 됐다. 따라서 Sprint를 분석할 때는 postpaid net adds, churn, ARPU, service revenue, adjusted EBITDA, network CapEx, 실제 FCF, handset financing/lease accounting, gross debt·maturities, spectrum의 사용가능성과 담보가치, 그리고 전략적 buyer 가능성을 함께 봐야 한다.

### 2. 산업 가치사슬과 돈의 흐름

Sprint의 돈 흐름은 '가입자수 × ARPU → service revenue → network·sales·device·customer-care 비용 → EBITDA → network CapEx·handset cash outflow·interest → FCF' 순이다. 무선망은 고정비가 커 가입자 증가가 margin을 크게 높일 수 있지만, 반대로 churn이 올라가면 같은 고정비를 더 적은 고객에게 배분해야 해 margin이 급격히 악화된다. 2010년대의 EIP·handset lease는 회계상 EBITDA와 실제 현금흐름을 더 복잡하게 만들었다. 단말기를 leasing하면 일부 비용이 당기 EBITDA에서 자산으로 이동할 수 있지만 현금은 먼저 나가기 때문에 EBITDA 개선과 FCF 개선을 동일시하면 안 된다. Spectrum은 매우 큰 자산가치를 가질 수 있지만 operating network에 묶여 있거나 FCC ownership cap·담보·고객망 제약이 있으면 liquidation value를 즉시 equity로 전환할 수 없다.

### 3. 경쟁우위·경쟁구도·핵심 지표

Sprint의 경쟁우위 후보는 전국망, 2.5GHz spectrum depth, 대규모 customer base와 SoftBank의 자본이었다. 그러나 Verizon·AT&T·T-Mobile 대비 network perception, churn, distribution, handset portfolio, balance sheet가 약했고, 특히 Nextel 통합 실패가 수년간 브랜드와 economics를 훼손했다. 2014 이후 network modernization과 cost cutting은 실제 개선을 만들었지만 높은 부채와 낮은 scale efficiency는 여전히 제약이었다. 이 기업의 역사는 '좋은 spectrum = 좋은 독립기업'이 아님을 보여준다. 핵심은 spectrum을 실제 coverage/capacity·customer retention·FCF로 전환할 운영능력과 자본구조다.

### 4. 당시 VIC 원문과 핵심 숫자

미국 wireless가 성숙해지고 가격경쟁이 강해지는 가운데 Sprint는 브랜드·network·cost structure·leverage 모두 열위라고 봤다. 가입자와 ARPU가 동시에 내려가면 높은 고정비 때문에 EBITDA margin이 급락하고 CapEx·interest를 뺀 FCF가 거의 사라질 수 있다고 주장했다. 특히 경쟁사가 안정적인데 Sprint만 구조적으로 share를 잃는다는 점을 short edge로 봤다.

### 5. 밸류에이션과 기대수익의 연결

가입자 -3%/년, ARPU -2~3%, churn +10bp, EBITDA margin 20%→13%를 가정. 2010 EBITDA $5.7bn, 2011 $4.6bn; FCF/share 약 $0.60→$0.15. 약 $17bn net debt와 만기 부담을 근거로 2년 30~40% downside를 제시. 사후에는 subscriber/churn/ARPU 또는 segment earnings → EBITDA → CapEx·interest → FCF → debt·corporate action → 기존 보통주 또는 merger spread payoff 순으로 다시 연결해 검증했다.

### 투자논지를 구성한 핵심 주장

#### 1. Mature wireless — 적중 · 논지 비중 18%

**당시 주장**

성숙시장과 가격경쟁이 Sprint ARPU·share를 압박한다.

**당시 근거**

미국 wireless가 성숙해지고 가격경쟁이 강해지는 가운데 Sprint는 브랜드·network·cost structure·leverage 모두 열위라고 봤다. 가입자와 ARPU가 동시에 내려가면 높은 고정비 때문에 EBITDA margin이 급락하고 CapEx·interest를 뺀 FCF가 거의 사라질 수 있다고 주장했다. 특히 경쟁사가 안정적인데 Sprint만 구조적으로 share를 잃는다는 점을 short edge로 봤다.

**이 주장이 성립하려면**

경쟁사가 더 강한 network/brand 유지

**사전 반증조건**

시장성장·Sprint share 회복

**실제 결과**

Sprint의 상대적 약세가 지속됐다.

**정량적 괴리**

가입자 / 연 -3% 가정 / 지속 감소 / postpaid weakness 지속

**분석 오류·핵심**

핵심 causal chain은 실제 결과에서 확인됐다. 다만 그 성공이 증권 payoff의 원인이었는지는 별도 판정한다.

**재사용할 교훈**

Mature wireless 가설은 '시장성장·Sprint share 회복'를 사전 반증조건으로 저장하고 사업·이벤트·가격 판정을 분리한다.

#### 2. Subscriber decline — 적중 · 논지 비중 18%

**당시 주장**

가입자가 연 3%가량 감소한다.

**당시 근거**

미국 wireless가 성숙해지고 가격경쟁이 강해지는 가운데 Sprint는 브랜드·network·cost structure·leverage 모두 열위라고 봤다. 가입자와 ARPU가 동시에 내려가면 높은 고정비 때문에 EBITDA margin이 급락하고 CapEx·interest를 뺀 FCF가 거의 사라질 수 있다고 주장했다. 특히 경쟁사가 안정적인데 Sprint만 구조적으로 share를 잃는다는 점을 short edge로 봤다.

**이 주장이 성립하려면**

churn이 gross adds보다 높음

**사전 반증조건**

net adds 회복

**실제 결과**

postpaid weakness가 계속됐다.

**정량적 괴리**

2010 CFO / FCF 압축 예상 / 낮은 cash conversion / operating cash flow 약 $4.8bn

**분석 오류·핵심**

핵심 causal chain은 실제 결과에서 확인됐다. 다만 그 성공이 증권 payoff의 원인이었는지는 별도 판정한다.

**재사용할 교훈**

Subscriber decline 가설은 'net adds 회복'를 사전 반증조건으로 저장하고 사업·이벤트·가격 판정을 분리한다.

#### 3. Margin compression — 방향 적중 · 논지 비중 16%

**당시 주장**

20% margin이 13% 방향으로 떨어질 수 있다.

**당시 근거**

미국 wireless가 성숙해지고 가격경쟁이 강해지는 가운데 Sprint는 브랜드·network·cost structure·leverage 모두 열위라고 봤다. 가입자와 ARPU가 동시에 내려가면 높은 고정비 때문에 EBITDA margin이 급락하고 CapEx·interest를 뺀 FCF가 거의 사라질 수 있다고 주장했다. 특히 경쟁사가 안정적인데 Sprint만 구조적으로 share를 잃는다는 점을 short edge로 봤다.

**이 주장이 성립하려면**

고정비가 revenue보다 느리게 줄어듦

**사전 반증조건**

비용절감이 revenue decline 상쇄

**실제 결과**

수익성 압박은 현실이었다.

**정량적 괴리**

주가 / 약 $4 / 2년 -30~40% / 2011 $2대

**분석 오류·핵심**

핵심 causal chain은 실제 결과에서 확인됐다. 다만 그 성공이 증권 payoff의 원인이었는지는 별도 판정한다.

**재사용할 교훈**

Margin compression 가설은 '비용절감이 revenue decline 상쇄'를 사전 반증조건으로 저장하고 사업·이벤트·가격 판정을 분리한다.

#### 4. FCF erosion — 부분 적중 · 논지 비중 16%

**당시 주장**

CapEx·interest 후 FCF가 급감한다.

**당시 근거**

미국 wireless가 성숙해지고 가격경쟁이 강해지는 가운데 Sprint는 브랜드·network·cost structure·leverage 모두 열위라고 봤다. 가입자와 ARPU가 동시에 내려가면 높은 고정비 때문에 EBITDA margin이 급락하고 CapEx·interest를 뺀 FCF가 거의 사라질 수 있다고 주장했다. 특히 경쟁사가 안정적인데 Sprint만 구조적으로 share를 잃는다는 점을 short edge로 봤다.

**이 주장이 성립하려면**

network investment와 debt service 지속

**사전 반증조건**

대규모 비용절감·capex 감소

**실제 결과**

cash flow는 약했지만 완전 소멸까지는 아니었다.

**정량적 괴리**

전략적 rescue / 낮게 평가 / standalone distress / 2012 SoftBank 거래 발표

**분석 오류·핵심**

핵심 causal chain은 실제 결과에서 확인됐다. 다만 그 성공이 증권 payoff의 원인이었는지는 별도 판정한다.

**재사용할 교훈**

FCF erosion 가설은 '대규모 비용절감·capex 감소'를 사전 반증조건으로 저장하고 사업·이벤트·가격 판정을 분리한다.

#### 5. Debt distress — 실패 · 논지 비중 16%

**당시 주장**

$17bn net debt·maturities가 equity downside를 키운다.

**당시 근거**

미국 wireless가 성숙해지고 가격경쟁이 강해지는 가운데 Sprint는 브랜드·network·cost structure·leverage 모두 열위라고 봤다. 가입자와 ARPU가 동시에 내려가면 높은 고정비 때문에 EBITDA margin이 급락하고 CapEx·interest를 뺀 FCF가 거의 사라질 수 있다고 주장했다. 특히 경쟁사가 안정적인데 Sprint만 구조적으로 share를 잃는다는 점을 short edge로 봤다.

**이 주장이 성립하려면**

외부 자본·buyer 부재

**사전 반증조건**

전략적 recapitalization

**실제 결과**

SoftBank가 자본구조를 바꿨다.

**정량적 괴리**

단기적으로 Sprint 주가는 2011년 $2대까지 내려 short 논지가 작동했지만, 2012 SoftBank 거래 발표 이후 생존·재자본화로 크게 반등. 파산/영구가치 훼손 thesis는 부분 실패.

**분석 오류·핵심**

좋은 자산·평균 operating path를 equity payoff에 직접 연결하거나, debt·integration·corporate action·timing의 joint distribution을 충분히 stress하지 않았다.

**재사용할 교훈**

Debt distress 가설은 '전략적 recapitalization'를 사전 반증조건으로 저장하고 사업·이벤트·가격 판정을 분리한다.

#### 6. 30~40% downside — 가격 적중·경로 제한 · 논지 비중 16%

**당시 주장**

2년 안에 주가가 30~40% 하락한다.

**당시 근거**

미국 wireless가 성숙해지고 가격경쟁이 강해지는 가운데 Sprint는 브랜드·network·cost structure·leverage 모두 열위라고 봤다. 가입자와 ARPU가 동시에 내려가면 높은 고정비 때문에 EBITDA margin이 급락하고 CapEx·interest를 뺀 FCF가 거의 사라질 수 있다고 주장했다. 특히 경쟁사가 안정적인데 Sprint만 구조적으로 share를 잃는다는 점을 short edge로 봤다.

**이 주장이 성립하려면**

standalone thesis 유지

**사전 반증조건**

strategic bid

**실제 결과**

2011 하락으로 단기 달성 후 반등 tail 발생.

**정량적 괴리**

단기적으로 Sprint 주가는 2011년 $2대까지 내려 short 논지가 작동했지만, 2012 SoftBank 거래 발표 이후 생존·재자본화로 크게 반등. 파산/영구가치 훼손 thesis는 부분 실패.

**분석 오류·핵심**

핵심 causal chain은 실제 결과에서 확인됐다. 다만 그 성공이 증권 payoff의 원인이었는지는 별도 판정한다.

**재사용할 교훈**

30~40% downside 가설은 'strategic bid'를 사전 반증조건으로 저장하고 사업·이벤트·가격 판정을 분리한다.

### 6. 실제 사업의 시간순 전개

2010 operating cash flow는 약 $4.8bn이었지만 postpaid subscriber decline과 weak economics는 지속됐다. 주가는 2011년 $2대로 내려 단기 short는 유효했다. 그러나 Sprint는 파산하지 않았고 2012년 SoftBank가 대규모 자본투입·지분취득을 발표해 2013년 거래를 완료했다. 즉 standalone cash-flow 약점은 맞았지만 strategic capital rescue와 spectrum optionality를 충분히 반영하지 못했다.

### 7. 사업 결과와 가격 결과 분리

증권 결과는 단기적으로 Sprint 주가는 2011년 $2대까지 내려 short 논지가 작동했지만, 2012 SoftBank 거래 발표 이후 생존·재자본화로 크게 반등. 파산/영구가치 훼손 thesis는 부분 실패. 사업논지·촉매·valuation·corporate structure와 주가를 서로 다른 판정으로 저장한다.

### 8. 무엇을 잘 봤고 무엇을 놓쳤나

부정적 operating forecast는 당시 Long 글들보다 현실에 가까웠다. 하지만 높은 부채의 약한 사업을 short할 때는 '회사가 계속 standalone으로 남는다'는 전제도 필요하다. spectrum과 nationwide footprint는 재무적 수익성이 나빠도 strategic buyer에게 가치가 있었다. 이 rescue optionality가 equity의 tail을 만들었다.

### 9. 최초 검증·반증 신호와 회피 가능성

2012-10-15 — SoftBank가 Sprint에 약 $20bn 규모 투자·인수계획을 발표하면서 standalone deterioration만으로 equity payoff를 계산한 Short 논지가 구조적으로 바뀌었다. 이 시점에 원 valuation bridge를 다시 만들면 operating thesis와 security thesis 중 무엇이 살아있는지 구분할 수 있었다. 회피 가능성: 중간. 2011년 주가하락으로 핵심 short가 작동한 뒤 strategic buyer 가능성이 커졌을 때 이익을 실현하거나 tail risk를 재평가했어야 한다.

### 10. 최종 판정·반사실·재사용 교훈

운영논지 상당 부분 적중·전략적 rescue 미반영. Telecom에서는 좋은 spectrum·좋은 콘텐츠·높은 FCF 하나만으로 equity floor를 만들지 않고, 실제 고객경제성·부채·corporate-action 귀속구조를 함께 stress해야 한다.

### 핵심 수치 — 당시 vs 실제

| 지표 | 글 당시 | VIC 기대 | 실제 | 판정 |
|---|---|---|---|---|
| 가입자 | 연 -3% 가정 | 지속 감소 | postpaid weakness 지속 | 적중 |
| 2010 CFO | FCF 압축 예상 | 낮은 cash conversion | operating cash flow 약 $4.8bn | 부분 |
| 주가 | 약 $4 | 2년 -30~40% | 2011 $2대 | 단기 적중 |
| 전략적 rescue | 낮게 평가 | standalone distress | 2012 SoftBank 거래 발표 | 누락 |

### 사건 타임라인

| 시점 | 사건 | 논지에 대한 의미 |
|---|---|---|
| 2010-03-10 | VIC 아이디어 게시 | 고비용·가입자 감소·FCF 압축 Short |
| 2012-10-15 | 최초 핵심 검증·반증 신호 | SoftBank가 Sprint에 약 $20bn 규모 투자·인수계획을 발표하면서 standalone deterioration만으로 equity payoff를 계산한 Short 논지가 구조적으로 바뀌었다. |
| 2007-12-31 | Nextel 통합 손상 확인 | 2007년 대규모 goodwill impairment로 합병가치 훼손이 공식화 |
| 2016-12-31 | SoftBank-era operating/FCF 재평가 | 비용·network·subscriber economics가 과거와 달라졌는지 점검 |
| 2020-04-01 | Sprint 독립기업 종료 | T-Mobile merger 종결, 2.5GHz spectrum strategic value가 결합회사로 이전 |
| 2024-01-31 | 고정 사후평가 | Sprint 독립 equity는 소멸했으므로 원 security thesis는 merger 시점까지 평가 |

### Failure / Success Anatomy

- **근본 오류:** 핵심 causal chain은 상당 부분 맞았으나 operating success·event success·security payoff를 계속 분리해야 함
- **최초 검증·반증 신호:** 2012-10-15 — SoftBank가 Sprint에 약 $20bn 규모 투자·인수계획을 발표하면서 standalone deterioration만으로 equity payoff를 계산한 Short 논지가 구조적으로 바뀌었다.
- **당시 알 수 있었나:** 가입자 순증·churn·ARPU·service revenue·EBITDA·CapEx·FCF·gross debt·maturities·spectrum 사용·corporate-action 조건은 공시와 earnings에서 재검증 가능했다.
- **피할 수 있었나:** 중간. 2011년 주가하락으로 핵심 short가 작동한 뒤 strategic buyer 가능성이 커졌을 때 이익을 실현하거나 tail risk를 재평가했어야 한다.
- **반사실 질문:** spectrum·segment business가 가치 있어도 integration, debt, corporate action 또는 security horizon이 반대로 움직이면 기존 보통주/스프레드의 payoff는 어떻게 달라지는가?
- **성공 패턴:** spectrum_optionality; fixed_cost_operating_leverage; event_driven_merger_arb; network_turnaround; strategic_buyer
- **실패·주의 패턴:** integration_failure; asset_value_trap; fcf_normalization_error; leverage; strategic_option_underpricing

### 주요 근거자료

- 1. VIC S 2010-03-10 원문 — Value Investors Club, 2010-03-10. 원 SQL description에서 당시 thesis·valuation·risk·catalyst·방향을 복원
- [2. Sprint 2006 Form 10-K](https://www.sec.gov/Archives/edgar/data/101830/000119312507040849/d10k.htm) — SEC, 2007-02-28. Nextel merger·Embarq spin·초기 통합상태 확인
- [3. Sprint Nextel 2007 Form 10-K](https://www.sec.gov/Archives/edgar/data/101830/000119312508043342/d10k.htm) — SEC, 2008-02-29. 4Q07 약 $29.7bn goodwill impairment·subscriber 문제 확인
- [4. Sprint FY2008 Results](https://www.sec.gov/Archives/edgar/data/101830/000119312509035054/dex991.htm) — Sprint/SEC, 2009-02-19. FY2008 free cash flow $1.8bn+ 확인
- [5. Sprint 2010 Form 10-K](https://www.sec.gov/Archives/edgar/data/101830/000119312511045676/d10k.htm) — SEC, 2011-02-24. 2010 operating cash flow·postpaid trends·historical shareholder performance 확인
- [6. Sprint 2014 Form 10-K](https://www.sec.gov/Archives/edgar/data/101830/000010183015000028/s-20150331x10k.htm) — SEC, 2015-05-26. network modernization·customer trends·SoftBank-era 상태 확인
- [7. Sprint FY2015 Results](https://newsroom.sprint.com/sprint-reports-fourth-quarter-and-fiscal-year-2015-results.htm) — Sprint, 2016-05-03. Adj EBITDA $8.1bn·postpaid net adds 1.2m+·churn 개선 확인
- [8. Sprint FY2016 Results](https://group.softbank/en/news/press/20170503) — Sprint/SoftBank, 2017-05-03. FY2016 adjusted FCF +$607m 등 turnaround cash flow 확인
- [9. Sprint FY2017 Results](https://newsroom.sprint.com/sprint-reports-fourth-quarter-and-fiscal-year-2017-results.htm) — Sprint, 2018-05-02. FY2017 adjusted FCF +$945m·두 해 연속 positive 확인
- [10. T-Mobile and Sprint amend merger terms](https://www.t-mobile.com/news/un-carrier/t-mobile-sprint-amend-business-combination-agreement) — T-Mobile, 2020-02-20. non-SoftBank Sprint 0.10256 exchange ratio 확인
- [11. T-Mobile completes merger with Sprint](https://www.t-mobile.com/news/un-carrier/t-mobile-sprint-one-company) — T-Mobile, 2020-04-01. 2020-04-01 종결 및 exchange ratio 확인
- 12. Sprint historical price context — Macrotrends/market history, 2020-04-01. VIC 당시 가격과 주요 저점·고점 교차검증


---

<!-- idea:ea0293cb-7f3a-4085-9505-48fc203b6b6b -->
## 4. 2014-08-06 — SoftBank·2.5GHz spectrum·Claure turnaround Long

### 결론부터

**종합판정: 자산·운영개선 통찰 적중·목표가/시간 부분 실패.** 이 글은 2014 시장이 '나쁜 회사'와 '좋은 spectrum asset'을 지나치게 동일시한 점을 잘 봤고, SoftBank 이후 비용·network 개선도 맞혔다. 반면 excess spectrum을 주당 $3~4로 바로 더한 뒤 'very little downside'라고 한 부분은 debt·CapEx·monetization timing을 과소평가했다. 자산가치가 높아도 standalone equity에서 실현되기까지 시간이 오래 걸릴 수 있다.

**주가·증권 결과:** 약 $6에서 FY2017 고점 $9.65까지 상승했지만 'near term $10+, 장기 2~3x'는 평가 horizon 내 미달.

**Thesis / Process 점수:** 5.8 / 6.2

### 1. 무슨 기업인가

Sprint는 미국 전국 단위 이동통신 사업자였으며 2005년 Nextel과 합병한 뒤 CDMA 기반 Sprint망과 iDEN 기반 Nextel망을 동시에 운영했다. 사업의 본질은 spectrum·기지국·backhaul·core network에 대규모 고정비를 선투자한 뒤 postpaid·prepaid 가입자의 월 서비스료에서 고객획득·단말기·network·sales 비용을 차감하는 구조였다. 2005~2010년 Sprint의 핵심 문제는 단순한 가입자 감소가 아니라 서로 다른 두 망과 브랜드를 합치는 과정에서 network quality·customer service·handset lineup이 동시에 악화되며 churn이 상승했다는 점이다. 반대로 가장 중요한 자산은 전국 단위 spectrum, 특히 2.5GHz 중대역이었다. 이 자산은 Sprint 자체 운영 아래에서는 충분히 monetization되지 못했지만 훗날 T-Mobile 합병에서 핵심 전략가치가 됐다. 따라서 Sprint를 분석할 때는 postpaid net adds, churn, ARPU, service revenue, adjusted EBITDA, network CapEx, 실제 FCF, handset financing/lease accounting, gross debt·maturities, spectrum의 사용가능성과 담보가치, 그리고 전략적 buyer 가능성을 함께 봐야 한다.

### 2. 산업 가치사슬과 돈의 흐름

Sprint의 돈 흐름은 '가입자수 × ARPU → service revenue → network·sales·device·customer-care 비용 → EBITDA → network CapEx·handset cash outflow·interest → FCF' 순이다. 무선망은 고정비가 커 가입자 증가가 margin을 크게 높일 수 있지만, 반대로 churn이 올라가면 같은 고정비를 더 적은 고객에게 배분해야 해 margin이 급격히 악화된다. 2010년대의 EIP·handset lease는 회계상 EBITDA와 실제 현금흐름을 더 복잡하게 만들었다. 단말기를 leasing하면 일부 비용이 당기 EBITDA에서 자산으로 이동할 수 있지만 현금은 먼저 나가기 때문에 EBITDA 개선과 FCF 개선을 동일시하면 안 된다. Spectrum은 매우 큰 자산가치를 가질 수 있지만 operating network에 묶여 있거나 FCC ownership cap·담보·고객망 제약이 있으면 liquidation value를 즉시 equity로 전환할 수 없다.

### 3. 경쟁우위·경쟁구도·핵심 지표

Sprint의 경쟁우위 후보는 전국망, 2.5GHz spectrum depth, 대규모 customer base와 SoftBank의 자본이었다. 그러나 Verizon·AT&T·T-Mobile 대비 network perception, churn, distribution, handset portfolio, balance sheet가 약했고, 특히 Nextel 통합 실패가 수년간 브랜드와 economics를 훼손했다. 2014 이후 network modernization과 cost cutting은 실제 개선을 만들었지만 높은 부채와 낮은 scale efficiency는 여전히 제약이었다. 이 기업의 역사는 '좋은 spectrum = 좋은 독립기업'이 아님을 보여준다. 핵심은 spectrum을 실제 coverage/capacity·customer retention·FCF로 전환할 운영능력과 자본구조다.

### 4. 당시 VIC 원문과 핵심 숫자

T-Mobile 인수 시도가 무산되고 Dan Hesse가 교체된 직후, 시장은 Sprint의 과거 실패만 반영하고 SoftBank·Marcelo Claure 운영개선과 excess spectrum을 거의 가치에 넣지 않는다고 봤다. 45.7bn MHz-POPs의 사용되지 않는 spectrum과 2.5GHz depth가 향후 Spark/network advantage를 만들고, postpaid net adds가 2015년부터 플러스로 돌아서면 $10 이상이 가능하다고 주장했다.

### 5. 밸류에이션과 기대수익의 연결

Baseline EBITDA 약 $4bn, EV 약 $51.5bn, net debt 약 $27.5bn. 사용되지 않는 2.5GHz 등 excess spectrum을 $12~15bn($3~4/share)로 보고 $10+ near-term, 장기 2~3배를 제시. 사후에는 subscriber/churn/ARPU 또는 segment earnings → EBITDA → CapEx·interest → FCF → debt·corporate action → 기존 보통주 또는 merger spread payoff 순으로 다시 연결해 검증했다.

### 투자논지를 구성한 핵심 주장

#### 1. SoftBank/management — 적중 · 논지 비중 18%

**당시 주장**

SoftBank와 Claure가 Hesse 시대보다 실행력을 높인다.

**당시 근거**

T-Mobile 인수 시도가 무산되고 Dan Hesse가 교체된 직후, 시장은 Sprint의 과거 실패만 반영하고 SoftBank·Marcelo Claure 운영개선과 excess spectrum을 거의 가치에 넣지 않는다고 봤다. 45.7bn MHz-POPs의 사용되지 않는 spectrum과 2.5GHz depth가 향후 Spark/network advantage를 만들고, postpaid net adds가 2015년부터 플러스로 돌아서면 $10 이상이 가능하다고 주장했다.

**이 주장이 성립하려면**

비용·network·sales 개선

**사전 반증조건**

운영지표 개선 부재

**실제 결과**

FY2015~17 EBITDA·FCF가 개선됐다.

**정량적 괴리**

주가 / $5.95~6 / near term $10+ / FY2017 high $9.65

**분석 오류·핵심**

핵심 causal chain은 실제 결과에서 확인됐다. 다만 그 성공이 증권 payoff의 원인이었는지는 별도 판정한다.

**재사용할 교훈**

SoftBank/management 가설은 '운영지표 개선 부재'를 사전 반증조건으로 저장하고 사업·이벤트·가격 판정을 분리한다.

#### 2. Network turnaround — 적중 · 논지 비중 18%

**당시 주장**

Spark·network modernization이 고객경험을 개선한다.

**당시 근거**

T-Mobile 인수 시도가 무산되고 Dan Hesse가 교체된 직후, 시장은 Sprint의 과거 실패만 반영하고 SoftBank·Marcelo Claure 운영개선과 excess spectrum을 거의 가치에 넣지 않는다고 봤다. 45.7bn MHz-POPs의 사용되지 않는 spectrum과 2.5GHz depth가 향후 Spark/network advantage를 만들고, postpaid net adds가 2015년부터 플러스로 돌아서면 $10 이상이 가능하다고 주장했다.

**이 주장이 성립하려면**

coverage/capacity가 churn/net adds로 연결

**사전 반증조건**

network perception 열위 지속

**실제 결과**

churn과 postpaid trends가 개선됐다.

**정량적 괴리**

Adjusted EBITDA / 약 $4bn baseline / 강한 개선 / FY2015 $8.1bn

**분석 오류·핵심**

핵심 causal chain은 실제 결과에서 확인됐다. 다만 그 성공이 증권 payoff의 원인이었는지는 별도 판정한다.

**재사용할 교훈**

Network turnaround 가설은 'network perception 열위 지속'를 사전 반증조건으로 저장하고 사업·이벤트·가격 판정을 분리한다.

#### 3. Postpaid recovery — 강한 적중 · 논지 비중 16%

**당시 주장**

2015부터 postpaid net adds가 플러스로 돌아선다.

**당시 근거**

T-Mobile 인수 시도가 무산되고 Dan Hesse가 교체된 직후, 시장은 Sprint의 과거 실패만 반영하고 SoftBank·Marcelo Claure 운영개선과 excess spectrum을 거의 가치에 넣지 않는다고 봤다. 45.7bn MHz-POPs의 사용되지 않는 spectrum과 2.5GHz depth가 향후 Spark/network advantage를 만들고, postpaid net adds가 2015년부터 플러스로 돌아서면 $10 이상이 가능하다고 주장했다.

**이 주장이 성립하려면**

gross adds와 retention 동시개선

**사전 반증조건**

순감 지속

**실제 결과**

FY2015 postpaid net adds 1.2m+로 강한 적중.

**정량적 괴리**

Adjusted FCF / negative / turnaround 후 positive / FY2016 +$607m; FY2017 +$945m

**분석 오류·핵심**

핵심 causal chain은 실제 결과에서 확인됐다. 다만 그 성공이 증권 payoff의 원인이었는지는 별도 판정한다.

**재사용할 교훈**

Postpaid recovery 가설은 '순감 지속'를 사전 반증조건으로 저장하고 사업·이벤트·가격 판정을 분리한다.

#### 4. Excess spectrum — 적중 · 논지 비중 16%

**당시 주장**

$12~15bn excess spectrum이 시장에서 무시된다.

**당시 근거**

T-Mobile 인수 시도가 무산되고 Dan Hesse가 교체된 직후, 시장은 Sprint의 과거 실패만 반영하고 SoftBank·Marcelo Claure 운영개선과 excess spectrum을 거의 가치에 넣지 않는다고 봤다. 45.7bn MHz-POPs의 사용되지 않는 spectrum과 2.5GHz depth가 향후 Spark/network advantage를 만들고, postpaid net adds가 2015년부터 플러스로 돌아서면 $10 이상이 가능하다고 주장했다.

**이 주장이 성립하려면**

실제 monetization·strategic value 존재

**사전 반증조건**

규제·사용제약으로 가치 실현 불가

**실제 결과**

후일 T-Mobile에게 매우 중요한 2.5GHz 자산이 됐다.

**정량적 괴리**

Spectrum / $12~15bn excess / equity upside / T-Mobile 합병의 핵심 2.5GHz 자산

**분석 오류·핵심**

핵심 causal chain은 실제 결과에서 확인됐다. 다만 그 성공이 증권 payoff의 원인이었는지는 별도 판정한다.

**재사용할 교훈**

Excess spectrum 가설은 '규제·사용제약으로 가치 실현 불가'를 사전 반증조건으로 저장하고 사업·이벤트·가격 판정을 분리한다.

#### 5. Downside — 과도한 낙관 · 논지 비중 16%

**당시 주장**

cash/liquidity와 spectrum 때문에 downside가 매우 작다.

**당시 근거**

T-Mobile 인수 시도가 무산되고 Dan Hesse가 교체된 직후, 시장은 Sprint의 과거 실패만 반영하고 SoftBank·Marcelo Claure 운영개선과 excess spectrum을 거의 가치에 넣지 않는다고 봤다. 45.7bn MHz-POPs의 사용되지 않는 spectrum과 2.5GHz depth가 향후 Spark/network advantage를 만들고, postpaid net adds가 2015년부터 플러스로 돌아서면 $10 이상이 가능하다고 주장했다.

**이 주장이 성립하려면**

maturities 관리·FCF 개선

**사전 반증조건**

cash burn·debt stress

**실제 결과**

운영개선 전까지 높은 변동성과 downside가 존재했다.

**정량적 괴리**

약 $6에서 FY2017 고점 $9.65까지 상승했지만 'near term $10+, 장기 2~3x'는 평가 horizon 내 미달.

**분석 오류·핵심**

좋은 자산·평균 operating path를 equity payoff에 직접 연결하거나, debt·integration·corporate action·timing의 joint distribution을 충분히 stress하지 않았다.

**재사용할 교훈**

Downside 가설은 'cash burn·debt stress'를 사전 반증조건으로 저장하고 사업·이벤트·가격 판정을 분리한다.

#### 6. $10+/2~3x — 부분 · 논지 비중 16%

**당시 주장**

turnaround+spectrum으로 $10 이상, 장기 2~3배다.

**당시 근거**

T-Mobile 인수 시도가 무산되고 Dan Hesse가 교체된 직후, 시장은 Sprint의 과거 실패만 반영하고 SoftBank·Marcelo Claure 운영개선과 excess spectrum을 거의 가치에 넣지 않는다고 봤다. 45.7bn MHz-POPs의 사용되지 않는 spectrum과 2.5GHz depth가 향후 Spark/network advantage를 만들고, postpaid net adds가 2015년부터 플러스로 돌아서면 $10 이상이 가능하다고 주장했다.

**이 주장이 성립하려면**

운영개선과 rerating이 빠르게 동시발생

**사전 반증조건**

monetization 지연

**실제 결과**

$9.65 고점으로 near-term target 근접, 장기 2~3x 미달.

**정량적 괴리**

약 $6에서 FY2017 고점 $9.65까지 상승했지만 'near term $10+, 장기 2~3x'는 평가 horizon 내 미달.

**분석 오류·핵심**

핵심 causal chain은 실제 결과에서 확인됐다. 다만 그 성공이 증권 payoff의 원인이었는지는 별도 판정한다.

**재사용할 교훈**

$10+/2~3x 가설은 'monetization 지연'를 사전 반증조건으로 저장하고 사업·이벤트·가격 판정을 분리한다.

### 6. 실제 사업의 시간순 전개

운영개선은 실제 나타났다. FY2015 adjusted EBITDA는 약 $8.1bn으로 36% 증가했고 postpaid net adds는 1.2m+, churn도 개선됐다. FY2016 adjusted FCF는 +$607m, FY2017은 +$945m으로 2년 연속 positive가 됐다. 주가도 FY2017 고점 $9.65까지 회복했다. 그러나 near-term $10+와 장기 2~3x는 충분히 달성되지 않았고, spectrum의 최대 가치는 결국 Sprint standalone보다 T-Mobile 합병에서 실현됐다.

### 7. 사업 결과와 가격 결과 분리

증권 결과는 약 $6에서 FY2017 고점 $9.65까지 상승했지만 'near term $10+, 장기 2~3x'는 평가 horizon 내 미달. 사업논지·촉매·valuation·corporate structure와 주가를 서로 다른 판정으로 저장한다.

### 8. 무엇을 잘 봤고 무엇을 놓쳤나

이 글은 2014 시장이 '나쁜 회사'와 '좋은 spectrum asset'을 지나치게 동일시한 점을 잘 봤고, SoftBank 이후 비용·network 개선도 맞혔다. 반면 excess spectrum을 주당 $3~4로 바로 더한 뒤 'very little downside'라고 한 부분은 debt·CapEx·monetization timing을 과소평가했다. 자산가치가 높아도 standalone equity에서 실현되기까지 시간이 오래 걸릴 수 있다.

### 9. 최초 검증·반증 신호와 회피 가능성

2016-05-03 — FY2015 결과에서 adjusted EBITDA $8.1bn, 1.2m+ postpaid net adds와 churn 개선이 확인되며 turnaround가 숫자로 검증됐다. 이 시점에 원 valuation bridge를 다시 만들면 operating thesis와 security thesis 중 무엇이 살아있는지 구분할 수 있었다. 회피 가능성: 핵심 long은 일부 성공했다. 다만 $10을 못 넘는 기간이 길어질수록 spectrum value의 직접 monetization 가능성과 debt를 다시 평가해 장기 2~3x 기대는 낮췄어야 한다.

### 10. 최종 판정·반사실·재사용 교훈

자산·운영개선 통찰 적중·목표가/시간 부분 실패. Telecom에서는 좋은 spectrum·좋은 콘텐츠·높은 FCF 하나만으로 equity floor를 만들지 않고, 실제 고객경제성·부채·corporate-action 귀속구조를 함께 stress해야 한다.

### 핵심 수치 — 당시 vs 실제

| 지표 | 글 당시 | VIC 기대 | 실제 | 판정 |
|---|---|---|---|---|
| 주가 | $5.95~6 | near term $10+ | FY2017 high $9.65 | 부분 성공 |
| Adjusted EBITDA | 약 $4bn baseline | 강한 개선 | FY2015 $8.1bn | 강한 적중 |
| Adjusted FCF | negative | turnaround 후 positive | FY2016 +$607m; FY2017 +$945m | 적중 |
| Spectrum | $12~15bn excess | equity upside | T-Mobile 합병의 핵심 2.5GHz 자산 | 자산 통찰 적중 |

### 사건 타임라인

| 시점 | 사건 | 논지에 대한 의미 |
|---|---|---|
| 2014-08-06 | VIC 아이디어 게시 | SoftBank·2.5GHz spectrum·Claure turnaround Long |
| 2016-05-03 | 최초 핵심 검증·반증 신호 | FY2015 결과에서 adjusted EBITDA $8.1bn, 1.2m+ postpaid net adds와 churn 개선이 확인되며 turnaround가 숫자로 검증됐다. |
| 2007-12-31 | Nextel 통합 손상 확인 | 2007년 대규모 goodwill impairment로 합병가치 훼손이 공식화 |
| 2016-12-31 | SoftBank-era operating/FCF 재평가 | 비용·network·subscriber economics가 과거와 달라졌는지 점검 |
| 2020-04-01 | Sprint 독립기업 종료 | T-Mobile merger 종결, 2.5GHz spectrum strategic value가 결합회사로 이전 |
| 2024-01-31 | 고정 사후평가 | Sprint 독립 equity는 소멸했으므로 원 security thesis는 merger 시점까지 평가 |

### Failure / Success Anatomy

- **근본 오류:** spectrum·balance-sheet 자산가치를 operating customer economics 또는 strategic exit probability와 잘못 연결
- **최초 검증·반증 신호:** 2016-05-03 — FY2015 결과에서 adjusted EBITDA $8.1bn, 1.2m+ postpaid net adds와 churn 개선이 확인되며 turnaround가 숫자로 검증됐다.
- **당시 알 수 있었나:** 가입자 순증·churn·ARPU·service revenue·EBITDA·CapEx·FCF·gross debt·maturities·spectrum 사용·corporate-action 조건은 공시와 earnings에서 재검증 가능했다.
- **피할 수 있었나:** 핵심 long은 일부 성공했다. 다만 $10을 못 넘는 기간이 길어질수록 spectrum value의 직접 monetization 가능성과 debt를 다시 평가해 장기 2~3x 기대는 낮췄어야 한다.
- **반사실 질문:** spectrum·segment business가 가치 있어도 integration, debt, corporate action 또는 security horizon이 반대로 움직이면 기존 보통주/스프레드의 payoff는 어떻게 달라지는가?
- **성공 패턴:** spectrum_optionality; fixed_cost_operating_leverage; event_driven_merger_arb; network_turnaround; strategic_buyer
- **실패·주의 패턴:** integration_failure; asset_value_trap; fcf_normalization_error; leverage; strategic_option_underpricing

### 주요 근거자료

- 1. VIC S 2014-08-06 원문 — Value Investors Club, 2014-08-06. 원 SQL description에서 당시 thesis·valuation·risk·catalyst·방향을 복원
- [2. Sprint 2006 Form 10-K](https://www.sec.gov/Archives/edgar/data/101830/000119312507040849/d10k.htm) — SEC, 2007-02-28. Nextel merger·Embarq spin·초기 통합상태 확인
- [3. Sprint Nextel 2007 Form 10-K](https://www.sec.gov/Archives/edgar/data/101830/000119312508043342/d10k.htm) — SEC, 2008-02-29. 4Q07 약 $29.7bn goodwill impairment·subscriber 문제 확인
- [4. Sprint FY2008 Results](https://www.sec.gov/Archives/edgar/data/101830/000119312509035054/dex991.htm) — Sprint/SEC, 2009-02-19. FY2008 free cash flow $1.8bn+ 확인
- [5. Sprint 2010 Form 10-K](https://www.sec.gov/Archives/edgar/data/101830/000119312511045676/d10k.htm) — SEC, 2011-02-24. 2010 operating cash flow·postpaid trends·historical shareholder performance 확인
- [6. Sprint 2014 Form 10-K](https://www.sec.gov/Archives/edgar/data/101830/000010183015000028/s-20150331x10k.htm) — SEC, 2015-05-26. network modernization·customer trends·SoftBank-era 상태 확인
- [7. Sprint FY2015 Results](https://newsroom.sprint.com/sprint-reports-fourth-quarter-and-fiscal-year-2015-results.htm) — Sprint, 2016-05-03. Adj EBITDA $8.1bn·postpaid net adds 1.2m+·churn 개선 확인
- [8. Sprint FY2016 Results](https://group.softbank/en/news/press/20170503) — Sprint/SoftBank, 2017-05-03. FY2016 adjusted FCF +$607m 등 turnaround cash flow 확인
- [9. Sprint FY2017 Results](https://newsroom.sprint.com/sprint-reports-fourth-quarter-and-fiscal-year-2017-results.htm) — Sprint, 2018-05-02. FY2017 adjusted FCF +$945m·두 해 연속 positive 확인
- [10. T-Mobile and Sprint amend merger terms](https://www.t-mobile.com/news/un-carrier/t-mobile-sprint-amend-business-combination-agreement) — T-Mobile, 2020-02-20. non-SoftBank Sprint 0.10256 exchange ratio 확인
- [11. T-Mobile completes merger with Sprint](https://www.t-mobile.com/news/un-carrier/t-mobile-sprint-one-company) — T-Mobile, 2020-04-01. 2020-04-01 종결 및 exchange ratio 확인
- 12. Sprint historical price context — Macrotrends/market history, 2020-04-01. VIC 당시 가격과 주요 저점·고점 교차검증


---

<!-- idea:7aaaeb44-58b2-4551-a8bb-4d14710150ef -->
## 5. 2016-03-09 — Handset lease accounting·-$4.2bn normalized FCF·equity zero Short

### 결론부터

**종합판정: 회계/FCF 통찰은 좋았지만 증권 thesis 실패.** 이 글은 'EBITDA가 좋아 보여도 handset lease cash outflow를 보라'는 점에서 매우 좋은 분석이었다. 그러나 normalized FCF를 과거 TTM 숫자에 고정하고 비용구조·subscriber economics가 바뀔 가능성을 낮게 봤다. 가장 큰 오류는 strategic optionality의 확률을 사실상 0으로 둔 것이다. 높은 spectrum value를 인정하면서도 그 자산을 가장 필요로 하는 T-Mobile의 거래가능성을 지나치게 배제했다.

**주가·증권 결과:** 약 $4에서 FY2017 high $9.65까지 상승. Short는 큰 adverse move를 겪었고 strategic T-Mobile exit까지 이어져 증권 thesis 실패.

**Thesis / Process 점수:** 5.8 / 6.2

### 1. 무슨 기업인가

Sprint는 미국 전국 단위 이동통신 사업자였으며 2005년 Nextel과 합병한 뒤 CDMA 기반 Sprint망과 iDEN 기반 Nextel망을 동시에 운영했다. 사업의 본질은 spectrum·기지국·backhaul·core network에 대규모 고정비를 선투자한 뒤 postpaid·prepaid 가입자의 월 서비스료에서 고객획득·단말기·network·sales 비용을 차감하는 구조였다. 2005~2010년 Sprint의 핵심 문제는 단순한 가입자 감소가 아니라 서로 다른 두 망과 브랜드를 합치는 과정에서 network quality·customer service·handset lineup이 동시에 악화되며 churn이 상승했다는 점이다. 반대로 가장 중요한 자산은 전국 단위 spectrum, 특히 2.5GHz 중대역이었다. 이 자산은 Sprint 자체 운영 아래에서는 충분히 monetization되지 못했지만 훗날 T-Mobile 합병에서 핵심 전략가치가 됐다. 따라서 Sprint를 분석할 때는 postpaid net adds, churn, ARPU, service revenue, adjusted EBITDA, network CapEx, 실제 FCF, handset financing/lease accounting, gross debt·maturities, spectrum의 사용가능성과 담보가치, 그리고 전략적 buyer 가능성을 함께 봐야 한다.

### 2. 산업 가치사슬과 돈의 흐름

Sprint의 돈 흐름은 '가입자수 × ARPU → service revenue → network·sales·device·customer-care 비용 → EBITDA → network CapEx·handset cash outflow·interest → FCF' 순이다. 무선망은 고정비가 커 가입자 증가가 margin을 크게 높일 수 있지만, 반대로 churn이 올라가면 같은 고정비를 더 적은 고객에게 배분해야 해 margin이 급격히 악화된다. 2010년대의 EIP·handset lease는 회계상 EBITDA와 실제 현금흐름을 더 복잡하게 만들었다. 단말기를 leasing하면 일부 비용이 당기 EBITDA에서 자산으로 이동할 수 있지만 현금은 먼저 나가기 때문에 EBITDA 개선과 FCF 개선을 동일시하면 안 된다. Spectrum은 매우 큰 자산가치를 가질 수 있지만 operating network에 묶여 있거나 FCC ownership cap·담보·고객망 제약이 있으면 liquidation value를 즉시 equity로 전환할 수 없다.

### 3. 경쟁우위·경쟁구도·핵심 지표

Sprint의 경쟁우위 후보는 전국망, 2.5GHz spectrum depth, 대규모 customer base와 SoftBank의 자본이었다. 그러나 Verizon·AT&T·T-Mobile 대비 network perception, churn, distribution, handset portfolio, balance sheet가 약했고, 특히 Nextel 통합 실패가 수년간 브랜드와 economics를 훼손했다. 2014 이후 network modernization과 cost cutting은 실제 개선을 만들었지만 높은 부채와 낮은 scale efficiency는 여전히 제약이었다. 이 기업의 역사는 '좋은 spectrum = 좋은 독립기업'이 아님을 보여준다. 핵심은 spectrum을 실제 coverage/capacity·customer retention·FCF로 전환할 운영능력과 자본구조다.

### 4. 당시 VIC 원문과 핵심 숫자

EIP와 handset leasing이 EBITDA를 왜곡해 시장이 Sprint의 실제 cash burn을 과소평가한다고 봤다. 복잡한 EBITDA adjustment 대신 trailing FCF를 보면 연 -$4.2bn이 정상화 run-rate이고, MLS·Network LeaseCo·spectrum financing 같은 금융공학은 가치를 만들지 않는다고 주장했다. Spectrum은 auction에서 매우 가치있을 수 있지만 대부분 운영에 필요하고 FCC cap 때문에 팔기 어렵다. 유일한 logical buyer는 T-Mobile이지만 takeover risk는 'exceedingly low'라고 판단했다.

### 5. 밸류에이션과 기대수익의 연결

회사 TTM cash burn 약 $4.2bn이 'temporary working capital'이 아니라 normalized FCF라고 주장. debt 약 $34bn, 3년 내 $10bn+ 추가차입 필요, 약 $8bn debt maturities를 고려하면 spectrum 가치에도 불구하고 equity 가치가 사실상 0에 가깝다고 봤다. 사후에는 subscriber/churn/ARPU 또는 segment earnings → EBITDA → CapEx·interest → FCF → debt·corporate action → 기존 보통주 또는 merger spread payoff 순으로 다시 연결해 검증했다.

### 투자논지를 구성한 핵심 주장

#### 1. Lease accounting — 적중 · 논지 비중 18%

**당시 주장**

handset lease가 EBITDA를 좋게 보이게 해 실제 cash burn을 숨긴다.

**당시 근거**

EIP와 handset leasing이 EBITDA를 왜곡해 시장이 Sprint의 실제 cash burn을 과소평가한다고 봤다. 복잡한 EBITDA adjustment 대신 trailing FCF를 보면 연 -$4.2bn이 정상화 run-rate이고, MLS·Network LeaseCo·spectrum financing 같은 금융공학은 가치를 만들지 않는다고 주장했다. Spectrum은 auction에서 매우 가치있을 수 있지만 대부분 운영에 필요하고 FCC cap 때문에 팔기 어렵다. 유일한 logical buyer는 T-Mobile이지만 takeover risk는 'exceedingly low'라고 판단했다.

**이 주장이 성립하려면**

lease cash outflow가 반복

**사전 반증조건**

accounting effect보다 cost/ARPU 개선이 큼

**실제 결과**

회계상 주의점 자체는 유효했다.

**정량적 괴리**

Normalized FCF / -$4.2bn / 지속 cash burn / FY2016 +$607m; FY2017 +$945m

**분석 오류·핵심**

핵심 causal chain은 실제 결과에서 확인됐다. 다만 그 성공이 증권 payoff의 원인이었는지는 별도 판정한다.

**재사용할 교훈**

Lease accounting 가설은 'accounting effect보다 cost/ARPU 개선이 큼'를 사전 반증조건으로 저장하고 사업·이벤트·가격 판정을 분리한다.

#### 2. -$4.2bn normalized FCF — 실패 · 논지 비중 18%

**당시 주장**

TTM -$4.2bn이 일시적이 아니라 정상이다.

**당시 근거**

EIP와 handset leasing이 EBITDA를 왜곡해 시장이 Sprint의 실제 cash burn을 과소평가한다고 봤다. 복잡한 EBITDA adjustment 대신 trailing FCF를 보면 연 -$4.2bn이 정상화 run-rate이고, MLS·Network LeaseCo·spectrum financing 같은 금융공학은 가치를 만들지 않는다고 주장했다. Spectrum은 auction에서 매우 가치있을 수 있지만 대부분 운영에 필요하고 FCC cap 때문에 팔기 어렵다. 유일한 logical buyer는 T-Mobile이지만 takeover risk는 'exceedingly low'라고 판단했다.

**이 주장이 성립하려면**

subscriber economics·cost base 불변

**사전 반증조건**

비용절감·매출개선으로 FCF 급반등

**실제 결과**

FY2016부터 positive adjusted FCF.

**정량적 괴리**

Debt / 약 $34bn / 추가 $10bn+ 필요 / financing과 operating improvement로 생존

**분석 오류·핵심**

좋은 자산·평균 operating path를 equity payoff에 직접 연결하거나, debt·integration·corporate action·timing의 joint distribution을 충분히 stress하지 않았다.

**재사용할 교훈**

-$4.2bn normalized FCF 가설은 '비용절감·매출개선으로 FCF 급반등'를 사전 반증조건으로 저장하고 사업·이벤트·가격 판정을 분리한다.

#### 3. Financing engineering — 부분 적중 · 논지 비중 16%

**당시 주장**

LeaseCo·spectrum financing은 경제적 가치를 만들지 않는다.

**당시 근거**

EIP와 handset leasing이 EBITDA를 왜곡해 시장이 Sprint의 실제 cash burn을 과소평가한다고 봤다. 복잡한 EBITDA adjustment 대신 trailing FCF를 보면 연 -$4.2bn이 정상화 run-rate이고, MLS·Network LeaseCo·spectrum financing 같은 금융공학은 가치를 만들지 않는다고 주장했다. Spectrum은 auction에서 매우 가치있을 수 있지만 대부분 운영에 필요하고 FCC cap 때문에 팔기 어렵다. 유일한 logical buyer는 T-Mobile이지만 takeover risk는 'exceedingly low'라고 판단했다.

**이 주장이 성립하려면**

현금유입이 debt와 동등하고 operating loss 지속

**사전 반증조건**

financing이 liquidity runway를 늘려 turnaround 시간 확보

**실제 결과**

가치창출 자체는 제한적이나 생존확률에는 영향.

**정량적 괴리**

주가 / 약 $4 / equity≈0 / FY2017 high $9.65

**분석 오류·핵심**

핵심 causal chain은 실제 결과에서 확인됐다. 다만 그 성공이 증권 payoff의 원인이었는지는 별도 판정한다.

**재사용할 교훈**

Financing engineering 가설은 'financing이 liquidity runway를 늘려 turnaround 시간 확보'를 사전 반증조건으로 저장하고 사업·이벤트·가격 판정을 분리한다.

#### 4. Spectrum unusable floor — 실패 · 논지 비중 16%

**당시 주장**

spectrum은 가치가 커도 팔 수 없어 equity floor가 아니다.

**당시 근거**

EIP와 handset leasing이 EBITDA를 왜곡해 시장이 Sprint의 실제 cash burn을 과소평가한다고 봤다. 복잡한 EBITDA adjustment 대신 trailing FCF를 보면 연 -$4.2bn이 정상화 run-rate이고, MLS·Network LeaseCo·spectrum financing 같은 금융공학은 가치를 만들지 않는다고 주장했다. Spectrum은 auction에서 매우 가치있을 수 있지만 대부분 운영에 필요하고 FCC cap 때문에 팔기 어렵다. 유일한 logical buyer는 T-Mobile이지만 takeover risk는 'exceedingly low'라고 판단했다.

**이 주장이 성립하려면**

규제·operating use 제약

**사전 반증조건**

전략적 buyer가 spectrum을 통째로 가치평가

**실제 결과**

후일 T-Mobile 거래가 이 경로를 실현했다.

**정량적 괴리**

T-Mobile buyer / 가능성 exceedingly low / takeover 무시 / 2018 거래 발표·2020 완료

**분석 오류·핵심**

좋은 자산·평균 operating path를 equity payoff에 직접 연결하거나, debt·integration·corporate action·timing의 joint distribution을 충분히 stress하지 않았다.

**재사용할 교훈**

Spectrum unusable floor 가설은 '전략적 buyer가 spectrum을 통째로 가치평가'를 사전 반증조건으로 저장하고 사업·이벤트·가격 판정을 분리한다.

#### 5. T-Mobile risk — 치명적 실패 · 논지 비중 16%

**당시 주장**

T-Mobile 인수위험은 exceedingly low다.

**당시 근거**

EIP와 handset leasing이 EBITDA를 왜곡해 시장이 Sprint의 실제 cash burn을 과소평가한다고 봤다. 복잡한 EBITDA adjustment 대신 trailing FCF를 보면 연 -$4.2bn이 정상화 run-rate이고, MLS·Network LeaseCo·spectrum financing 같은 금융공학은 가치를 만들지 않는다고 주장했다. Spectrum은 auction에서 매우 가치있을 수 있지만 대부분 운영에 필요하고 FCC cap 때문에 팔기 어렵다. 유일한 logical buyer는 T-Mobile이지만 takeover risk는 'exceedingly low'라고 판단했다.

**이 주장이 성립하려면**

규제·financing 장벽 지속

**사전 반증조건**

산업구조상 strategic logic 강화

**실제 결과**

실제로 거래 발표·종결.

**정량적 괴리**

약 $4에서 FY2017 high $9.65까지 상승. Short는 큰 adverse move를 겪었고 strategic T-Mobile exit까지 이어져 증권 thesis 실패.

**분석 오류·핵심**

좋은 자산·평균 operating path를 equity payoff에 직접 연결하거나, debt·integration·corporate action·timing의 joint distribution을 충분히 stress하지 않았다.

**재사용할 교훈**

T-Mobile risk 가설은 '산업구조상 strategic logic 강화'를 사전 반증조건으로 저장하고 사업·이벤트·가격 판정을 분리한다.

#### 6. Equity zero — 실패 · 논지 비중 16%

**당시 주장**

cash burn+debt 때문에 시총 $3bn도 과하다.

**당시 근거**

EIP와 handset leasing이 EBITDA를 왜곡해 시장이 Sprint의 실제 cash burn을 과소평가한다고 봤다. 복잡한 EBITDA adjustment 대신 trailing FCF를 보면 연 -$4.2bn이 정상화 run-rate이고, MLS·Network LeaseCo·spectrum financing 같은 금융공학은 가치를 만들지 않는다고 주장했다. Spectrum은 auction에서 매우 가치있을 수 있지만 대부분 운영에 필요하고 FCC cap 때문에 팔기 어렵다. 유일한 logical buyer는 T-Mobile이지만 takeover risk는 'exceedingly low'라고 판단했다.

**이 주장이 성립하려면**

FCF 개선과 strategic rescue 부재

**사전 반증조건**

FCF 흑자전환·M&A

**실제 결과**

주가가 두 배 이상 올라 short thesis 실패.

**정량적 괴리**

약 $4에서 FY2017 high $9.65까지 상승. Short는 큰 adverse move를 겪었고 strategic T-Mobile exit까지 이어져 증권 thesis 실패.

**분석 오류·핵심**

좋은 자산·평균 operating path를 equity payoff에 직접 연결하거나, debt·integration·corporate action·timing의 joint distribution을 충분히 stress하지 않았다.

**재사용할 교훈**

Equity zero 가설은 'FCF 흑자전환·M&A'를 사전 반증조건으로 저장하고 사업·이벤트·가격 판정을 분리한다.

### 6. 실제 사업의 시간순 전개

핵심 accounting 질문은 유효했지만 cash-flow path가 예상보다 빠르게 개선됐다. FY2016 adjusted FCF는 +$607m으로 FY2015 -$1.404bn에서 흑자전환했고 FY2017은 +$945m으로 두 해 연속 positive였다. 비용절감·network/customer 개선이 cash burn을 줄였다. 더 결정적으로 작성자가 거의 무시한 T-Mobile strategic exit가 결국 현실이 됐다. 주가는 FY2017 $9.65까지 올라 약 $4 short에 큰 역행을 만들었다.

### 7. 사업 결과와 가격 결과 분리

증권 결과는 약 $4에서 FY2017 high $9.65까지 상승. Short는 큰 adverse move를 겪었고 strategic T-Mobile exit까지 이어져 증권 thesis 실패. 사업논지·촉매·valuation·corporate structure와 주가를 서로 다른 판정으로 저장한다.

### 8. 무엇을 잘 봤고 무엇을 놓쳤나

이 글은 'EBITDA가 좋아 보여도 handset lease cash outflow를 보라'는 점에서 매우 좋은 분석이었다. 그러나 normalized FCF를 과거 TTM 숫자에 고정하고 비용구조·subscriber economics가 바뀔 가능성을 낮게 봤다. 가장 큰 오류는 strategic optionality의 확률을 사실상 0으로 둔 것이다. 높은 spectrum value를 인정하면서도 그 자산을 가장 필요로 하는 T-Mobile의 거래가능성을 지나치게 배제했다.

### 9. 최초 검증·반증 신호와 회피 가능성

2017-05-03 — FY2016 adjusted FCF +$607m이 발표돼 '-$4.2bn normalized burn'의 핵심 숫자가 반증됐다. 이 시점에 원 valuation bridge를 다시 만들면 operating thesis와 security thesis 중 무엇이 살아있는지 구분할 수 있었다. 회피 가능성: 매우 높음. FCF가 실제로 흑자전환하는 순간 short의 가장 중요한 quantitative premise를 폐기해야 했다. 또한 T-Mobile 합병 가능성을 tail scenario로라도 가격에 넣어야 했다.

### 10. 최종 판정·반사실·재사용 교훈

회계/FCF 통찰은 좋았지만 증권 thesis 실패. Telecom에서는 좋은 spectrum·좋은 콘텐츠·높은 FCF 하나만으로 equity floor를 만들지 않고, 실제 고객경제성·부채·corporate-action 귀속구조를 함께 stress해야 한다.

### 핵심 수치 — 당시 vs 실제

| 지표 | 글 당시 | VIC 기대 | 실제 | 판정 |
|---|---|---|---|---|
| Normalized FCF | -$4.2bn | 지속 cash burn | FY2016 +$607m; FY2017 +$945m | 치명적 반증 |
| Debt | 약 $34bn | 추가 $10bn+ 필요 | financing과 operating improvement로 생존 | distress 과대평가 |
| 주가 | 약 $4 | equity≈0 | FY2017 high $9.65 | 실패 |
| T-Mobile buyer | 가능성 exceedingly low | takeover 무시 | 2018 거래 발표·2020 완료 | 치명적 누락 |

### 사건 타임라인

| 시점 | 사건 | 논지에 대한 의미 |
|---|---|---|
| 2016-03-09 | VIC 아이디어 게시 | Handset lease accounting·-$4.2bn normalized FCF·equity zero Short |
| 2017-05-03 | 최초 핵심 검증·반증 신호 | FY2016 adjusted FCF +$607m이 발표돼 '-$4.2bn normalized burn'의 핵심 숫자가 반증됐다. |
| 2007-12-31 | Nextel 통합 손상 확인 | 2007년 대규모 goodwill impairment로 합병가치 훼손이 공식화 |
| 2016-12-31 | SoftBank-era operating/FCF 재평가 | 비용·network·subscriber economics가 과거와 달라졌는지 점검 |
| 2020-04-01 | Sprint 독립기업 종료 | T-Mobile merger 종결, 2.5GHz spectrum strategic value가 결합회사로 이전 |
| 2024-01-31 | 고정 사후평가 | Sprint 독립 equity는 소멸했으므로 원 security thesis는 merger 시점까지 평가 |

### Failure / Success Anatomy

- **근본 오류:** spectrum·balance-sheet 자산가치를 operating customer economics 또는 strategic exit probability와 잘못 연결
- **최초 검증·반증 신호:** 2017-05-03 — FY2016 adjusted FCF +$607m이 발표돼 '-$4.2bn normalized burn'의 핵심 숫자가 반증됐다.
- **당시 알 수 있었나:** 가입자 순증·churn·ARPU·service revenue·EBITDA·CapEx·FCF·gross debt·maturities·spectrum 사용·corporate-action 조건은 공시와 earnings에서 재검증 가능했다.
- **피할 수 있었나:** 매우 높음. FCF가 실제로 흑자전환하는 순간 short의 가장 중요한 quantitative premise를 폐기해야 했다. 또한 T-Mobile 합병 가능성을 tail scenario로라도 가격에 넣어야 했다.
- **반사실 질문:** spectrum·segment business가 가치 있어도 integration, debt, corporate action 또는 security horizon이 반대로 움직이면 기존 보통주/스프레드의 payoff는 어떻게 달라지는가?
- **성공 패턴:** spectrum_optionality; fixed_cost_operating_leverage; event_driven_merger_arb; network_turnaround; strategic_buyer
- **실패·주의 패턴:** integration_failure; asset_value_trap; fcf_normalization_error; leverage; strategic_option_underpricing

### 주요 근거자료

- 1. VIC S 2016-03-09 원문 — Value Investors Club, 2016-03-09. 원 SQL description에서 당시 thesis·valuation·risk·catalyst·방향을 복원
- [2. Sprint 2006 Form 10-K](https://www.sec.gov/Archives/edgar/data/101830/000119312507040849/d10k.htm) — SEC, 2007-02-28. Nextel merger·Embarq spin·초기 통합상태 확인
- [3. Sprint Nextel 2007 Form 10-K](https://www.sec.gov/Archives/edgar/data/101830/000119312508043342/d10k.htm) — SEC, 2008-02-29. 4Q07 약 $29.7bn goodwill impairment·subscriber 문제 확인
- [4. Sprint FY2008 Results](https://www.sec.gov/Archives/edgar/data/101830/000119312509035054/dex991.htm) — Sprint/SEC, 2009-02-19. FY2008 free cash flow $1.8bn+ 확인
- [5. Sprint 2010 Form 10-K](https://www.sec.gov/Archives/edgar/data/101830/000119312511045676/d10k.htm) — SEC, 2011-02-24. 2010 operating cash flow·postpaid trends·historical shareholder performance 확인
- [6. Sprint 2014 Form 10-K](https://www.sec.gov/Archives/edgar/data/101830/000010183015000028/s-20150331x10k.htm) — SEC, 2015-05-26. network modernization·customer trends·SoftBank-era 상태 확인
- [7. Sprint FY2015 Results](https://newsroom.sprint.com/sprint-reports-fourth-quarter-and-fiscal-year-2015-results.htm) — Sprint, 2016-05-03. Adj EBITDA $8.1bn·postpaid net adds 1.2m+·churn 개선 확인
- [8. Sprint FY2016 Results](https://group.softbank/en/news/press/20170503) — Sprint/SoftBank, 2017-05-03. FY2016 adjusted FCF +$607m 등 turnaround cash flow 확인
- [9. Sprint FY2017 Results](https://newsroom.sprint.com/sprint-reports-fourth-quarter-and-fiscal-year-2017-results.htm) — Sprint, 2018-05-02. FY2017 adjusted FCF +$945m·두 해 연속 positive 확인
- [10. T-Mobile and Sprint amend merger terms](https://www.t-mobile.com/news/un-carrier/t-mobile-sprint-amend-business-combination-agreement) — T-Mobile, 2020-02-20. non-SoftBank Sprint 0.10256 exchange ratio 확인
- [11. T-Mobile completes merger with Sprint](https://www.t-mobile.com/news/un-carrier/t-mobile-sprint-one-company) — T-Mobile, 2020-04-01. 2020-04-01 종결 및 exchange ratio 확인
- 12. Sprint historical price context — Macrotrends/market history, 2020-04-01. VIC 당시 가격과 주요 저점·고점 교차검증


---

<!-- idea:c202c3b5-29ba-4723-aa1c-9efd82d8e706 -->
## 6. 2020-02-21 — T-Mobile merger 마지막 45~60일 spread Long

### 결론부터

**종합판정: 깔끔한 성공.** 이번 배치에서 가장 깔끔한 event-driven 성공이다. 중요한 점은 'Sprint가 좋은 회사인가'가 아니라 이미 승인된 계약의 교환비율·조건·closing mechanics만 분석했다는 것이다. 2016 Short와 달리 strategic buyer 가능성을 확률로 추정하는 단계가 아니라 법적·규제적 불확실성이 대부분 해소된 시점이었다.

**주가·증권 결과:** 거래는 작성자 예상 4월 6일보다 빠른 2020-04-01 종결. non-SoftBank Sprint 주주는 1주당 0.10256 TMUS를 받아 spread trade가 성공.

**Thesis / Process 점수:** 9.5 / 9.3

### 1. 무슨 기업인가

Sprint는 미국 전국 단위 이동통신 사업자였으며 2005년 Nextel과 합병한 뒤 CDMA 기반 Sprint망과 iDEN 기반 Nextel망을 동시에 운영했다. 사업의 본질은 spectrum·기지국·backhaul·core network에 대규모 고정비를 선투자한 뒤 postpaid·prepaid 가입자의 월 서비스료에서 고객획득·단말기·network·sales 비용을 차감하는 구조였다. 2005~2010년 Sprint의 핵심 문제는 단순한 가입자 감소가 아니라 서로 다른 두 망과 브랜드를 합치는 과정에서 network quality·customer service·handset lineup이 동시에 악화되며 churn이 상승했다는 점이다. 반대로 가장 중요한 자산은 전국 단위 spectrum, 특히 2.5GHz 중대역이었다. 이 자산은 Sprint 자체 운영 아래에서는 충분히 monetization되지 못했지만 훗날 T-Mobile 합병에서 핵심 전략가치가 됐다. 따라서 Sprint를 분석할 때는 postpaid net adds, churn, ARPU, service revenue, adjusted EBITDA, network CapEx, 실제 FCF, handset financing/lease accounting, gross debt·maturities, spectrum의 사용가능성과 담보가치, 그리고 전략적 buyer 가능성을 함께 봐야 한다.

### 2. 산업 가치사슬과 돈의 흐름

Sprint의 돈 흐름은 '가입자수 × ARPU → service revenue → network·sales·device·customer-care 비용 → EBITDA → network CapEx·handset cash outflow·interest → FCF' 순이다. 무선망은 고정비가 커 가입자 증가가 margin을 크게 높일 수 있지만, 반대로 churn이 올라가면 같은 고정비를 더 적은 고객에게 배분해야 해 margin이 급격히 악화된다. 2010년대의 EIP·handset lease는 회계상 EBITDA와 실제 현금흐름을 더 복잡하게 만들었다. 단말기를 leasing하면 일부 비용이 당기 EBITDA에서 자산으로 이동할 수 있지만 현금은 먼저 나가기 때문에 EBITDA 개선과 FCF 개선을 동일시하면 안 된다. Spectrum은 매우 큰 자산가치를 가질 수 있지만 operating network에 묶여 있거나 FCC ownership cap·담보·고객망 제약이 있으면 liquidation value를 즉시 equity로 전환할 수 없다.

### 3. 경쟁우위·경쟁구도·핵심 지표

Sprint의 경쟁우위 후보는 전국망, 2.5GHz spectrum depth, 대규모 customer base와 SoftBank의 자본이었다. 그러나 Verizon·AT&T·T-Mobile 대비 network perception, churn, distribution, handset portfolio, balance sheet가 약했고, 특히 Nextel 통합 실패가 수년간 브랜드와 economics를 훼손했다. 2014 이후 network modernization과 cost cutting은 실제 개선을 만들었지만 높은 부채와 낮은 scale efficiency는 여전히 제약이었다. 이 기업의 역사는 '좋은 spectrum = 좋은 독립기업'이 아님을 보여준다. 핵심은 spectrum을 실제 coverage/capacity·customer retention·FCF로 전환할 운영능력과 자본구조다.

### 4. 당시 VIC 원문과 핵심 숫자

DOJ/FCC 승인과 연방법원 승소 뒤 거래가 'red zone'에 들어왔고, 마지막 주요 변수였던 SoftBank terms 재협상도 끝났으므로 남은 closing risk는 clerical·mechanical 수준이라고 봤다. Sprint common을 사고 정확한 비율만큼 TMUS를 short해 시장베타를 제거하고 closing까지 보유하는 merger-arb였다.

### 5. 밸류에이션과 기대수익의 연결

2020-02-19 amended terms에서 일반 Sprint 주주는 기존과 동일한 0.10256 TMUS/S 교환비율을 유지. 규제승인·financing condition이 사실상 해결된 상태에서 45~60일 보유로 약 7.5% gross spread를 제시. 사후에는 subscriber/churn/ARPU 또는 segment earnings → EBITDA → CapEx·interest → FCF → debt·corporate action → 기존 보통주 또는 merger spread payoff 순으로 다시 연결해 검증했다.

### 투자논지를 구성한 핵심 주장

#### 1. Regulatory completion — 적중 · 논지 비중 18%

**당시 주장**

필수 규제승인은 사실상 끝났다.

**당시 근거**

DOJ/FCC 승인과 연방법원 승소 뒤 거래가 'red zone'에 들어왔고, 마지막 주요 변수였던 SoftBank terms 재협상도 끝났으므로 남은 closing risk는 clerical·mechanical 수준이라고 봤다. Sprint common을 사고 정확한 비율만큼 TMUS를 short해 시장베타를 제거하고 closing까지 보유하는 merger-arb였다.

**이 주장이 성립하려면**

FCC/DOJ/법원 이슈 재발 없음

**사전 반증조건**

새 injunction·regulatory reopening

**실제 결과**

거래는 정상 종결됐다.

**정량적 괴리**

Gross spread / 약 7.5% / 45~60일 수익 / 2020-04-01 종결

**분석 오류·핵심**

핵심 causal chain은 실제 결과에서 확인됐다. 다만 그 성공이 증권 payoff의 원인이었는지는 별도 판정한다.

**재사용할 교훈**

Regulatory completion 가설은 '새 injunction·regulatory reopening'를 사전 반증조건으로 저장하고 사업·이벤트·가격 판정을 분리한다.

#### 2. Amended terms — 적중 · 논지 비중 18%

**당시 주장**

SoftBank 재협상 후 일반 Sprint 주주는 0.10256을 유지한다.

**당시 근거**

DOJ/FCC 승인과 연방법원 승소 뒤 거래가 'red zone'에 들어왔고, 마지막 주요 변수였던 SoftBank terms 재협상도 끝났으므로 남은 closing risk는 clerical·mechanical 수준이라고 봤다. Sprint common을 사고 정확한 비율만큼 TMUS를 short해 시장베타를 제거하고 closing까지 보유하는 merger-arb였다.

**이 주장이 성립하려면**

amendment가 변경되지 않음

**사전 반증조건**

일반주주 exchange ratio 재하향

**실제 결과**

그 비율 그대로 적용됐다.

**정량적 괴리**

교환비율 / 0.10256 TMUS/S / 일반 S 주주 유지 / 0.10256 적용

**분석 오류·핵심**

핵심 causal chain은 실제 결과에서 확인됐다. 다만 그 성공이 증권 payoff의 원인이었는지는 별도 판정한다.

**재사용할 교훈**

Amended terms 가설은 '일반주주 exchange ratio 재하향'를 사전 반증조건으로 저장하고 사업·이벤트·가격 판정을 분리한다.

#### 3. Financing — 적중 · 논지 비중 16%

**당시 주장**

financing이 더 이상 closing condition이 아니다.

**당시 근거**

DOJ/FCC 승인과 연방법원 승소 뒤 거래가 'red zone'에 들어왔고, 마지막 주요 변수였던 SoftBank terms 재협상도 끝났으므로 남은 closing risk는 clerical·mechanical 수준이라고 봤다. Sprint common을 사고 정확한 비율만큼 TMUS를 short해 시장베타를 제거하고 closing까지 보유하는 merger-arb였다.

**이 주장이 성립하려면**

commitment와 closing mechanics 안정

**사전 반증조건**

financing failure

**실제 결과**

종결에 문제 없었다.

**정량적 괴리**

예상 종결 / 2020-04-06 / 약 45일 / 2020-04-01

**분석 오류·핵심**

핵심 causal chain은 실제 결과에서 확인됐다. 다만 그 성공이 증권 payoff의 원인이었는지는 별도 판정한다.

**재사용할 교훈**

Financing 가설은 'financing failure'를 사전 반증조건으로 저장하고 사업·이벤트·가격 판정을 분리한다.

#### 4. Closing timing — 강한 적중 · 논지 비중 16%

**당시 주장**

45~60일 내, 4월 6일 정도 종결한다.

**당시 근거**

DOJ/FCC 승인과 연방법원 승소 뒤 거래가 'red zone'에 들어왔고, 마지막 주요 변수였던 SoftBank terms 재협상도 끝났으므로 남은 closing risk는 clerical·mechanical 수준이라고 봤다. Sprint common을 사고 정확한 비율만큼 TMUS를 short해 시장베타를 제거하고 closing까지 보유하는 merger-arb였다.

**이 주장이 성립하려면**

administrative steps만 남음

**사전 반증조건**

장기 지연

**실제 결과**

4월 1일 조기 종결.

**정량적 괴리**

방향 / SQL Short / Long S / Short TMUS / spread trade

**분석 오류·핵심**

핵심 causal chain은 실제 결과에서 확인됐다. 다만 그 성공이 증권 payoff의 원인이었는지는 별도 판정한다.

**재사용할 교훈**

Closing timing 가설은 '장기 지연'를 사전 반증조건으로 저장하고 사업·이벤트·가격 판정을 분리한다.

#### 5. Hedge — 적중 · 논지 비중 16%

**당시 주장**

TMUS short로 시장·acquirer beta를 제거한다.

**당시 근거**

DOJ/FCC 승인과 연방법원 승소 뒤 거래가 'red zone'에 들어왔고, 마지막 주요 변수였던 SoftBank terms 재협상도 끝났으므로 남은 closing risk는 clerical·mechanical 수준이라고 봤다. Sprint common을 사고 정확한 비율만큼 TMUS를 short해 시장베타를 제거하고 closing까지 보유하는 merger-arb였다.

**이 주장이 성립하려면**

hedge ratio 정확

**사전 반증조건**

borrow/ratio mismatch

**실제 결과**

계약비율 기반 spread가 수렴했다.

**정량적 괴리**

거래는 작성자 예상 4월 6일보다 빠른 2020-04-01 종결. non-SoftBank Sprint 주주는 1주당 0.10256 TMUS를 받아 spread trade가 성공.

**분석 오류·핵심**

핵심 causal chain은 실제 결과에서 확인됐다. 다만 그 성공이 증권 payoff의 원인이었는지는 별도 판정한다.

**재사용할 교훈**

Hedge 가설은 'borrow/ratio mismatch'를 사전 반증조건으로 저장하고 사업·이벤트·가격 판정을 분리한다.

#### 6. 7.5% spread — 성공 · 논지 비중 16%

**당시 주장**

잔여 deal-break risk 대비 gross spread가 매력적이다.

**당시 근거**

DOJ/FCC 승인과 연방법원 승소 뒤 거래가 'red zone'에 들어왔고, 마지막 주요 변수였던 SoftBank terms 재협상도 끝났으므로 남은 closing risk는 clerical·mechanical 수준이라고 봤다. Sprint common을 사고 정확한 비율만큼 TMUS를 short해 시장베타를 제거하고 closing까지 보유하는 merger-arb였다.

**이 주장이 성립하려면**

break probability 매우 낮음

**사전 반증조건**

거래 무산

**실제 결과**

거래 성공으로 spread 수익 실현.

**정량적 괴리**

거래는 작성자 예상 4월 6일보다 빠른 2020-04-01 종결. non-SoftBank Sprint 주주는 1주당 0.10256 TMUS를 받아 spread trade가 성공.

**분석 오류·핵심**

핵심 causal chain은 실제 결과에서 확인됐다. 다만 그 성공이 증권 payoff의 원인이었는지는 별도 판정한다.

**재사용할 교훈**

7.5% spread 가설은 '거래 무산'를 사전 반증조건으로 저장하고 사업·이벤트·가격 판정을 분리한다.

### 6. 실제 사업의 시간순 전개

T-Mobile과 Sprint는 2020년 4월 1일 합병을 완료했다. non-SoftBank Sprint 주주는 Sprint 1주당 0.10256 T-Mobile 주식을 받았다. 작성자가 가정한 4월 6일보다 빨리 종결되어 duration도 더 짧았다.

### 7. 사업 결과와 가격 결과 분리

증권 결과는 거래는 작성자 예상 4월 6일보다 빠른 2020-04-01 종결. non-SoftBank Sprint 주주는 1주당 0.10256 TMUS를 받아 spread trade가 성공. 사업논지·촉매·valuation·corporate structure와 주가를 서로 다른 판정으로 저장한다.

### 8. 무엇을 잘 봤고 무엇을 놓쳤나

이번 배치에서 가장 깔끔한 event-driven 성공이다. 중요한 점은 'Sprint가 좋은 회사인가'가 아니라 이미 승인된 계약의 교환비율·조건·closing mechanics만 분석했다는 것이다. 2016 Short와 달리 strategic buyer 가능성을 확률로 추정하는 단계가 아니라 법적·규제적 불확실성이 대부분 해소된 시점이었다.

### 9. 최초 검증·반증 신호와 회피 가능성

2020-04-01 — T-Mobile/Sprint merger가 공식 종결되고 교환비율 0.10256이 적용되어 thesis가 완전히 실현됐다. 이 시점에 원 valuation bridge를 다시 만들면 operating thesis와 security thesis 중 무엇이 살아있는지 구분할 수 있었다. 회피 가능성: 해당 없음. 다만 merger arbitrage는 작은 잔여 spread에 비해 deal break 손실이 클 수 있으므로 포지션 sizing과 hedge ratio가 핵심이다.

### 10. 최종 판정·반사실·재사용 교훈

깔끔한 성공. Telecom에서는 좋은 spectrum·좋은 콘텐츠·높은 FCF 하나만으로 equity floor를 만들지 않고, 실제 고객경제성·부채·corporate-action 귀속구조를 함께 stress해야 한다.

### 핵심 수치 — 당시 vs 실제

| 지표 | 글 당시 | VIC 기대 | 실제 | 판정 |
|---|---|---|---|---|
| Gross spread | 약 7.5% | 45~60일 수익 | 2020-04-01 종결 | 적중 |
| 교환비율 | 0.10256 TMUS/S | 일반 S 주주 유지 | 0.10256 적용 | 적중 |
| 예상 종결 | 2020-04-06 | 약 45일 | 2020-04-01 | 조기 적중 |
| 방향 | SQL Short | Long S / Short TMUS | spread trade | 메타데이터 교정 |

### 사건 타임라인

| 시점 | 사건 | 논지에 대한 의미 |
|---|---|---|
| 2020-02-21 | VIC 아이디어 게시 | T-Mobile merger 마지막 45~60일 spread Long |
| 2020-04-01 | 최초 핵심 검증·반증 신호 | T-Mobile/Sprint merger가 공식 종결되고 교환비율 0.10256이 적용되어 thesis가 완전히 실현됐다. |
| 2007-12-31 | Nextel 통합 손상 확인 | 2007년 대규모 goodwill impairment로 합병가치 훼손이 공식화 |
| 2016-12-31 | SoftBank-era operating/FCF 재평가 | 비용·network·subscriber economics가 과거와 달라졌는지 점검 |
| 2020-04-01 | Sprint 독립기업 종료 | T-Mobile merger 종결, 2.5GHz spectrum strategic value가 결합회사로 이전 |
| 2024-01-31 | 고정 사후평가 | Sprint 독립 equity는 소멸했으므로 원 security thesis는 merger 시점까지 평가 |

### Failure / Success Anatomy

- **근본 오류:** 핵심 causal chain은 상당 부분 맞았으나 operating success·event success·security payoff를 계속 분리해야 함
- **최초 검증·반증 신호:** 2020-04-01 — T-Mobile/Sprint merger가 공식 종결되고 교환비율 0.10256이 적용되어 thesis가 완전히 실현됐다.
- **당시 알 수 있었나:** 가입자 순증·churn·ARPU·service revenue·EBITDA·CapEx·FCF·gross debt·maturities·spectrum 사용·corporate-action 조건은 공시와 earnings에서 재검증 가능했다.
- **피할 수 있었나:** 해당 없음. 다만 merger arbitrage는 작은 잔여 spread에 비해 deal break 손실이 클 수 있으므로 포지션 sizing과 hedge ratio가 핵심이다.
- **반사실 질문:** spectrum·segment business가 가치 있어도 integration, debt, corporate action 또는 security horizon이 반대로 움직이면 기존 보통주/스프레드의 payoff는 어떻게 달라지는가?
- **성공 패턴:** spectrum_optionality; fixed_cost_operating_leverage; event_driven_merger_arb; network_turnaround; strategic_buyer
- **실패·주의 패턴:** integration_failure; asset_value_trap; fcf_normalization_error; leverage; strategic_option_underpricing

### 주요 근거자료

- [1. VIC S 2020-02-21 원문](https://www.valueinvestorsclub.com/idea/SPRINT_CORP/9908147447) — Value Investors Club, 2020-02-21. 원 SQL description에서 당시 thesis·valuation·risk·catalyst·방향을 복원
- [2. Sprint 2006 Form 10-K](https://www.sec.gov/Archives/edgar/data/101830/000119312507040849/d10k.htm) — SEC, 2007-02-28. Nextel merger·Embarq spin·초기 통합상태 확인
- [3. Sprint Nextel 2007 Form 10-K](https://www.sec.gov/Archives/edgar/data/101830/000119312508043342/d10k.htm) — SEC, 2008-02-29. 4Q07 약 $29.7bn goodwill impairment·subscriber 문제 확인
- [4. Sprint FY2008 Results](https://www.sec.gov/Archives/edgar/data/101830/000119312509035054/dex991.htm) — Sprint/SEC, 2009-02-19. FY2008 free cash flow $1.8bn+ 확인
- [5. Sprint 2010 Form 10-K](https://www.sec.gov/Archives/edgar/data/101830/000119312511045676/d10k.htm) — SEC, 2011-02-24. 2010 operating cash flow·postpaid trends·historical shareholder performance 확인
- [6. Sprint 2014 Form 10-K](https://www.sec.gov/Archives/edgar/data/101830/000010183015000028/s-20150331x10k.htm) — SEC, 2015-05-26. network modernization·customer trends·SoftBank-era 상태 확인
- [7. Sprint FY2015 Results](https://newsroom.sprint.com/sprint-reports-fourth-quarter-and-fiscal-year-2015-results.htm) — Sprint, 2016-05-03. Adj EBITDA $8.1bn·postpaid net adds 1.2m+·churn 개선 확인
- [8. Sprint FY2016 Results](https://group.softbank/en/news/press/20170503) — Sprint/SoftBank, 2017-05-03. FY2016 adjusted FCF +$607m 등 turnaround cash flow 확인
- [9. Sprint FY2017 Results](https://newsroom.sprint.com/sprint-reports-fourth-quarter-and-fiscal-year-2017-results.htm) — Sprint, 2018-05-02. FY2017 adjusted FCF +$945m·두 해 연속 positive 확인
- [10. T-Mobile and Sprint amend merger terms](https://www.t-mobile.com/news/un-carrier/t-mobile-sprint-amend-business-combination-agreement) — T-Mobile, 2020-02-20. non-SoftBank Sprint 0.10256 exchange ratio 확인
- [11. T-Mobile completes merger with Sprint](https://www.t-mobile.com/news/un-carrier/t-mobile-sprint-one-company) — T-Mobile, 2020-04-01. 2020-04-01 종결 및 exchange ratio 확인
- 12. Sprint historical price context — Macrotrends/market history, 2020-04-01. VIC 당시 가격과 주요 저점·고점 교차검증


---

# AT&T INC. (T) — 기업과 비즈니스

## 1. 무슨 기업인가

AT&T는 미국의 대형 통신사업자로 wireless, fiber broadband와 기업통신을 중심으로 현금흐름을 창출한다. 다만 2015 DirecTV, 2018 Time Warner 인수로 한동안 미디어·위성TV까지 포함한 거대한 복합기업이 되었고, 2021~22 WarnerMedia/Discovery 거래와 DirecTV 분리를 통해 다시 통신 중심으로 축소됐다. Wireless에서는 postpaid phone subscribers·ARPU·churn·network CapEx·spectrum이 핵심이고, fiber에서는 passings·net adds·penetration·ARPU와 build cost가 중요하다. 미디어 보유기에는 HBO/HBO Max subscriber growth, content spend, advertising, distribution economics도 equity value를 좌우했다. AT&T의 VIC 역사는 특히 '현금흐름은 맞았지만 M&A의 전략적 질이 틀린 경우', 'HBO Max 운영지표는 맞았지만 corporate structure가 바뀐 경우', '높은 dividend yield가 downside floor가 아닌 경우'를 잘 보여준다.

## 2. 산업 가치사슬과 돈의 흐름

AT&T의 핵심 현금창출은 wireless와 broadband subscription이다. Service revenue에서 network operating cost, sales, handset subsidy/financing, customer care와 SG&A를 차감해 EBITDA가 나오고, 여기서 spectrum·fiber·5G CapEx, interest, taxes, working capital을 차감하면 FCF가 된다. Time Warner 보유기에는 HBO·Turner·Warner Bros의 subscription, advertising, licensing, theatrical economics가 추가되었다. 그러나 높은 부채 때문에 EBITDA가 늘어도 debt service와 mandatory CapEx가 크면 equity FCF가 제한될 수 있다. 특히 AT&T는 asset sales, receivables factoring, vendor financing, DirecTV economics 등으로 headline FCF와 underlying cash conversion의 차이를 따져야 했다.

## 3. 경쟁우위·경쟁구도·핵심 지표

AT&T의 주요 우위는 전국 무선망·spectrum·distribution·기업고객·fiber footprint와 방대한 customer base다. 하지만 wireless는 Verizon·T-Mobile과 지속 경쟁하며, DirecTV·WarnerMedia 같은 비통신 자산은 통신 moat와 별개로 자본배분의 질을 요구한다. 2018~21의 핵심 질문은 'Time Warner가 좋은 콘텐츠 자산인가'보다 'AT&T 안에서 높은 부채와 복합기업 할인까지 감안했을 때 주당가치를 높이는가'였다. 2021 이후에는 Warner 분리로 그 질문 자체가 사라졌다. 따라서 통신 operating metrics, FCF와 동시에 net debt, dividend coverage, M&A·spin 구조와 기존 주주에게 귀속되는 분배가치를 추적해야 한다.

## 4. 아이디어 전체 판정

| 게시일 | 원 SQL | 실제방향 | 핵심 논지 | 가격·증권 결과 | 종합판정 |
|---|---|---|---|---|---|
| 2018-07-16 | Short | Long | Time Warner cash-flow·deleveraging·$40 Long | 2019년 말 약 $39.08로 $40 목표에 거의 도달했고 높은 배당까지 포함하면 18개월 성과는 좋았다. 이후 Time Warner/DirecTV 전략은 결국 분리로 되돌려졌다. | 가격·현금흐름 성공 / 전략적 M&A 평가는 혼합 |
| 2020-01-29 | Short | Short | FCF quality·DirecTV decline·2022 guidance skepticism Short | 2020년 3월 COVID 충격 때 $30 아래로 급락했고 2020년 말도 약 $28.75로 $26~30 target zone에 근접. 가격 방향은 성공했지만 pandemic이라는 외생요인이 컸고 wireless는 예상보다 강했다. | 가격 성공·인과 혼합 |
| 2021-01-03 | Short | Long | HBO Max subscriber surprise·$51~63.5 Long | HBO Max subscriber thesis는 빠르게 적중했지만 AT&T는 2021-05 WarnerMedia 분리를 발표. 2024-01-31 AT&T $15.85 + 배분된 0.241917 WBD×$10.02 ≈ $18.27 before dividends로 원 entry와 $51~63 target을 크게 하회. | 운영촉매 적중·증권/기업구조 thesis 실패 |
| 2021-05-13 | Short | Long | Warner 55% valuation·wireless/fiber·$65 SOTP Long | 불과 4일 뒤 WarnerMedia 분리 발표로 핵심 SOTP 구조가 무효화. 2024-01 package value는 AT&T $15.85 + 0.241917 WBD×$10.02 ≈ $18.27 before dividends로 entry 대비 크게 낮음. | 기업구조가 4일 만에 반증된 실패 |

---

<!-- idea:27aa7b16-15ab-49a6-b29b-6eb9af2c225a -->
## 1. 2018-07-16 — Time Warner cash-flow·deleveraging·$40 Long

### 결론부터

**종합판정: 가격·현금흐름 성공 / 전략적 M&A 평가는 혼합.** 이 글은 '좋은/나쁜 M&A'를 추상적으로 논하기보다 acquired EBITDA와 CapEx를 cash conversion으로 연결한 점이 좋았다. 단기 cash-generation과 deleveraging은 정확했다. 다만 거래가 현금흐름에 accretive하다는 것과 장기 ROIC·corporate fit이 좋다는 것은 다른 문제다. 결국 Warner 분리는 strategic thesis가 완전히 성공하지 않았음을 보여준다.

**주가·증권 결과:** 2019년 말 약 $39.08로 $40 목표에 거의 도달했고 높은 배당까지 포함하면 18개월 성과는 좋았다. 이후 Time Warner/DirecTV 전략은 결국 분리로 되돌려졌다.

**Thesis / Process 점수:** 8 / 8

### 1. 무슨 기업인가

AT&T는 미국의 대형 통신사업자로 wireless, fiber broadband와 기업통신을 중심으로 현금흐름을 창출한다. 다만 2015 DirecTV, 2018 Time Warner 인수로 한동안 미디어·위성TV까지 포함한 거대한 복합기업이 되었고, 2021~22 WarnerMedia/Discovery 거래와 DirecTV 분리를 통해 다시 통신 중심으로 축소됐다. Wireless에서는 postpaid phone subscribers·ARPU·churn·network CapEx·spectrum이 핵심이고, fiber에서는 passings·net adds·penetration·ARPU와 build cost가 중요하다. 미디어 보유기에는 HBO/HBO Max subscriber growth, content spend, advertising, distribution economics도 equity value를 좌우했다. AT&T의 VIC 역사는 특히 '현금흐름은 맞았지만 M&A의 전략적 질이 틀린 경우', 'HBO Max 운영지표는 맞았지만 corporate structure가 바뀐 경우', '높은 dividend yield가 downside floor가 아닌 경우'를 잘 보여준다.

### 2. 산업 가치사슬과 돈의 흐름

AT&T의 핵심 현금창출은 wireless와 broadband subscription이다. Service revenue에서 network operating cost, sales, handset subsidy/financing, customer care와 SG&A를 차감해 EBITDA가 나오고, 여기서 spectrum·fiber·5G CapEx, interest, taxes, working capital을 차감하면 FCF가 된다. Time Warner 보유기에는 HBO·Turner·Warner Bros의 subscription, advertising, licensing, theatrical economics가 추가되었다. 그러나 높은 부채 때문에 EBITDA가 늘어도 debt service와 mandatory CapEx가 크면 equity FCF가 제한될 수 있다. 특히 AT&T는 asset sales, receivables factoring, vendor financing, DirecTV economics 등으로 headline FCF와 underlying cash conversion의 차이를 따져야 했다.

### 3. 경쟁우위·경쟁구도·핵심 지표

AT&T의 주요 우위는 전국 무선망·spectrum·distribution·기업고객·fiber footprint와 방대한 customer base다. 하지만 wireless는 Verizon·T-Mobile과 지속 경쟁하며, DirecTV·WarnerMedia 같은 비통신 자산은 통신 moat와 별개로 자본배분의 질을 요구한다. 2018~21의 핵심 질문은 'Time Warner가 좋은 콘텐츠 자산인가'보다 'AT&T 안에서 높은 부채와 복합기업 할인까지 감안했을 때 주당가치를 높이는가'였다. 2021 이후에는 Warner 분리로 그 질문 자체가 사라졌다. 따라서 통신 operating metrics, FCF와 동시에 net debt, dividend coverage, M&A·spin 구조와 기존 주주에게 귀속되는 분배가치를 추적해야 한다.

### 4. 당시 VIC 원문과 핵심 숫자

Time Warner 인수, DOJ appeal, 거래 financing 때문에 AT&T가 6년 저점과 6% dividend yield에 거래되지만 cash economics는 시장 우려보다 좋다고 봤다. TWX는 낮은 capital intensity의 콘텐츠 EBITDA를 추가하고, combined FCF로 약 3.2x net debt를 수년 내 2.5x 아래로 낮출 수 있다고 주장했다. DOJ appeal은 약하고 배당도 충분히 커버되므로 downside가 제한적이라고 봤다.

### 5. 밸류에이션과 기대수익의 연결

Time Warner가 $9bn+ EBITDA와 $1bn 미만 CapEx를 더해 combined EBITDA $55~60bn+, CapEx $22~25bn, EBITDA-CapEx floor 약 $30bn을 만든다고 봤다. 약 12x earnings와 5% dividend yield 기준 $40, wireless까지 회복하면 high-$40s 가능. 사후에는 subscriber/churn/ARPU 또는 segment earnings → EBITDA → CapEx·interest → FCF → debt·corporate action → 기존 보통주 또는 merger spread payoff 순으로 다시 연결해 검증했다.

### 투자논지를 구성한 핵심 주장

#### 1. TWX cash conversion — 적중 · 논지 비중 18%

**당시 주장**

Time Warner는 $9bn+ EBITDA에 CapEx가 낮아 combined FCF를 높인다.

**당시 근거**

Time Warner 인수, DOJ appeal, 거래 financing 때문에 AT&T가 6년 저점과 6% dividend yield에 거래되지만 cash economics는 시장 우려보다 좋다고 봤다. TWX는 낮은 capital intensity의 콘텐츠 EBITDA를 추가하고, combined FCF로 약 3.2x net debt를 수년 내 2.5x 아래로 낮출 수 있다고 주장했다. DOJ appeal은 약하고 배당도 충분히 커버되므로 downside가 제한적이라고 봤다.

**이 주장이 성립하려면**

콘텐츠 earnings 안정

**사전 반증조건**

cord-cutting/streaming investment가 FCF 훼손

**실제 결과**

단기 combined FCF는 크게 증가했다.

**정량적 괴리**

주가 / $31.97 / $40 / 2019말 $39.08

**분석 오류·핵심**

핵심 causal chain은 실제 결과에서 확인됐다. 다만 그 성공이 증권 payoff의 원인이었는지는 별도 판정한다.

**재사용할 교훈**

TWX cash conversion 가설은 'cord-cutting/streaming investment가 FCF 훼손'를 사전 반증조건으로 저장하고 사업·이벤트·가격 판정을 분리한다.

#### 2. Deleveraging — 강한 적중 · 논지 비중 18%

**당시 주장**

높은 FCF로 3.2x debt를 2.5x 아래 방향으로 빠르게 낮춘다.

**당시 근거**

Time Warner 인수, DOJ appeal, 거래 financing 때문에 AT&T가 6년 저점과 6% dividend yield에 거래되지만 cash economics는 시장 우려보다 좋다고 봤다. TWX는 낮은 capital intensity의 콘텐츠 EBITDA를 추가하고, combined FCF로 약 3.2x net debt를 수년 내 2.5x 아래로 낮출 수 있다고 주장했다. DOJ appeal은 약하고 배당도 충분히 커버되므로 downside가 제한적이라고 봤다.

**이 주장이 성립하려면**

자산매각·FCF가 debt에 우선 배분

**사전 반증조건**

M&A/배당이 cash를 소진

**실제 결과**

2019말 약 2.5x까지 낮아졌다.

**정량적 괴리**

FCF / 2018E 강한 cash / $20bn+ 지속 / 2018 $22.4bn; 2019 $29bn

**분석 오류·핵심**

핵심 causal chain은 실제 결과에서 확인됐다. 다만 그 성공이 증권 payoff의 원인이었는지는 별도 판정한다.

**재사용할 교훈**

Deleveraging 가설은 'M&A/배당이 cash를 소진'를 사전 반증조건으로 저장하고 사업·이벤트·가격 판정을 분리한다.

#### 3. Dividend floor — 적중 · 논지 비중 16%

**당시 주장**

6% dividend가 충분히 FCF로 커버돼 downside를 지지한다.

**당시 근거**

Time Warner 인수, DOJ appeal, 거래 financing 때문에 AT&T가 6년 저점과 6% dividend yield에 거래되지만 cash economics는 시장 우려보다 좋다고 봤다. TWX는 낮은 capital intensity의 콘텐츠 EBITDA를 추가하고, combined FCF로 약 3.2x net debt를 수년 내 2.5x 아래로 낮출 수 있다고 주장했다. DOJ appeal은 약하고 배당도 충분히 커버되므로 downside가 제한적이라고 봤다.

**이 주장이 성립하려면**

FCF payout 여유

**사전 반증조건**

FCF 급락·dividend cut

**실제 결과**

해당 horizon에서는 dividend 유지.

**정량적 괴리**

Net leverage / 약 3.2x / 수년 내 <2.5x / 2019말 약 2.5x

**분석 오류·핵심**

핵심 causal chain은 실제 결과에서 확인됐다. 다만 그 성공이 증권 payoff의 원인이었는지는 별도 판정한다.

**재사용할 교훈**

Dividend floor 가설은 'FCF 급락·dividend cut'를 사전 반증조건으로 저장하고 사업·이벤트·가격 판정을 분리한다.

#### 4. DOJ appeal — 적중 · 논지 비중 16%

**당시 주장**

Time Warner antitrust appeal risk가 과도하다.

**당시 근거**

Time Warner 인수, DOJ appeal, 거래 financing 때문에 AT&T가 6년 저점과 6% dividend yield에 거래되지만 cash economics는 시장 우려보다 좋다고 봤다. TWX는 낮은 capital intensity의 콘텐츠 EBITDA를 추가하고, combined FCF로 약 3.2x net debt를 수년 내 2.5x 아래로 낮출 수 있다고 주장했다. DOJ appeal은 약하고 배당도 충분히 커버되므로 downside가 제한적이라고 봤다.

**이 주장이 성립하려면**

법원 판결 유지

**사전 반증조건**

거래 unwind

**실제 결과**

DOJ appeal이 거래를 무너뜨리지 못했다.

**정량적 괴리**

Time Warner / $9bn+ EBITDA / 낮은 CapEx / cash accretion / 단기 cash 기여, 2022 분리

**분석 오류·핵심**

핵심 causal chain은 실제 결과에서 확인됐다. 다만 그 성공이 증권 payoff의 원인이었는지는 별도 판정한다.

**재사용할 교훈**

DOJ appeal 가설은 '거래 unwind'를 사전 반증조건으로 저장하고 사업·이벤트·가격 판정을 분리한다.

#### 5. Strategic fit — 부분 실패 · 논지 비중 16%

**당시 주장**

통신+미디어 결합이 장기 가치파괴를 만들지 않는다.

**당시 근거**

Time Warner 인수, DOJ appeal, 거래 financing 때문에 AT&T가 6년 저점과 6% dividend yield에 거래되지만 cash economics는 시장 우려보다 좋다고 봤다. TWX는 낮은 capital intensity의 콘텐츠 EBITDA를 추가하고, combined FCF로 약 3.2x net debt를 수년 내 2.5x 아래로 낮출 수 있다고 주장했다. DOJ appeal은 약하고 배당도 충분히 커버되므로 downside가 제한적이라고 봤다.

**이 주장이 성립하려면**

cross-platform 시너지와 낮은 debt

**사전 반증조건**

복합기업 할인·전략철회

**실제 결과**

WarnerMedia는 결국 분리됐다.

**정량적 괴리**

2019년 말 약 $39.08로 $40 목표에 거의 도달했고 높은 배당까지 포함하면 18개월 성과는 좋았다. 이후 Time Warner/DirecTV 전략은 결국 분리로 되돌려졌다.

**분석 오류·핵심**

좋은 자산·평균 operating path를 equity payoff에 직접 연결하거나, debt·integration·corporate action·timing의 joint distribution을 충분히 stress하지 않았다.

**재사용할 교훈**

Strategic fit 가설은 '복합기업 할인·전략철회'를 사전 반증조건으로 저장하고 사업·이벤트·가격 판정을 분리한다.

#### 6. $40 target — 성공 · 논지 비중 16%

**당시 주장**

cash flow와 12x/5% yield 기준 $40 가능.

**당시 근거**

Time Warner 인수, DOJ appeal, 거래 financing 때문에 AT&T가 6년 저점과 6% dividend yield에 거래되지만 cash economics는 시장 우려보다 좋다고 봤다. TWX는 낮은 capital intensity의 콘텐츠 EBITDA를 추가하고, combined FCF로 약 3.2x net debt를 수년 내 2.5x 아래로 낮출 수 있다고 주장했다. DOJ appeal은 약하고 배당도 충분히 커버되므로 downside가 제한적이라고 봤다.

**이 주장이 성립하려면**

deleveraging+multiple 안정

**사전 반증조건**

FCF miss

**실제 결과**

2019말 $39.08로 사실상 달성.

**정량적 괴리**

2019년 말 약 $39.08로 $40 목표에 거의 도달했고 높은 배당까지 포함하면 18개월 성과는 좋았다. 이후 Time Warner/DirecTV 전략은 결국 분리로 되돌려졌다.

**분석 오류·핵심**

핵심 causal chain은 실제 결과에서 확인됐다. 다만 그 성공이 증권 payoff의 원인이었는지는 별도 판정한다.

**재사용할 교훈**

$40 target 가설은 'FCF miss'를 사전 반증조건으로 저장하고 사업·이벤트·가격 판정을 분리한다.

### 6. 실제 사업의 시간순 전개

단기 cash-flow/deleveraging은 실제로 잘 됐다. 2018 FCF는 $22.4bn, 2019 FCF는 $29bn이었고 회사는 TWX close 이후 net debt를 약 $30bn 줄여 2019년 말 leverage를 약 2.5x로 낮췄다. 주가도 2019말 $39.08로 $40 target에 거의 도달했다. 그러나 장기적으로 DirecTV와 WarnerMedia 결합은 복합기업 할인·부채·전략적 복잡성을 남겼고 결국 WarnerMedia를 2022년 분리했다.

### 7. 사업 결과와 가격 결과 분리

증권 결과는 2019년 말 약 $39.08로 $40 목표에 거의 도달했고 높은 배당까지 포함하면 18개월 성과는 좋았다. 이후 Time Warner/DirecTV 전략은 결국 분리로 되돌려졌다. 사업논지·촉매·valuation·corporate structure와 주가를 서로 다른 판정으로 저장한다.

### 8. 무엇을 잘 봤고 무엇을 놓쳤나

이 글은 '좋은/나쁜 M&A'를 추상적으로 논하기보다 acquired EBITDA와 CapEx를 cash conversion으로 연결한 점이 좋았다. 단기 cash-generation과 deleveraging은 정확했다. 다만 거래가 현금흐름에 accretive하다는 것과 장기 ROIC·corporate fit이 좋다는 것은 다른 문제다. 결국 Warner 분리는 strategic thesis가 완전히 성공하지 않았음을 보여준다.

### 9. 최초 검증·반증 신호와 회피 가능성

2020-01-29 — FY2019 FCF $29bn과 net debt 약 $30bn 감소, leverage 약 2.5x가 발표돼 단기 deleveraging thesis가 수치로 확인됐다. 이 시점에 원 valuation bridge를 다시 만들면 operating thesis와 security thesis 중 무엇이 살아있는지 구분할 수 있었다. 회피 가능성: 핵심 18개월 Long은 성공했다. 이후 보유하려면 debt 감소만이 아니라 DirecTV subscriber decline과 WarnerMedia의 strategic fit을 새 thesis로 다시 평가했어야 한다.

### 10. 최종 판정·반사실·재사용 교훈

가격·현금흐름 성공 / 전략적 M&A 평가는 혼합. Telecom에서는 좋은 spectrum·좋은 콘텐츠·높은 FCF 하나만으로 equity floor를 만들지 않고, 실제 고객경제성·부채·corporate-action 귀속구조를 함께 stress해야 한다.

### 핵심 수치 — 당시 vs 실제

| 지표 | 글 당시 | VIC 기대 | 실제 | 판정 |
|---|---|---|---|---|
| 주가 | $31.97 | $40 | 2019말 $39.08 | 거의 적중 |
| FCF | 2018E 강한 cash | $20bn+ 지속 | 2018 $22.4bn; 2019 $29bn | 강한 적중 |
| Net leverage | 약 3.2x | 수년 내 <2.5x | 2019말 약 2.5x | 적중 |
| Time Warner | $9bn+ EBITDA / 낮은 CapEx | cash accretion | 단기 cash 기여, 2022 분리 | 운영 적중·전략 혼합 |

### 사건 타임라인

| 시점 | 사건 | 논지에 대한 의미 |
|---|---|---|
| 2018-07-16 | VIC 아이디어 게시 | Time Warner cash-flow·deleveraging·$40 Long |
| 2020-01-29 | 최초 핵심 검증·반증 신호 | FY2019 FCF $29bn과 net debt 약 $30bn 감소, leverage 약 2.5x가 발표돼 단기 deleveraging thesis가 수치로 확인됐다. |
| 2020-12-31 | Cash flow·HBO·wireless 점검 | 2020 FCF와 HBO Max subscriber, postpaid trends 재검증 |
| 2021-05-17 | WarnerMedia 구조변경 발표 | AT&T conglomerate thesis가 통신 stub + WBD 분배가치로 변환 |
| 2022-04-08 | WarnerMedia/Discovery 거래 종결 | AT&T 1주당 0.241917 WBD 분배 |
| 2024-01-31 | 고정 사후평가 | 2019년 말 약 $39.08로 $40 목표에 거의 도달했고 높은 배당까지 포함하면 18개월 성과는 좋았다. 이후 Time Warner/DirecTV 전략은 결국 분리로 되돌려졌다. |

### Failure / Success Anatomy

- **근본 오류:** 핵심 causal chain은 상당 부분 맞았으나 operating success·event success·security payoff를 계속 분리해야 함
- **최초 검증·반증 신호:** 2020-01-29 — FY2019 FCF $29bn과 net debt 약 $30bn 감소, leverage 약 2.5x가 발표돼 단기 deleveraging thesis가 수치로 확인됐다.
- **당시 알 수 있었나:** 가입자 순증·churn·ARPU·service revenue·EBITDA·CapEx·FCF·gross debt·maturities·spectrum 사용·corporate-action 조건은 공시와 earnings에서 재검증 가능했다.
- **피할 수 있었나:** 핵심 18개월 Long은 성공했다. 이후 보유하려면 debt 감소만이 아니라 DirecTV subscriber decline과 WarnerMedia의 strategic fit을 새 thesis로 다시 평가했어야 한다.
- **반사실 질문:** spectrum·segment business가 가치 있어도 integration, debt, corporate action 또는 security horizon이 반대로 움직이면 기존 보통주/스프레드의 payoff는 어떻게 달라지는가?
- **성공 패턴:** subscription_cash_flow; deleveraging; fiber_growth; content_optionality; event_restructuring
- **실패·주의 패턴:** conglomerate_discount; m_and_a_roic; fcf_quality; corporate_structure_change; dividend_floor_error

### 주요 근거자료

- [1. VIC T 2018-07-16 원문](https://www.valueinvestorsclub.com/idea/ATandamp%3BT_INC/8453290676) — Value Investors Club, 2018-07-16. 원 SQL description에서 당시 thesis·valuation·risk·catalyst·방향을 복원
- [2. AT&T FY2018 Results](https://about.att.com/story/2019/att_4q_earnings_2018.html) — AT&T, 2019-01-30. 2018 free cash flow $22.4bn·CapEx·deleveraging 확인
- [3. AT&T FY2019 Results](https://about.att.com/story/2020/4q_2019_earnings.html) — AT&T, 2020-01-29. 2019 FCF $29bn·net debt 약 $30bn 감소·leverage 약 2.5x 확인
- [4. AT&T FY2020 Results](https://about.att.com/story/2021/4q_2020_earnings.html) — AT&T, 2021-01-27. 2020 FCF $27.5bn·domestic HBO Max/HBO 41m+ 확인
- [5. AT&T Analyst Day 2021](https://about.att.com/story/2021/analyst_day_2021.html) — AT&T, 2021-03-12. HBO Max/HBO 2025 global target 120~150m·fiber build 확대 확인
- [6. AT&T and Discovery combine WarnerMedia and Discovery](https://about.att.com/story/2021/warnermedia_discovery.html) — AT&T, 2021-05-17. WarnerMedia 분리·Discovery 결합 발표
- [7. AT&T FY2021 Results](https://about.att.com/story/2022/fy_2021_earnings.html) — AT&T, 2022-01-26. 2021 wireless/fiber net adds·HBO/HBO Max 73.8m 확인
- [8. Warner Bros. Discovery transaction closes](https://about.att.com/story/2022/close-warnermedia-transaction.html) — AT&T, 2022-04-08. AT&T 1주당 0.241917 WBD 분배·거래종결 확인
- [9. AT&T FY2023 Results](https://about.att.com/story/2024/4q-earnings-2023.html) — AT&T, 2024-01-24. 2023 FCF·net debt·fiber/5G 장기상태 확인
- [10. AT&T historical prices](https://www.digrin.com/stocks/detail/T/price) — Digrin, 2024-01-31. 2018~2024 raw historical price 교차검증
- [11. Warner Bros. Discovery historical prices](https://www.digrin.com/stocks/detail/WBD/price) — Digrin, 2024-01-31. 2024-01 분배주식 가치 교차검증


---

<!-- idea:125eeb45-b6d3-4334-b245-8ed7b4dcbd0f -->
## 2. 2020-01-29 — FCF quality·DirecTV decline·2022 guidance skepticism Short

### 결론부터

**종합판정: 가격 성공·인과 혼합.** 좋은 Short 사후분석의 핵심은 주가 하락만으로 논지를 성공 처리하지 않는 것이다. DirecTV·off-balance obligations·capital allocation 비판은 유효했지만 2020의 실제 주가하락에는 pandemic shock이 컸고, wireless·FCF는 예상보다 방어적이었다. causal attribution을 분리해야 한다.

**주가·증권 결과:** 2020년 3월 COVID 충격 때 $30 아래로 급락했고 2020년 말도 약 $28.75로 $26~30 target zone에 근접. 가격 방향은 성공했지만 pandemic이라는 외생요인이 컸고 wireless는 예상보다 강했다.

**Thesis / Process 점수:** 8 / 8

### 1. 무슨 기업인가

AT&T는 미국의 대형 통신사업자로 wireless, fiber broadband와 기업통신을 중심으로 현금흐름을 창출한다. 다만 2015 DirecTV, 2018 Time Warner 인수로 한동안 미디어·위성TV까지 포함한 거대한 복합기업이 되었고, 2021~22 WarnerMedia/Discovery 거래와 DirecTV 분리를 통해 다시 통신 중심으로 축소됐다. Wireless에서는 postpaid phone subscribers·ARPU·churn·network CapEx·spectrum이 핵심이고, fiber에서는 passings·net adds·penetration·ARPU와 build cost가 중요하다. 미디어 보유기에는 HBO/HBO Max subscriber growth, content spend, advertising, distribution economics도 equity value를 좌우했다. AT&T의 VIC 역사는 특히 '현금흐름은 맞았지만 M&A의 전략적 질이 틀린 경우', 'HBO Max 운영지표는 맞았지만 corporate structure가 바뀐 경우', '높은 dividend yield가 downside floor가 아닌 경우'를 잘 보여준다.

### 2. 산업 가치사슬과 돈의 흐름

AT&T의 핵심 현금창출은 wireless와 broadband subscription이다. Service revenue에서 network operating cost, sales, handset subsidy/financing, customer care와 SG&A를 차감해 EBITDA가 나오고, 여기서 spectrum·fiber·5G CapEx, interest, taxes, working capital을 차감하면 FCF가 된다. Time Warner 보유기에는 HBO·Turner·Warner Bros의 subscription, advertising, licensing, theatrical economics가 추가되었다. 그러나 높은 부채 때문에 EBITDA가 늘어도 debt service와 mandatory CapEx가 크면 equity FCF가 제한될 수 있다. 특히 AT&T는 asset sales, receivables factoring, vendor financing, DirecTV economics 등으로 headline FCF와 underlying cash conversion의 차이를 따져야 했다.

### 3. 경쟁우위·경쟁구도·핵심 지표

AT&T의 주요 우위는 전국 무선망·spectrum·distribution·기업고객·fiber footprint와 방대한 customer base다. 하지만 wireless는 Verizon·T-Mobile과 지속 경쟁하며, DirecTV·WarnerMedia 같은 비통신 자산은 통신 moat와 별개로 자본배분의 질을 요구한다. 2018~21의 핵심 질문은 'Time Warner가 좋은 콘텐츠 자산인가'보다 'AT&T 안에서 높은 부채와 복합기업 할인까지 감안했을 때 주당가치를 높이는가'였다. 2021 이후에는 Warner 분리로 그 질문 자체가 사라졌다. 따라서 통신 operating metrics, FCF와 동시에 net debt, dividend coverage, M&A·spin 구조와 기존 주주에게 귀속되는 분배가치를 추적해야 한다.

### 4. 당시 VIC 원문과 핵심 숫자

2019 주가가 dividend 포함 48% 오른 뒤 시장이 deleveraging과 Elliott activism을 과대평가했다고 봤다. DirecTV/Entertainment EBITDA decline, aggressive 2022 EPS $4.50~4.80 guidance, vague cost cuts, factoring·working-capital·vendor financing 등으로 FCF가 과장돼 있다고 주장했다. 5G/wireless 경쟁과 HBO Max 투자까지 고려하면 multiple이 다시 낮아질 가능성이 크다고 봤다.

### 5. 밸류에이션과 기대수익의 연결

회사 headline FCF $28bn의 quality를 의심하고 true run-rate를 약 $23bn으로 조정. off-balance-sheet/external liabilities 약 $41.5bn을 반영해 6x EV/EBITDA fair value $26.39, 두 해 dividend를 더한 $30.55로 약 18% downside. 사후에는 subscriber/churn/ARPU 또는 segment earnings → EBITDA → CapEx·interest → FCF → debt·corporate action → 기존 보통주 또는 merger spread payoff 순으로 다시 연결해 검증했다.

### 투자논지를 구성한 핵심 주장

#### 1. FCF quality — 실패/과장 · 논지 비중 18%

**당시 주장**

$28bn headline FCF는 factoring·working capital로 과장돼 true run-rate $23bn에 가깝다.

**당시 근거**

2019 주가가 dividend 포함 48% 오른 뒤 시장이 deleveraging과 Elliott activism을 과대평가했다고 봤다. DirecTV/Entertainment EBITDA decline, aggressive 2022 EPS $4.50~4.80 guidance, vague cost cuts, factoring·working-capital·vendor financing 등으로 FCF가 과장돼 있다고 주장했다. 5G/wireless 경쟁과 HBO Max 투자까지 고려하면 multiple이 다시 낮아질 가능성이 크다고 봤다.

**이 주장이 성립하려면**

일회성 cash levers reversal

**사전 반증조건**

반복가능 FCF $27bn+

**실제 결과**

2020 FCF는 $27.5bn으로 높은 수준을 유지.

**정량적 괴리**

주가 / $37.62 / $26.39 + dividends / 2020말 약 $28.75

**분석 오류·핵심**

좋은 자산·평균 operating path를 equity payoff에 직접 연결하거나, debt·integration·corporate action·timing의 joint distribution을 충분히 stress하지 않았다.

**재사용할 교훈**

FCF quality 가설은 '반복가능 FCF $27bn+'를 사전 반증조건으로 저장하고 사업·이벤트·가격 판정을 분리한다.

#### 2. DirecTV decline — 적중 · 논지 비중 18%

**당시 주장**

Entertainment subscriber loss와 margin pressure가 계속된다.

**당시 근거**

2019 주가가 dividend 포함 48% 오른 뒤 시장이 deleveraging과 Elliott activism을 과대평가했다고 봤다. DirecTV/Entertainment EBITDA decline, aggressive 2022 EPS $4.50~4.80 guidance, vague cost cuts, factoring·working-capital·vendor financing 등으로 FCF가 과장돼 있다고 주장했다. 5G/wireless 경쟁과 HBO Max 투자까지 고려하면 multiple이 다시 낮아질 가능성이 크다고 봤다.

**이 주장이 성립하려면**

cord cutting 지속

**사전 반증조건**

DTV stabilization

**실제 결과**

구조적 decline과 후일 분리가 현실화됐다.

**정량적 괴리**

FCF / headline $28bn / true $23bn 주장 / quality 악화 / 2020 $27.5bn

**분석 오류·핵심**

핵심 causal chain은 실제 결과에서 확인됐다. 다만 그 성공이 증권 payoff의 원인이었는지는 별도 판정한다.

**재사용할 교훈**

DirecTV decline 가설은 'DTV stabilization'를 사전 반증조건으로 저장하고 사업·이벤트·가격 판정을 분리한다.

#### 3. 2022 guidance — 방향 적중 · 논지 비중 16%

**당시 주장**

$4.50~4.80 EPS guidance는 aggressive하다.

**당시 근거**

2019 주가가 dividend 포함 48% 오른 뒤 시장이 deleveraging과 Elliott activism을 과대평가했다고 봤다. DirecTV/Entertainment EBITDA decline, aggressive 2022 EPS $4.50~4.80 guidance, vague cost cuts, factoring·working-capital·vendor financing 등으로 FCF가 과장돼 있다고 주장했다. 5G/wireless 경쟁과 HBO Max 투자까지 고려하면 multiple이 다시 낮아질 가능성이 크다고 봤다.

**이 주장이 성립하려면**

cost cuts·growth 목표 미달

**사전 반증조건**

사업개선으로 달성경로 유지

**실제 결과**

pandemic과 portfolio 변화로 원 계획은 의미가 약해졌다.

**정량적 괴리**

DirecTV / 구조적 decline / Entertainment 압박 / 후일 stake sale·분리

**분석 오류·핵심**

핵심 causal chain은 실제 결과에서 확인됐다. 다만 그 성공이 증권 payoff의 원인이었는지는 별도 판정한다.

**재사용할 교훈**

2022 guidance 가설은 '사업개선으로 달성경로 유지'를 사전 반증조건으로 저장하고 사업·이벤트·가격 판정을 분리한다.

#### 4. External liabilities — 부분 적중 · 논지 비중 16%

**당시 주장**

off-balance obligations까지 보면 leverage가 headline보다 높다.

**당시 근거**

2019 주가가 dividend 포함 48% 오른 뒤 시장이 deleveraging과 Elliott activism을 과대평가했다고 봤다. DirecTV/Entertainment EBITDA decline, aggressive 2022 EPS $4.50~4.80 guidance, vague cost cuts, factoring·working-capital·vendor financing 등으로 FCF가 과장돼 있다고 주장했다. 5G/wireless 경쟁과 HBO Max 투자까지 고려하면 multiple이 다시 낮아질 가능성이 크다고 봤다.

**이 주장이 성립하려면**

부채성 의무가 현금흐름을 소진

**사전 반증조건**

자산매각/FCF로 충분히 상쇄

**실제 결과**

높은 leverage와 portfolio 정리가 장기 핵심 이슈였다.

**정량적 괴리**

Wireless / 경쟁 악화 우려 / 압박 / 2020 strong postpaid performance

**분석 오류·핵심**

핵심 causal chain은 실제 결과에서 확인됐다. 다만 그 성공이 증권 payoff의 원인이었는지는 별도 판정한다.

**재사용할 교훈**

External liabilities 가설은 '자산매각/FCF로 충분히 상쇄'를 사전 반증조건으로 저장하고 사업·이벤트·가격 판정을 분리한다.

#### 5. Wireless pressure — 실패 · 논지 비중 16%

**당시 주장**

5G 경쟁이 wireless economics를 압박한다.

**당시 근거**

2019 주가가 dividend 포함 48% 오른 뒤 시장이 deleveraging과 Elliott activism을 과대평가했다고 봤다. DirecTV/Entertainment EBITDA decline, aggressive 2022 EPS $4.50~4.80 guidance, vague cost cuts, factoring·working-capital·vendor financing 등으로 FCF가 과장돼 있다고 주장했다. 5G/wireless 경쟁과 HBO Max 투자까지 고려하면 multiple이 다시 낮아질 가능성이 크다고 봤다.

**이 주장이 성립하려면**

T-Mobile share gain·ARPU 압박

**사전 반증조건**

AT&T postpaid strength

**실제 결과**

2020 wireless는 예상보다 강했다.

**정량적 괴리**

2020년 3월 COVID 충격 때 $30 아래로 급락했고 2020년 말도 약 $28.75로 $26~30 target zone에 근접. 가격 방향은 성공했지만 pandemic이라는 외생요인이 컸고 wireless는 예상보다 강했다.

**분석 오류·핵심**

좋은 자산·평균 operating path를 equity payoff에 직접 연결하거나, debt·integration·corporate action·timing의 joint distribution을 충분히 stress하지 않았다.

**재사용할 교훈**

Wireless pressure 가설은 'AT&T postpaid strength'를 사전 반증조건으로 저장하고 사업·이벤트·가격 판정을 분리한다.

#### 6. $26~30 price — 가격 적중·인과 혼합 · 논지 비중 16%

**당시 주장**

6x EV/EBITDA와 dividend를 고려해 약 18% downside.

**당시 근거**

2019 주가가 dividend 포함 48% 오른 뒤 시장이 deleveraging과 Elliott activism을 과대평가했다고 봤다. DirecTV/Entertainment EBITDA decline, aggressive 2022 EPS $4.50~4.80 guidance, vague cost cuts, factoring·working-capital·vendor financing 등으로 FCF가 과장돼 있다고 주장했다. 5G/wireless 경쟁과 HBO Max 투자까지 고려하면 multiple이 다시 낮아질 가능성이 크다고 봤다.

**이 주장이 성립하려면**

multiple 압축·business 우려

**사전 반증조건**

defensive FCF가 floor 제공

**실제 결과**

COVID 포함 2020에 목표 zone 접근.

**정량적 괴리**

2020년 3월 COVID 충격 때 $30 아래로 급락했고 2020년 말도 약 $28.75로 $26~30 target zone에 근접. 가격 방향은 성공했지만 pandemic이라는 외생요인이 컸고 wireless는 예상보다 강했다.

**분석 오류·핵심**

핵심 causal chain은 실제 결과에서 확인됐다. 다만 그 성공이 증권 payoff의 원인이었는지는 별도 판정한다.

**재사용할 교훈**

$26~30 price 가설은 'defensive FCF가 floor 제공'를 사전 반증조건으로 저장하고 사업·이벤트·가격 판정을 분리한다.

### 6. 실제 사업의 시간순 전개

주가는 2020년에 큰 폭 하락해 Short 가격 목표는 작동했다. 그러나 회사는 COVID 속에서도 2020 FCF $27.5bn을 기록했고 domestic HBO Max/HBO는 41m+가 됐다. Wireless도 강한 postpaid trends를 보였다. 반면 DirecTV decline·높은 debt·portfolio complexity와 capital allocation 비판은 이후 WarnerMedia/DirecTV 분리로 상당 부분 확인됐다. 즉 결과는 맞았지만 COVID가 큰 역할을 했고 headline FCF가 즉시 $23bn으로 무너진 것은 아니었다.

### 7. 사업 결과와 가격 결과 분리

증권 결과는 2020년 3월 COVID 충격 때 $30 아래로 급락했고 2020년 말도 약 $28.75로 $26~30 target zone에 근접. 가격 방향은 성공했지만 pandemic이라는 외생요인이 컸고 wireless는 예상보다 강했다. 사업논지·촉매·valuation·corporate structure와 주가를 서로 다른 판정으로 저장한다.

### 8. 무엇을 잘 봤고 무엇을 놓쳤나

좋은 Short 사후분석의 핵심은 주가 하락만으로 논지를 성공 처리하지 않는 것이다. DirecTV·off-balance obligations·capital allocation 비판은 유효했지만 2020의 실제 주가하락에는 pandemic shock이 컸고, wireless·FCF는 예상보다 방어적이었다. causal attribution을 분리해야 한다.

### 9. 최초 검증·반증 신호와 회피 가능성

2020-03-23 — COVID market crash로 주가가 $30 아래로 내려 목표가격에 접근했지만 이는 원문이 예상한 AT&T 고유의 operating deterioration과는 다른 외생경로였다. 이 시점에 원 valuation bridge를 다시 만들면 operating thesis와 security thesis 중 무엇이 살아있는지 구분할 수 있었다. 회피 가능성: Short 수익은 실현 가능했지만, 2020 FCF $27.5bn과 strong wireless가 나온 뒤에는 operating thesis의 일부가 틀렸음을 인정하고 이유를 재분류했어야 한다.

### 10. 최종 판정·반사실·재사용 교훈

가격 성공·인과 혼합. Telecom에서는 좋은 spectrum·좋은 콘텐츠·높은 FCF 하나만으로 equity floor를 만들지 않고, 실제 고객경제성·부채·corporate-action 귀속구조를 함께 stress해야 한다.

### 핵심 수치 — 당시 vs 실제

| 지표 | 글 당시 | VIC 기대 | 실제 | 판정 |
|---|---|---|---|---|
| 주가 | $37.62 | $26.39 + dividends | 2020말 약 $28.75 | 가격 성공 |
| FCF | headline $28bn / true $23bn 주장 | quality 악화 | 2020 $27.5bn | 운영 가정 미달 |
| DirecTV | 구조적 decline | Entertainment 압박 | 후일 stake sale·분리 | 적중 |
| Wireless | 경쟁 악화 우려 | 압박 | 2020 strong postpaid performance | 부분 실패 |

### 사건 타임라인

| 시점 | 사건 | 논지에 대한 의미 |
|---|---|---|
| 2020-01-29 | VIC 아이디어 게시 | FCF quality·DirecTV decline·2022 guidance skepticism Short |
| 2020-03-23 | 최초 핵심 검증·반증 신호 | COVID market crash로 주가가 $30 아래로 내려 목표가격에 접근했지만 이는 원문이 예상한 AT&T 고유의 operating deterioration과는 다른 외생경로였다. |
| 2020-12-31 | Cash flow·HBO·wireless 점검 | 2020 FCF와 HBO Max subscriber, postpaid trends 재검증 |
| 2021-05-17 | WarnerMedia 구조변경 발표 | AT&T conglomerate thesis가 통신 stub + WBD 분배가치로 변환 |
| 2022-04-08 | WarnerMedia/Discovery 거래 종결 | AT&T 1주당 0.241917 WBD 분배 |
| 2024-01-31 | 고정 사후평가 | 2020년 3월 COVID 충격 때 $30 아래로 급락했고 2020년 말도 약 $28.75로 $26~30 target zone에 근접. 가격 방향은 성공했지만 pandemic이라는 외생요인이 컸고 wireless는 예상보다 강했다. |

### Failure / Success Anatomy

- **근본 오류:** 핵심 causal chain은 상당 부분 맞았으나 operating success·event success·security payoff를 계속 분리해야 함
- **최초 검증·반증 신호:** 2020-03-23 — COVID market crash로 주가가 $30 아래로 내려 목표가격에 접근했지만 이는 원문이 예상한 AT&T 고유의 operating deterioration과는 다른 외생경로였다.
- **당시 알 수 있었나:** 가입자 순증·churn·ARPU·service revenue·EBITDA·CapEx·FCF·gross debt·maturities·spectrum 사용·corporate-action 조건은 공시와 earnings에서 재검증 가능했다.
- **피할 수 있었나:** Short 수익은 실현 가능했지만, 2020 FCF $27.5bn과 strong wireless가 나온 뒤에는 operating thesis의 일부가 틀렸음을 인정하고 이유를 재분류했어야 한다.
- **반사실 질문:** spectrum·segment business가 가치 있어도 integration, debt, corporate action 또는 security horizon이 반대로 움직이면 기존 보통주/스프레드의 payoff는 어떻게 달라지는가?
- **성공 패턴:** subscription_cash_flow; deleveraging; fiber_growth; content_optionality; event_restructuring
- **실패·주의 패턴:** conglomerate_discount; m_and_a_roic; fcf_quality; corporate_structure_change; dividend_floor_error

### 주요 근거자료

- [1. VIC T 2020-01-29 원문](https://www.valueinvestorsclub.com/idea/ATandamp%3BT_INC/9216541182) — Value Investors Club, 2020-01-29. 원 SQL description에서 당시 thesis·valuation·risk·catalyst·방향을 복원
- [2. AT&T FY2018 Results](https://about.att.com/story/2019/att_4q_earnings_2018.html) — AT&T, 2019-01-30. 2018 free cash flow $22.4bn·CapEx·deleveraging 확인
- [3. AT&T FY2019 Results](https://about.att.com/story/2020/4q_2019_earnings.html) — AT&T, 2020-01-29. 2019 FCF $29bn·net debt 약 $30bn 감소·leverage 약 2.5x 확인
- [4. AT&T FY2020 Results](https://about.att.com/story/2021/4q_2020_earnings.html) — AT&T, 2021-01-27. 2020 FCF $27.5bn·domestic HBO Max/HBO 41m+ 확인
- [5. AT&T Analyst Day 2021](https://about.att.com/story/2021/analyst_day_2021.html) — AT&T, 2021-03-12. HBO Max/HBO 2025 global target 120~150m·fiber build 확대 확인
- [6. AT&T and Discovery combine WarnerMedia and Discovery](https://about.att.com/story/2021/warnermedia_discovery.html) — AT&T, 2021-05-17. WarnerMedia 분리·Discovery 결합 발표
- [7. AT&T FY2021 Results](https://about.att.com/story/2022/fy_2021_earnings.html) — AT&T, 2022-01-26. 2021 wireless/fiber net adds·HBO/HBO Max 73.8m 확인
- [8. Warner Bros. Discovery transaction closes](https://about.att.com/story/2022/close-warnermedia-transaction.html) — AT&T, 2022-04-08. AT&T 1주당 0.241917 WBD 분배·거래종결 확인
- [9. AT&T FY2023 Results](https://about.att.com/story/2024/4q-earnings-2023.html) — AT&T, 2024-01-24. 2023 FCF·net debt·fiber/5G 장기상태 확인
- [10. AT&T historical prices](https://www.digrin.com/stocks/detail/T/price) — Digrin, 2024-01-31. 2018~2024 raw historical price 교차검증
- [11. Warner Bros. Discovery historical prices](https://www.digrin.com/stocks/detail/WBD/price) — Digrin, 2024-01-31. 2024-01 분배주식 가치 교차검증


---

<!-- idea:04a436a1-be2d-46d0-89c1-ea41a88e236b -->
## 3. 2021-01-03 — HBO Max subscriber surprise·$51~63.5 Long

### 결론부터

**종합판정: 운영촉매 적중·증권/기업구조 thesis 실패.** Variant perception은 맞았다. HBO Max subscriber expectations는 실제로 너무 낮았다. 그러나 '자회사 operating success → 모회사 P/E rerating' 사이에 capital structure·spin-off·management strategy라는 중간변수가 있었다. 특히 높은 부채를 가진 conglomerate에서 fastest-growing asset이 분리될 가능성을 전혀 고려하지 않았다.

**주가·증권 결과:** HBO Max subscriber thesis는 빠르게 적중했지만 AT&T는 2021-05 WarnerMedia 분리를 발표. 2024-01-31 AT&T $15.85 + 배분된 0.241917 WBD×$10.02 ≈ $18.27 before dividends로 원 entry와 $51~63 target을 크게 하회.

**Thesis / Process 점수:** 5.8 / 6.2

### 1. 무슨 기업인가

AT&T는 미국의 대형 통신사업자로 wireless, fiber broadband와 기업통신을 중심으로 현금흐름을 창출한다. 다만 2015 DirecTV, 2018 Time Warner 인수로 한동안 미디어·위성TV까지 포함한 거대한 복합기업이 되었고, 2021~22 WarnerMedia/Discovery 거래와 DirecTV 분리를 통해 다시 통신 중심으로 축소됐다. Wireless에서는 postpaid phone subscribers·ARPU·churn·network CapEx·spectrum이 핵심이고, fiber에서는 passings·net adds·penetration·ARPU와 build cost가 중요하다. 미디어 보유기에는 HBO/HBO Max subscriber growth, content spend, advertising, distribution economics도 equity value를 좌우했다. AT&T의 VIC 역사는 특히 '현금흐름은 맞았지만 M&A의 전략적 질이 틀린 경우', 'HBO Max 운영지표는 맞았지만 corporate structure가 바뀐 경우', '높은 dividend yield가 downside floor가 아닌 경우'를 잘 보여준다.

### 2. 산업 가치사슬과 돈의 흐름

AT&T의 핵심 현금창출은 wireless와 broadband subscription이다. Service revenue에서 network operating cost, sales, handset subsidy/financing, customer care와 SG&A를 차감해 EBITDA가 나오고, 여기서 spectrum·fiber·5G CapEx, interest, taxes, working capital을 차감하면 FCF가 된다. Time Warner 보유기에는 HBO·Turner·Warner Bros의 subscription, advertising, licensing, theatrical economics가 추가되었다. 그러나 높은 부채 때문에 EBITDA가 늘어도 debt service와 mandatory CapEx가 크면 equity FCF가 제한될 수 있다. 특히 AT&T는 asset sales, receivables factoring, vendor financing, DirecTV economics 등으로 headline FCF와 underlying cash conversion의 차이를 따져야 했다.

### 3. 경쟁우위·경쟁구도·핵심 지표

AT&T의 주요 우위는 전국 무선망·spectrum·distribution·기업고객·fiber footprint와 방대한 customer base다. 하지만 wireless는 Verizon·T-Mobile과 지속 경쟁하며, DirecTV·WarnerMedia 같은 비통신 자산은 통신 moat와 별개로 자본배분의 질을 요구한다. 2018~21의 핵심 질문은 'Time Warner가 좋은 콘텐츠 자산인가'보다 'AT&T 안에서 높은 부채와 복합기업 할인까지 감안했을 때 주당가치를 높이는가'였다. 2021 이후에는 Warner 분리로 그 질문 자체가 사라졌다. 따라서 통신 operating metrics, FCF와 동시에 net debt, dividend coverage, M&A·spin 구조와 기존 주주에게 귀속되는 분배가치를 추적해야 한다.

### 4. 당시 VIC 원문과 핵심 숫자

AT&T가 약 10x earnings와 높은 dividend yield에 거래돼 매우 싸며, 시장이 HBO Max subscriber trajectory를 크게 과소평가한다고 봤다. 약 3년 내 global 50m incremental subscribers가 $14.99/month로 추가되면 약 $0.76 EPS를 만들 수 있다고 단순 계산했고, 2021-01-27 실적발표에서 HBO Max subscriber beat가 valuation catalyst가 될 것이라 주장했다.

### 5. 밸류에이션과 기대수익의 연결

Historical P/E·P/B·S&P discount 등을 평균해 fair value 약 $51, 75%+ short-term upside. HBO Max가 성공하면 20x earnings 또는 추가 EPS value로 약 $63.5까지 가능하다고 봤다. 사후에는 subscriber/churn/ARPU 또는 segment earnings → EBITDA → CapEx·interest → FCF → debt·corporate action → 기존 보통주 또는 merger spread payoff 순으로 다시 연결해 검증했다.

### 투자논지를 구성한 핵심 주장

#### 1. HBO subscriber beat — 강한 적중 · 논지 비중 18%

**당시 주장**

HBO Max가 시장예상보다 훨씬 빨리 성장한다.

**당시 근거**

AT&T가 약 10x earnings와 높은 dividend yield에 거래돼 매우 싸며, 시장이 HBO Max subscriber trajectory를 크게 과소평가한다고 봤다. 약 3년 내 global 50m incremental subscribers가 $14.99/month로 추가되면 약 $0.76 EPS를 만들 수 있다고 단순 계산했고, 2021-01-27 실적발표에서 HBO Max subscriber beat가 valuation catalyst가 될 것이라 주장했다.

**이 주장이 성립하려면**

content·distribution이 subscriber adds로 연결

**사전 반증조건**

subscriber growth miss

**실제 결과**

41m+ domestic, 73.8m global로 강하게 적중.

**정량적 괴리**

HBO Max/HBO / 2020말 기대 상회 예상 / subscriber beat / 2020말 domestic 41m+; 2021말 global 73.8m

**분석 오류·핵심**

핵심 causal chain은 실제 결과에서 확인됐다. 다만 그 성공이 증권 payoff의 원인이었는지는 별도 판정한다.

**재사용할 교훈**

HBO subscriber beat 가설은 'subscriber growth miss'를 사전 반증조건으로 저장하고 사업·이벤트·가격 판정을 분리한다.

#### 2. Incremental EPS — 부분 · 논지 비중 18%

**당시 주장**

50m 추가 subs가 약 $0.76 EPS 가치가 된다.

**당시 근거**

AT&T가 약 10x earnings와 높은 dividend yield에 거래돼 매우 싸며, 시장이 HBO Max subscriber trajectory를 크게 과소평가한다고 봤다. 약 3년 내 global 50m incremental subscribers가 $14.99/month로 추가되면 약 $0.76 EPS를 만들 수 있다고 단순 계산했고, 2021-01-27 실적발표에서 HBO Max subscriber beat가 valuation catalyst가 될 것이라 주장했다.

**이 주장이 성립하려면**

ARPU $14.99와 margin economics 유지

**사전 반증조건**

콘텐츠비·국제 ARPU가 단순계산 훼손

**실제 결과**

subscriber growth는 맞았지만 단순 EPS conversion은 과도했다.

**정량적 괴리**

2025 target / 시장 기대 낮음 / 고성장 / 2021-03 120~150m로 상향

**분석 오류·핵심**

핵심 causal chain은 실제 결과에서 확인됐다. 다만 그 성공이 증권 payoff의 원인이었는지는 별도 판정한다.

**재사용할 교훈**

Incremental EPS 가설은 '콘텐츠비·국제 ARPU가 단순계산 훼손'를 사전 반증조건으로 저장하고 사업·이벤트·가격 판정을 분리한다.

#### 3. Valuation discount — 실패 · 논지 비중 16%

**당시 주장**

10x earnings 수준은 HBO optionality를 반영하지 않는다.

**당시 근거**

AT&T가 약 10x earnings와 높은 dividend yield에 거래돼 매우 싸며, 시장이 HBO Max subscriber trajectory를 크게 과소평가한다고 봤다. 약 3년 내 global 50m incremental subscribers가 $14.99/month로 추가되면 약 $0.76 EPS를 만들 수 있다고 단순 계산했고, 2021-01-27 실적발표에서 HBO Max subscriber beat가 valuation catalyst가 될 것이라 주장했다.

**이 주장이 성립하려면**

asset가 AT&T 안에서 계속 귀속

**사전 반증조건**

asset spin/divestiture

**실제 결과**

WarnerMedia가 분리돼 rerating bridge가 끊겼다.

**정량적 괴리**

주가 / $28.63 / $51~63.5 / 2024-01 package 약 $18.27 before dividends

**분석 오류·핵심**

좋은 자산·평균 operating path를 equity payoff에 직접 연결하거나, debt·integration·corporate action·timing의 joint distribution을 충분히 stress하지 않았다.

**재사용할 교훈**

Valuation discount 가설은 'asset spin/divestiture'를 사전 반증조건으로 저장하고 사업·이벤트·가격 판정을 분리한다.

#### 4. Dividend/downside — 실패 · 논지 비중 16%

**당시 주장**

높은 dividend와 낮은 P/E가 downside를 제한한다.

**당시 근거**

AT&T가 약 10x earnings와 높은 dividend yield에 거래돼 매우 싸며, 시장이 HBO Max subscriber trajectory를 크게 과소평가한다고 봤다. 약 3년 내 global 50m incremental subscribers가 $14.99/month로 추가되면 약 $0.76 EPS를 만들 수 있다고 단순 계산했고, 2021-01-27 실적발표에서 HBO Max subscriber beat가 valuation catalyst가 될 것이라 주장했다.

**이 주장이 성립하려면**

FCF·dividend structure 유지

**사전 반증조건**

spin 후 dividend reset

**실제 결과**

WarnerMedia 거래와 dividend cut/reset으로 floor 논리 훼손.

**정량적 괴리**

Corporate structure / Warner AT&T 내 가치 / 모회사 rerating / 2021-05 spin/Discovery merger 발표

**분석 오류·핵심**

좋은 자산·평균 operating path를 equity payoff에 직접 연결하거나, debt·integration·corporate action·timing의 joint distribution을 충분히 stress하지 않았다.

**재사용할 교훈**

Dividend/downside 가설은 'spin 후 dividend reset'를 사전 반증조건으로 저장하고 사업·이벤트·가격 판정을 분리한다.

#### 5. $51 fair value — 실패 · 논지 비중 16%

**당시 주장**

historical multiples 평균이 정상가치다.

**당시 근거**

AT&T가 약 10x earnings와 높은 dividend yield에 거래돼 매우 싸며, 시장이 HBO Max subscriber trajectory를 크게 과소평가한다고 봤다. 약 3년 내 global 50m incremental subscribers가 $14.99/month로 추가되면 약 $0.76 EPS를 만들 수 있다고 단순 계산했고, 2021-01-27 실적발표에서 HBO Max subscriber beat가 valuation catalyst가 될 것이라 주장했다.

**이 주장이 성립하려면**

과거 conglomerate 구조·yield가 재현

**사전 반증조건**

구조적 multiple reset

**실제 결과**

목표 미달.

**정량적 괴리**

HBO Max subscriber thesis는 빠르게 적중했지만 AT&T는 2021-05 WarnerMedia 분리를 발표. 2024-01-31 AT&T $15.85 + 배분된 0.241917 WBD×$10.02 ≈ $18.27 before dividends로 원 entry와 $51~63 target을 크게 하회.

**분석 오류·핵심**

좋은 자산·평균 operating path를 equity payoff에 직접 연결하거나, debt·integration·corporate action·timing의 joint distribution을 충분히 stress하지 않았다.

**재사용할 교훈**

$51 fair value 가설은 '구조적 multiple reset'를 사전 반증조건으로 저장하고 사업·이벤트·가격 판정을 분리한다.

#### 6. $63.5 bull — 실패 · 논지 비중 16%

**당시 주장**

HBO Max 성공 시 20x까지 rerating 가능.

**당시 근거**

AT&T가 약 10x earnings와 높은 dividend yield에 거래돼 매우 싸며, 시장이 HBO Max subscriber trajectory를 크게 과소평가한다고 봤다. 약 3년 내 global 50m incremental subscribers가 $14.99/month로 추가되면 약 $0.76 EPS를 만들 수 있다고 단순 계산했고, 2021-01-27 실적발표에서 HBO Max subscriber beat가 valuation catalyst가 될 것이라 주장했다.

**이 주장이 성립하려면**

HBO가 AT&T 내 growth mix를 바꿈

**사전 반증조건**

분리·conglomerate discount

**실제 결과**

운영은 성공했지만 모회사 rerating은 발생하지 않았다.

**정량적 괴리**

HBO Max subscriber thesis는 빠르게 적중했지만 AT&T는 2021-05 WarnerMedia 분리를 발표. 2024-01-31 AT&T $15.85 + 배분된 0.241917 WBD×$10.02 ≈ $18.27 before dividends로 원 entry와 $51~63 target을 크게 하회.

**분석 오류·핵심**

좋은 자산·평균 operating path를 equity payoff에 직접 연결하거나, debt·integration·corporate action·timing의 joint distribution을 충분히 stress하지 않았다.

**재사용할 교훈**

$63.5 bull 가설은 '분리·conglomerate discount'를 사전 반증조건으로 저장하고 사업·이벤트·가격 판정을 분리한다.

### 6. 실제 사업의 시간순 전개

운영촉매는 강하게 적중했다. 2020말 domestic HBO Max/HBO는 41m+로 초기 계획을 2년 앞섰고, 2021년 3월 회사는 2025 global HBO Max/HBO 목표를 75~90m에서 120~150m으로 상향했다. 2021말 글로벌 HBO Max/HBO는 73.8m이었다. 그러나 2021년 5월 AT&T는 WarnerMedia를 Discovery와 결합해 분리하기로 발표했다. 따라서 HBO Max 성공이 AT&T 내 multiple rerating으로 연결된다는 핵심 security bridge가 끊겼다.

### 7. 사업 결과와 가격 결과 분리

증권 결과는 HBO Max subscriber thesis는 빠르게 적중했지만 AT&T는 2021-05 WarnerMedia 분리를 발표. 2024-01-31 AT&T $15.85 + 배분된 0.241917 WBD×$10.02 ≈ $18.27 before dividends로 원 entry와 $51~63 target을 크게 하회. 사업논지·촉매·valuation·corporate structure와 주가를 서로 다른 판정으로 저장한다.

### 8. 무엇을 잘 봤고 무엇을 놓쳤나

Variant perception은 맞았다. HBO Max subscriber expectations는 실제로 너무 낮았다. 그러나 '자회사 operating success → 모회사 P/E rerating' 사이에 capital structure·spin-off·management strategy라는 중간변수가 있었다. 특히 높은 부채를 가진 conglomerate에서 fastest-growing asset이 분리될 가능성을 전혀 고려하지 않았다.

### 9. 최초 검증·반증 신호와 회피 가능성

2021-05-17 — AT&T가 WarnerMedia/Discovery 거래를 발표하면서 HBO Max가 AT&T valuation을 직접 끌어올린다는 thesis가 4개월 만에 구조적으로 무효화됐다. 이 시점에 원 valuation bridge를 다시 만들면 operating thesis와 security thesis 중 무엇이 살아있는지 구분할 수 있었다. 회피 가능성: 매우 높음. 5월 17일 발표 직후 기존 $51/$63.5 target을 폐기하고 AT&T stub + WBD 분배가치로 새 SOTP를 만들어야 했다.

### 10. 최종 판정·반사실·재사용 교훈

운영촉매 적중·증권/기업구조 thesis 실패. Telecom에서는 좋은 spectrum·좋은 콘텐츠·높은 FCF 하나만으로 equity floor를 만들지 않고, 실제 고객경제성·부채·corporate-action 귀속구조를 함께 stress해야 한다.

### 핵심 수치 — 당시 vs 실제

| 지표 | 글 당시 | VIC 기대 | 실제 | 판정 |
|---|---|---|---|---|
| HBO Max/HBO | 2020말 기대 상회 예상 | subscriber beat | 2020말 domestic 41m+; 2021말 global 73.8m | 강한 적중 |
| 2025 target | 시장 기대 낮음 | 고성장 | 2021-03 120~150m로 상향 | 강한 적중 |
| 주가 | $28.63 | $51~63.5 | 2024-01 package 약 $18.27 before dividends | 실패 |
| Corporate structure | Warner AT&T 내 가치 | 모회사 rerating | 2021-05 spin/Discovery merger 발표 | 치명적 반증 |

### 사건 타임라인

| 시점 | 사건 | 논지에 대한 의미 |
|---|---|---|
| 2021-01-03 | VIC 아이디어 게시 | HBO Max subscriber surprise·$51~63.5 Long |
| 2021-05-17 | 최초 핵심 검증·반증 신호 | AT&T가 WarnerMedia/Discovery 거래를 발표하면서 HBO Max가 AT&T valuation을 직접 끌어올린다는 thesis가 4개월 만에 구조적으로 무효화됐다. |
| 2020-12-31 | Cash flow·HBO·wireless 점검 | 2020 FCF와 HBO Max subscriber, postpaid trends 재검증 |
| 2021-05-17 | WarnerMedia 구조변경 발표 | AT&T conglomerate thesis가 통신 stub + WBD 분배가치로 변환 |
| 2022-04-08 | WarnerMedia/Discovery 거래 종결 | AT&T 1주당 0.241917 WBD 분배 |
| 2024-01-31 | 고정 사후평가 | HBO Max subscriber thesis는 빠르게 적중했지만 AT&T는 2021-05 WarnerMedia 분리를 발표. 2024-01-31 AT&T $15.85 + 배분된 0.241917 WBD×$10.02 ≈ $18.27 before dividends로 원 entry와 $51~63 target을 크게 하회. |

### Failure / Success Anatomy

- **근본 오류:** segment cash flow/operating success에서 parent equity multiple·corporate structure로 넘어가는 bridge 부족
- **최초 검증·반증 신호:** 2021-05-17 — AT&T가 WarnerMedia/Discovery 거래를 발표하면서 HBO Max가 AT&T valuation을 직접 끌어올린다는 thesis가 4개월 만에 구조적으로 무효화됐다.
- **당시 알 수 있었나:** 가입자 순증·churn·ARPU·service revenue·EBITDA·CapEx·FCF·gross debt·maturities·spectrum 사용·corporate-action 조건은 공시와 earnings에서 재검증 가능했다.
- **피할 수 있었나:** 매우 높음. 5월 17일 발표 직후 기존 $51/$63.5 target을 폐기하고 AT&T stub + WBD 분배가치로 새 SOTP를 만들어야 했다.
- **반사실 질문:** spectrum·segment business가 가치 있어도 integration, debt, corporate action 또는 security horizon이 반대로 움직이면 기존 보통주/스프레드의 payoff는 어떻게 달라지는가?
- **성공 패턴:** subscription_cash_flow; deleveraging; fiber_growth; content_optionality; event_restructuring
- **실패·주의 패턴:** conglomerate_discount; m_and_a_roic; fcf_quality; corporate_structure_change; dividend_floor_error

### 주요 근거자료

- [1. VIC T 2021-01-03 원문](https://www.valueinvestorsclub.com/idea/ATandamp%3BT_INC/1984848210) — Value Investors Club, 2021-01-03. 원 SQL description에서 당시 thesis·valuation·risk·catalyst·방향을 복원
- [2. AT&T FY2018 Results](https://about.att.com/story/2019/att_4q_earnings_2018.html) — AT&T, 2019-01-30. 2018 free cash flow $22.4bn·CapEx·deleveraging 확인
- [3. AT&T FY2019 Results](https://about.att.com/story/2020/4q_2019_earnings.html) — AT&T, 2020-01-29. 2019 FCF $29bn·net debt 약 $30bn 감소·leverage 약 2.5x 확인
- [4. AT&T FY2020 Results](https://about.att.com/story/2021/4q_2020_earnings.html) — AT&T, 2021-01-27. 2020 FCF $27.5bn·domestic HBO Max/HBO 41m+ 확인
- [5. AT&T Analyst Day 2021](https://about.att.com/story/2021/analyst_day_2021.html) — AT&T, 2021-03-12. HBO Max/HBO 2025 global target 120~150m·fiber build 확대 확인
- [6. AT&T and Discovery combine WarnerMedia and Discovery](https://about.att.com/story/2021/warnermedia_discovery.html) — AT&T, 2021-05-17. WarnerMedia 분리·Discovery 결합 발표
- [7. AT&T FY2021 Results](https://about.att.com/story/2022/fy_2021_earnings.html) — AT&T, 2022-01-26. 2021 wireless/fiber net adds·HBO/HBO Max 73.8m 확인
- [8. Warner Bros. Discovery transaction closes](https://about.att.com/story/2022/close-warnermedia-transaction.html) — AT&T, 2022-04-08. AT&T 1주당 0.241917 WBD 분배·거래종결 확인
- [9. AT&T FY2023 Results](https://about.att.com/story/2024/4q-earnings-2023.html) — AT&T, 2024-01-24. 2023 FCF·net debt·fiber/5G 장기상태 확인
- [10. AT&T historical prices](https://www.digrin.com/stocks/detail/T/price) — Digrin, 2024-01-31. 2018~2024 raw historical price 교차검증
- [11. Warner Bros. Discovery historical prices](https://www.digrin.com/stocks/detail/WBD/price) — Digrin, 2024-01-31. 2024-01 분배주식 가치 교차검증


---

<!-- idea:b42c135a-5384-4b5d-8958-2570f157006c -->
## 4. 2021-05-13 — Warner 55% valuation·wireless/fiber·$65 SOTP Long

### 결론부터

**종합판정: 기업구조가 4일 만에 반증된 실패.** 이 글은 wireless industry structure와 fiber ROIC, Warner D2C economics를 각각 흥미롭게 분석했지만, SOTP의 가장 큰 상태변수인 '이 자산들이 같은 기업 안에 계속 존재한다'는 전제를 체크하지 못했다. M&A-heavy management가 이미 asset reshuffling을 하고 있던 상황에서 corporate action risk를 낮게 본 것이 치명적이다. 좋은 segment 분석도 ownership structure가 바뀌면 기존 보통주의 payoff가 달라진다.

**주가·증권 결과:** 불과 4일 뒤 WarnerMedia 분리 발표로 핵심 SOTP 구조가 무효화. 2024-01 package value는 AT&T $15.85 + 0.241917 WBD×$10.02 ≈ $18.27 before dividends로 entry 대비 크게 낮음.

**Thesis / Process 점수:** 5.8 / 6.2

### 1. 무슨 기업인가

AT&T는 미국의 대형 통신사업자로 wireless, fiber broadband와 기업통신을 중심으로 현금흐름을 창출한다. 다만 2015 DirecTV, 2018 Time Warner 인수로 한동안 미디어·위성TV까지 포함한 거대한 복합기업이 되었고, 2021~22 WarnerMedia/Discovery 거래와 DirecTV 분리를 통해 다시 통신 중심으로 축소됐다. Wireless에서는 postpaid phone subscribers·ARPU·churn·network CapEx·spectrum이 핵심이고, fiber에서는 passings·net adds·penetration·ARPU와 build cost가 중요하다. 미디어 보유기에는 HBO/HBO Max subscriber growth, content spend, advertising, distribution economics도 equity value를 좌우했다. AT&T의 VIC 역사는 특히 '현금흐름은 맞았지만 M&A의 전략적 질이 틀린 경우', 'HBO Max 운영지표는 맞았지만 corporate structure가 바뀐 경우', '높은 dividend yield가 downside floor가 아닌 경우'를 잘 보여준다.

### 2. 산업 가치사슬과 돈의 흐름

AT&T의 핵심 현금창출은 wireless와 broadband subscription이다. Service revenue에서 network operating cost, sales, handset subsidy/financing, customer care와 SG&A를 차감해 EBITDA가 나오고, 여기서 spectrum·fiber·5G CapEx, interest, taxes, working capital을 차감하면 FCF가 된다. Time Warner 보유기에는 HBO·Turner·Warner Bros의 subscription, advertising, licensing, theatrical economics가 추가되었다. 그러나 높은 부채 때문에 EBITDA가 늘어도 debt service와 mandatory CapEx가 크면 equity FCF가 제한될 수 있다. 특히 AT&T는 asset sales, receivables factoring, vendor financing, DirecTV economics 등으로 headline FCF와 underlying cash conversion의 차이를 따져야 했다.

### 3. 경쟁우위·경쟁구도·핵심 지표

AT&T의 주요 우위는 전국 무선망·spectrum·distribution·기업고객·fiber footprint와 방대한 customer base다. 하지만 wireless는 Verizon·T-Mobile과 지속 경쟁하며, DirecTV·WarnerMedia 같은 비통신 자산은 통신 moat와 별개로 자본배분의 질을 요구한다. 2018~21의 핵심 질문은 'Time Warner가 좋은 콘텐츠 자산인가'보다 'AT&T 안에서 높은 부채와 복합기업 할인까지 감안했을 때 주당가치를 높이는가'였다. 2021 이후에는 Warner 분리로 그 질문 자체가 사라졌다. 따라서 통신 operating metrics, FCF와 동시에 net debt, dividend coverage, M&A·spin 구조와 기존 주주에게 귀속되는 분배가치를 추적해야 한다.

### 4. 당시 VIC 원문과 핵심 숫자

AT&T의 핵심 upside를 세 축으로 봤다. 첫째 WarnerMedia가 HBO Max D2C로 Netflix/Disney 다음 글로벌 player가 되어 수익·valuation 비중을 크게 늘린다. 둘째 T-Mobile이 wireless leader가 되어도 3강 구조로 competition은 과거보다 완화되고 AT&T wireless ROIC 9.5%가 7%로 떨어질 필요가 없다. 셋째 fiber는 10~15% ROIC로 15m homes에서 35m homes까지 확장 가능하다. Jason Kilar와 개선된 management가 과거 DirecTV 실수를 되돌린다고 봤다.

### 5. 밸류에이션과 기대수익의 연결

4년 내 FCFE $38.5bn. Wireless 11x, Warner 18x, 기타 7x를 적용해 market cap 약 $470bn, 주가 $65 + 약 7% dividend를 제시. Warner는 현재 profit 18%/valuation 25%에서 5년 후 profit 35%/valuation 55%로 확대된다고 봄. 사후에는 subscriber/churn/ARPU 또는 segment earnings → EBITDA → CapEx·interest → FCF → debt·corporate action → 기존 보통주 또는 merger spread payoff 순으로 다시 연결해 검증했다.

### 투자논지를 구성한 핵심 주장

#### 1. Warner D2C — 치명적 실패 · 논지 비중 18%

**당시 주장**

Warner가 AT&T 안에서 NFLX/DIS 다음 글로벌 D2C가 된다.

**당시 근거**

AT&T의 핵심 upside를 세 축으로 봤다. 첫째 WarnerMedia가 HBO Max D2C로 Netflix/Disney 다음 글로벌 player가 되어 수익·valuation 비중을 크게 늘린다. 둘째 T-Mobile이 wireless leader가 되어도 3강 구조로 competition은 과거보다 완화되고 AT&T wireless ROIC 9.5%가 7%로 떨어질 필요가 없다. 셋째 fiber는 10~15% ROIC로 15m homes에서 35m homes까지 확장 가능하다. Jason Kilar와 개선된 management가 과거 DirecTV 실수를 되돌린다고 봤다.

**이 주장이 성립하려면**

Warner ownership가 AT&T에 남음

**사전 반증조건**

spin/merger

**실제 결과**

4일 뒤 Discovery와 결합·분리 발표.

**정량적 괴리**

주가 / $29.43 / 4년 $65 + dividend / 2024-01 package 약 $18.27 before dividends

**분석 오류·핵심**

좋은 자산·평균 operating path를 equity payoff에 직접 연결하거나, debt·integration·corporate action·timing의 joint distribution을 충분히 stress하지 않았다.

**재사용할 교훈**

Warner D2C 가설은 'spin/merger'를 사전 반증조건으로 저장하고 사업·이벤트·가격 판정을 분리한다.

#### 2. Wireless ROIC — 부분 적중 · 논지 비중 18%

**당시 주장**

3강 구조로 AT&T wireless ROIC가 9% 안팎을 유지할 수 있다.

**당시 근거**

AT&T의 핵심 upside를 세 축으로 봤다. 첫째 WarnerMedia가 HBO Max D2C로 Netflix/Disney 다음 글로벌 player가 되어 수익·valuation 비중을 크게 늘린다. 둘째 T-Mobile이 wireless leader가 되어도 3강 구조로 competition은 과거보다 완화되고 AT&T wireless ROIC 9.5%가 7%로 떨어질 필요가 없다. 셋째 fiber는 10~15% ROIC로 15m homes에서 35m homes까지 확장 가능하다. Jason Kilar와 개선된 management가 과거 DirecTV 실수를 되돌린다고 봤다.

**이 주장이 성립하려면**

DISH가 약하고 pricing 합리화

**사전 반증조건**

T-Mobile 경쟁으로 ROIC 급락

**실제 결과**

wireless는 이후에도 핵심 cash generator로 유지.

**정량적 괴리**

Warner 구조 / AT&T 내 profit 18%→35% / valuation 25%→55% / 4일 뒤 spin 발표

**분석 오류·핵심**

핵심 causal chain은 실제 결과에서 확인됐다. 다만 그 성공이 증권 payoff의 원인이었는지는 별도 판정한다.

**재사용할 교훈**

Wireless ROIC 가설은 'T-Mobile 경쟁으로 ROIC 급락'를 사전 반증조건으로 저장하고 사업·이벤트·가격 판정을 분리한다.

#### 3. Fiber ROIC — 적중 · 논지 비중 16%

**당시 주장**

FTTH build가 10~15% ROIC로 35m homes까지 확장된다.

**당시 근거**

AT&T의 핵심 upside를 세 축으로 봤다. 첫째 WarnerMedia가 HBO Max D2C로 Netflix/Disney 다음 글로벌 player가 되어 수익·valuation 비중을 크게 늘린다. 둘째 T-Mobile이 wireless leader가 되어도 3강 구조로 competition은 과거보다 완화되고 AT&T wireless ROIC 9.5%가 7%로 떨어질 필요가 없다. 셋째 fiber는 10~15% ROIC로 15m homes에서 35m homes까지 확장 가능하다. Jason Kilar와 개선된 management가 과거 DirecTV 실수를 되돌린다고 봤다.

**이 주장이 성립하려면**

build cost와 take rate 양호

**사전 반증조건**

높은 CapEx·낮은 penetration

**실제 결과**

fiber subscriber/build 성장은 실제 강했다.

**정량적 괴리**

HBO/HBO Max / D2C 성장 / global scale / 2021말 73.8m

**분석 오류·핵심**

핵심 causal chain은 실제 결과에서 확인됐다. 다만 그 성공이 증권 payoff의 원인이었는지는 별도 판정한다.

**재사용할 교훈**

Fiber ROIC 가설은 '높은 CapEx·낮은 penetration'를 사전 반증조건으로 저장하고 사업·이벤트·가격 판정을 분리한다.

#### 4. Management — 혼합 · 논지 비중 16%

**당시 주장**

Kilar와 asset divestitures가 capital allocation을 개선한다.

**당시 근거**

AT&T의 핵심 upside를 세 축으로 봤다. 첫째 WarnerMedia가 HBO Max D2C로 Netflix/Disney 다음 글로벌 player가 되어 수익·valuation 비중을 크게 늘린다. 둘째 T-Mobile이 wireless leader가 되어도 3강 구조로 competition은 과거보다 완화되고 AT&T wireless ROIC 9.5%가 7%로 떨어질 필요가 없다. 셋째 fiber는 10~15% ROIC로 15m homes에서 35m homes까지 확장 가능하다. Jason Kilar와 개선된 management가 과거 DirecTV 실수를 되돌린다고 봤다.

**이 주장이 성립하려면**

Warner strategy 안정

**사전 반증조건**

대규모 구조변경

**실제 결과**

Warner 자체를 분리해 원래 management thesis가 바뀌었다.

**정량적 괴리**

Fiber / 15m→35m homes / 10~15% ROIC growth / 2021 +1m fiber subs, 이후 build 확대

**분석 오류·핵심**

핵심 causal chain은 실제 결과에서 확인됐다. 다만 그 성공이 증권 payoff의 원인이었는지는 별도 판정한다.

**재사용할 교훈**

Management 가설은 '대규모 구조변경'를 사전 반증조건으로 저장하고 사업·이벤트·가격 판정을 분리한다.

#### 5. FCFE $38.5bn — 실패 · 논지 비중 16%

**당시 주장**

segment growth와 capex normalization으로 FCFE가 크게 증가한다.

**당시 근거**

AT&T의 핵심 upside를 세 축으로 봤다. 첫째 WarnerMedia가 HBO Max D2C로 Netflix/Disney 다음 글로벌 player가 되어 수익·valuation 비중을 크게 늘린다. 둘째 T-Mobile이 wireless leader가 되어도 3강 구조로 competition은 과거보다 완화되고 AT&T wireless ROIC 9.5%가 7%로 떨어질 필요가 없다. 셋째 fiber는 10~15% ROIC로 15m homes에서 35m homes까지 확장 가능하다. Jason Kilar와 개선된 management가 과거 DirecTV 실수를 되돌린다고 봤다.

**이 주장이 성립하려면**

Warner·wireless·fiber 동시 성장

**사전 반증조건**

portfolio separation·higher capex

**실제 결과**

원 구조가 해체돼 원 FCFE bridge가 무효화.

**정량적 괴리**

불과 4일 뒤 WarnerMedia 분리 발표로 핵심 SOTP 구조가 무효화. 2024-01 package value는 AT&T $15.85 + 0.241917 WBD×$10.02 ≈ $18.27 before dividends로 entry 대비 크게 낮음.

**분석 오류·핵심**

좋은 자산·평균 operating path를 equity payoff에 직접 연결하거나, debt·integration·corporate action·timing의 joint distribution을 충분히 stress하지 않았다.

**재사용할 교훈**

FCFE $38.5bn 가설은 'portfolio separation·higher capex'를 사전 반증조건으로 저장하고 사업·이벤트·가격 판정을 분리한다.

#### 6. $65 SOTP — 치명적 실패 · 논지 비중 16%

**당시 주장**

Wireless 11x·Warner 18x·rest 7x로 $65 가능.

**당시 근거**

AT&T의 핵심 upside를 세 축으로 봤다. 첫째 WarnerMedia가 HBO Max D2C로 Netflix/Disney 다음 글로벌 player가 되어 수익·valuation 비중을 크게 늘린다. 둘째 T-Mobile이 wireless leader가 되어도 3강 구조로 competition은 과거보다 완화되고 AT&T wireless ROIC 9.5%가 7%로 떨어질 필요가 없다. 셋째 fiber는 10~15% ROIC로 15m homes에서 35m homes까지 확장 가능하다. Jason Kilar와 개선된 management가 과거 DirecTV 실수를 되돌린다고 봤다.

**이 주장이 성립하려면**

segments가 AT&T 안에 존속

**사전 반증조건**

Warner spin

**실제 결과**

핵심 전제 붕괴로 target 무효.

**정량적 괴리**

불과 4일 뒤 WarnerMedia 분리 발표로 핵심 SOTP 구조가 무효화. 2024-01 package value는 AT&T $15.85 + 0.241917 WBD×$10.02 ≈ $18.27 before dividends로 entry 대비 크게 낮음.

**분석 오류·핵심**

좋은 자산·평균 operating path를 equity payoff에 직접 연결하거나, debt·integration·corporate action·timing의 joint distribution을 충분히 stress하지 않았다.

**재사용할 교훈**

$65 SOTP 가설은 'Warner spin'를 사전 반증조건으로 저장하고 사업·이벤트·가격 판정을 분리한다.

### 6. 실제 사업의 시간순 전개

가장 중요한 반증이 매우 빨랐다. 2021년 5월 17일, 글 게시 4일 뒤 AT&T는 WarnerMedia를 Discovery와 결합해 분리한다고 발표했다. 따라서 Warner가 AT&T profit 35%·valuation 55%가 된다는 핵심 corporate-structure 전제는 즉시 사라졌다. 거래는 2022년 4월 8일 완료됐고 AT&T 주주는 1주당 0.241917 WBD를 받았다. 다만 운영조각 중 fiber는 실제로 강했다. 2021 AT&T는 fiber subscribers 약 1m 순증했고 이후 fiber build를 계속 확대했다. HBO/HBO Max도 2021말 73.8m까지 성장했다.

### 7. 사업 결과와 가격 결과 분리

증권 결과는 불과 4일 뒤 WarnerMedia 분리 발표로 핵심 SOTP 구조가 무효화. 2024-01 package value는 AT&T $15.85 + 0.241917 WBD×$10.02 ≈ $18.27 before dividends로 entry 대비 크게 낮음. 사업논지·촉매·valuation·corporate structure와 주가를 서로 다른 판정으로 저장한다.

### 8. 무엇을 잘 봤고 무엇을 놓쳤나

이 글은 wireless industry structure와 fiber ROIC, Warner D2C economics를 각각 흥미롭게 분석했지만, SOTP의 가장 큰 상태변수인 '이 자산들이 같은 기업 안에 계속 존재한다'는 전제를 체크하지 못했다. M&A-heavy management가 이미 asset reshuffling을 하고 있던 상황에서 corporate action risk를 낮게 본 것이 치명적이다. 좋은 segment 분석도 ownership structure가 바뀌면 기존 보통주의 payoff가 달라진다.

### 9. 최초 검증·반증 신호와 회피 가능성

2021-05-17 — 게시 4일 뒤 WarnerMedia/Discovery 거래 발표. 핵심 SOTP와 $65 target의 구조가 즉시 반증됐다. 이 시점에 원 valuation bridge를 다시 만들면 operating thesis와 security thesis 중 무엇이 살아있는지 구분할 수 있었다. 회피 가능성: 매우 높음. 발표 즉시 thesis를 폐기하거나 AT&T stub + WBD 분배가치로 완전히 새로 계산했어야 한다. 원래 Warner 18x multiple을 AT&T 안에서 적용하는 것은 더 이상 유효하지 않았다.

### 10. 최종 판정·반사실·재사용 교훈

기업구조가 4일 만에 반증된 실패. Telecom에서는 좋은 spectrum·좋은 콘텐츠·높은 FCF 하나만으로 equity floor를 만들지 않고, 실제 고객경제성·부채·corporate-action 귀속구조를 함께 stress해야 한다.

### 핵심 수치 — 당시 vs 실제

| 지표 | 글 당시 | VIC 기대 | 실제 | 판정 |
|---|---|---|---|---|
| 주가 | $29.43 | 4년 $65 + dividend | 2024-01 package 약 $18.27 before dividends | 실패 |
| Warner 구조 | AT&T 내 profit 18%→35% | valuation 25%→55% | 4일 뒤 spin 발표 | 치명적 실패 |
| HBO/HBO Max | D2C 성장 | global scale | 2021말 73.8m | 운영 적중 |
| Fiber | 15m→35m homes | 10~15% ROIC growth | 2021 +1m fiber subs, 이후 build 확대 | 운영 적중 |

### 사건 타임라인

| 시점 | 사건 | 논지에 대한 의미 |
|---|---|---|
| 2021-05-13 | VIC 아이디어 게시 | Warner 55% valuation·wireless/fiber·$65 SOTP Long |
| 2021-05-17 | 최초 핵심 검증·반증 신호 | 게시 4일 뒤 WarnerMedia/Discovery 거래 발표. 핵심 SOTP와 $65 target의 구조가 즉시 반증됐다. |
| 2020-12-31 | Cash flow·HBO·wireless 점검 | 2020 FCF와 HBO Max subscriber, postpaid trends 재검증 |
| 2021-05-17 | WarnerMedia 구조변경 발표 | AT&T conglomerate thesis가 통신 stub + WBD 분배가치로 변환 |
| 2022-04-08 | WarnerMedia/Discovery 거래 종결 | AT&T 1주당 0.241917 WBD 분배 |
| 2024-01-31 | 고정 사후평가 | 불과 4일 뒤 WarnerMedia 분리 발표로 핵심 SOTP 구조가 무효화. 2024-01 package value는 AT&T $15.85 + 0.241917 WBD×$10.02 ≈ $18.27 before dividends로 entry 대비 크게 낮음. |

### Failure / Success Anatomy

- **근본 오류:** segment cash flow/operating success에서 parent equity multiple·corporate structure로 넘어가는 bridge 부족
- **최초 검증·반증 신호:** 2021-05-17 — 게시 4일 뒤 WarnerMedia/Discovery 거래 발표. 핵심 SOTP와 $65 target의 구조가 즉시 반증됐다.
- **당시 알 수 있었나:** 가입자 순증·churn·ARPU·service revenue·EBITDA·CapEx·FCF·gross debt·maturities·spectrum 사용·corporate-action 조건은 공시와 earnings에서 재검증 가능했다.
- **피할 수 있었나:** 매우 높음. 발표 즉시 thesis를 폐기하거나 AT&T stub + WBD 분배가치로 완전히 새로 계산했어야 한다. 원래 Warner 18x multiple을 AT&T 안에서 적용하는 것은 더 이상 유효하지 않았다.
- **반사실 질문:** spectrum·segment business가 가치 있어도 integration, debt, corporate action 또는 security horizon이 반대로 움직이면 기존 보통주/스프레드의 payoff는 어떻게 달라지는가?
- **성공 패턴:** subscription_cash_flow; deleveraging; fiber_growth; content_optionality; event_restructuring
- **실패·주의 패턴:** conglomerate_discount; m_and_a_roic; fcf_quality; corporate_structure_change; dividend_floor_error

### 주요 근거자료

- [1. VIC T 2021-05-13 원문](https://www.valueinvestorsclub.com/idea/ATandamp%3BT_INC/5472051992) — Value Investors Club, 2021-05-13. 원 SQL description에서 당시 thesis·valuation·risk·catalyst·방향을 복원
- [2. AT&T FY2018 Results](https://about.att.com/story/2019/att_4q_earnings_2018.html) — AT&T, 2019-01-30. 2018 free cash flow $22.4bn·CapEx·deleveraging 확인
- [3. AT&T FY2019 Results](https://about.att.com/story/2020/4q_2019_earnings.html) — AT&T, 2020-01-29. 2019 FCF $29bn·net debt 약 $30bn 감소·leverage 약 2.5x 확인
- [4. AT&T FY2020 Results](https://about.att.com/story/2021/4q_2020_earnings.html) — AT&T, 2021-01-27. 2020 FCF $27.5bn·domestic HBO Max/HBO 41m+ 확인
- [5. AT&T Analyst Day 2021](https://about.att.com/story/2021/analyst_day_2021.html) — AT&T, 2021-03-12. HBO Max/HBO 2025 global target 120~150m·fiber build 확대 확인
- [6. AT&T and Discovery combine WarnerMedia and Discovery](https://about.att.com/story/2021/warnermedia_discovery.html) — AT&T, 2021-05-17. WarnerMedia 분리·Discovery 결합 발표
- [7. AT&T FY2021 Results](https://about.att.com/story/2022/fy_2021_earnings.html) — AT&T, 2022-01-26. 2021 wireless/fiber net adds·HBO/HBO Max 73.8m 확인
- [8. Warner Bros. Discovery transaction closes](https://about.att.com/story/2022/close-warnermedia-transaction.html) — AT&T, 2022-04-08. AT&T 1주당 0.241917 WBD 분배·거래종결 확인
- [9. AT&T FY2023 Results](https://about.att.com/story/2024/4q-earnings-2023.html) — AT&T, 2024-01-24. 2023 FCF·net debt·fiber/5G 장기상태 확인
- [10. AT&T historical prices](https://www.digrin.com/stocks/detail/T/price) — Digrin, 2024-01-31. 2018~2024 raw historical price 교차검증
- [11. Warner Bros. Discovery historical prices](https://www.digrin.com/stocks/detail/WBD/price) — Digrin, 2024-01-31. 2024-01 분배주식 가치 교차검증


---

# 배치 공통 학습

1. **M&A accretion보다 integration physics를 먼저 본다.** Sprint 2005는 leverage·EPS math는 정교했지만 network·customer integration이 실패하자 전부 무너졌다.
2. **Asset value는 cash floor가 아니다.** Sprint 2008의 2.5GHz spectrum 가치는 실제로 컸지만 debt·operating use·규제 때문에 당시 equity의 $12 floor가 되지 못했다.
3. **나쁜 standalone 기업도 strategic asset이면 Short tail이 크다.** Sprint 2010은 economics를 맞혔지만 SoftBank, 2016은 T-Mobile의 rescue/strategic bid를 과소평가했다.
4. **FCF accounting insight와 security thesis를 분리한다.** Sprint 2016의 handset lease 회계 비판은 좋았지만 FCF가 실제 흑자전환하면서 핵심 normalized-burn premise가 깨졌다.
5. **Event-driven에서는 사업 전망보다 계약조건·closing probability가 중요할 수 있다.** Sprint 2020 merger arb가 가장 깨끗한 성공인 이유다.
6. **Cash accretion과 strategic ROIC는 다르다.** AT&T 2018은 Time Warner의 단기 cash contribution과 deleveraging을 맞혔지만 장기 corporate fit은 결국 spin으로 되돌려졌다.
7. **가격이 맞아도 원인이 틀릴 수 있다.** AT&T 2020 Short는 목표가격에 접근했지만 COVID shock의 영향이 커서 thesis accuracy를 주가수익률과 동일시하면 안 된다.
8. **Operating catalyst가 맞아도 parent equity가 오르는 것은 아니다.** HBO Max subscriber beat를 정확히 맞힌 2021 Long도 WarnerMedia가 분리되면서 AT&T rerating bridge가 끊겼다.
9. **SOTP에는 ownership stability가 숨은 전제다.** 게시 4일 뒤 Warner spin이 발표된 2021-05 AT&T 사례는 segment 가치 이전에 '누가 그 자산을 보유하게 되는가'를 확인해야 함을 보여준다.
