# Batch 006 — Western Union (WU), agent moat와 디지털 전환 9건

평가기준일: 각 글의 최대 5년 성과, 장기사업 확인은 2024-01-31  
분석일: 2026-09-03  
대상 VIC 아이디어: 2007-07-12~2017-09-10, 총 9건

## 결론부터

| 게시일 | 실제 방향 | 핵심 주장 | 실제 가격 경로 | 종합판정 |
|---|---:|---|---|---:|
| 2007-07-12 | Long | agent network와 이민·송금 성장, $20.75→$32 | 1년 +16.4%, 3년 -23.1%, 5년 -16.8% | 실패 |
| 2011-09-15 | Long | 10.1x unlevered FCF, core moat는 불침투 | 1년 +18.5%, 3년 +11.6%, 5년 +44.3% | 부분 성공 |
| 2012-11-13 | Short | online 가격발견으로 마진 붕괴, 50%+ 하락 | 1년 -42.8%, 3년 -60.7%, 5년 -80.9% 숏손익 | 치명적 실패 |
| 2013-06-06 | Short | smartphone이 만드는 Kodak moment | 1년 -0.5%, 3년 -29.0%, 5년 -45.4% 숏손익 | 실패 |
| 2013-08-29 | Short | ROIC 하락·가격압박, $18→$11~14 | 6개월 +6.7%, 1년 -2.6%, 5년 -26.2% 숏손익 | 대체로 실패 |
| 2014-02-25 | Long | Mexico·compliance는 일시적, 5년 20% IRR | 1년 +23.1%, 3년 +35.2%, 5년 +27.8% | 부분 성공 |
| 2015-04-13 | Long | 기술파괴 가능성 낮고 12x FCF | 1년 -0.5%, 3년 +1.9%, 5년 +15.3% | 실패 |
| 2016-03-18 | Short | 경쟁·마진하락·공격적 비용자본화 | 1년 -9.3%, 3년 -6.1%, 5년 -56.5% 숏손익 | 실패 |
| 2017-09-10 | Long | WU.com이 2020 EPS 10~13%, $19→$33 | 1년 +5.1%, 3년 +34.5%, 5년 -3.2% | 부분 성공 |

SQL은 9건 모두 `is_short=true`로 저장했지만 원문은 **롱 5건, 숏 4건**이다. 원본값은
보존하고 분석 레이어에서 실제 방향을 교정했다. 성과값도 단순 가격비율이므로 롱은
`ratio-1`, 숏은 `1-ratio`로 재계산했다. 배당과 대차비용은 포함하지 않는다.

이 9건의 핵심은 누가 디지털 전환을 맞혔는지가 아니다. 숏은 가격하락, C2C revenue와
margin 하락을 꽤 정확히 봤다. 롱은 현금흐름, agent network, 규제규모의 경제와 자사주를
정확히 봤다. 양쪽이 동시에 맞을 수 있었다.

> **Western Union은 디지털 전환으로 경제성이 서서히 악화된 진짜 legacy business였지만,
> 2012년 $12 부근의 주가는 이미 더 빠른 붕괴를 가격에 넣었다. 사업이 나빠진다는 것과
> 주식이 하락한다는 것은 같은 명제가 아니다. 반대로 2017년 롱은 디지털 자산을 정확히
> 발견했지만, 성장사업 WU.com이 성숙한 retail network 전체를 다시 고성장기업으로
> 바꾸기에는 아직 너무 작았다.**

---

## 1. Western Union은 무슨 기업인가

Western Union은 은행계좌가 없거나 국제은행 송금이 불편한 개인이 국경을 넘어 돈을
보내도록 중개하는 글로벌 remittance 회사다. 발송인은 현금·카드·은행계좌로 자금을 내고,
수취인은 현지 agent에서 현금으로 받거나 계좌·wallet로 받는다.

### ① Consumer-to-Consumer: 핵심 cash remittance

역사적으로 매출의 약 80%, 이익의 더 큰 비중이 C2C였다. 수익원은 두 가지다.

- 소비자가 내는 transaction fee
- 고객에게 적용한 환율과 WU가 조달한 환율 사이의 FX spread

WU는 송금 원금을 매출로 잡지 않고 fee와 FX spread만 매출로 인식한다. transaction 수가
늘어도 건당 가격이 하락하면 매출은 정체될 수 있다. 2012년 C2C transaction은 231m,
C2C revenue는 $4.58bn, operating margin은 28%였다.

### ② 물리적 agent network

WU는 우체국, 은행, 편의점, 환전상 등 제3자 agent를 이용하므로 직접 점포 capex가 작다.
2007년 305,000여 개였던 agent location은 2012년 510,000개 이상으로 확대됐다. 발송·수취
양쪽에서 현금 접근점이 많을수록 고객이 늘고, 고객이 많을수록 agent가 WU를 취급할 유인이
커지는 양면 network다.

그러나 agent도 무료 자산은 아니다. WU는 transaction fee의 일정 비율을 양쪽 agent에
지급하고 계약 갱신비용을 부담한다. 디지털 발송은 send-side commission을 줄일 수 있지만
가격이 훨씬 낮고 receive-side 현금 agent가 남으면 gross revenue와 margin의 순효과는
단순하지 않다.

### ③ 규제·compliance scale

국경간 송금에는 AML, KYC, 사기방지, sanctions와 각국 licensing이 필요하다. 이는 비용인
동시에 작은 경쟁자의 진입장벽이다. 롱은 WU가 고정 compliance 비용을 더 큰 거래량에
분산한다고 봤고, 숏은 절대 compliance expense와 agent oversight 책임이 계속 증가한다고
봤다. 두 주장 모두 실제였다. 규모는 상대우위를 주지만 규제비용 자체를 제거하지 않는다.

### ④ 디지털 송금

`westernunion.com`과 모바일 앱은 bank/card-funded 송금을 받고 현금·계좌·wallet로 지급한다.
2012년 electronic channel은 consolidated revenue의 4%에 불과했다. 2016년 WU.com은 약
8%까지 성장했고 2017년 롱은 2020년 15%를 예상했다. 디지털은 경쟁자에게 열린 공격경로인
동시에 WU가 기존 브랜드·compliance·payout network를 재사용하는 자기잠식 경로다.

### ⑤ Consumer-to-Business와 Business Solutions

C2B는 공과금, 자동차금융, 정부 등에 소비자 납부를 중개한다. Business Solutions는
Custom House와 2011년 약 $1bn에 산 Travelex Global Business Payments를 기반으로 SME의
국경간 결제와 FX를 제공했다. 여러 롱은 B2B turnaround를 무료 옵션으로 봤지만 오랫동안
낮은 이익이 문제였다. WU는 결국 2022년 Business Solutions를 매각했다. 이는 숨은 성장축이
핵심엔진이 되었다기보다 capital allocation의 복구에 가까웠다.

### ⑥ 이 기업의 실제 경제성을 읽는 지표

| 지표 | 의미 | 함정 |
|---|---|---|
| C2C transactions | network 사용량 | 가격인하로 산 volume일 수 있음 |
| Revenue per transaction | fee·FX 가격력 | corridor·원금·digital mix 영향 |
| C2C operating margin | core moat의 수익화 | compliance·agent·digital 투자가 섞임 |
| Digital revenue·transactions | 적응속도 | 기존 retail 자기잠식과 낮은 가격 고려 |
| CFO·FCF | 현금창출력 | settlement·intercompany working capital 분리 |
| Share count·dividend | 주주환원 | 영업이익 정체를 EPS가 가릴 수 있음 |
| ROIC·ROTC | 자본효율 | 음의 장부자본과 acquisition intangibles로 왜곡 가능 |

---

## 2. 장기사업 결과: 양쪽 논지가 왜 동시에 맞았나

| 연도 | Revenue | Operating income | EPS | C2C transactions | 핵심 해석 |
|---:|---:|---:|---:|---:|---|
| 2007 | $4.90bn | $1.32bn | $1.11 | 167.7m | 국제 transaction 성장, margin은 이미 32%→27% 하락 |
| 2011 | $5.49bn | $1.39bn | $1.84 | 약 226m | cash moat·FCF 논리가 가장 강해 보인 시점 |
| 2012 | $5.66bn | $1.33bn | $1.69 | 231.0m | 가격 reset 직전, electronic revenue 4% |
| 2013 | $5.54bn | $1.11bn | $1.43 | 242.3m | revenue -2%, op income -17%, C2C margin 28%→23% |
| 2017 | $5.52bn | 일회성 포함 $0.47bn | -$1.19 | 275.8m | 거래량은 증가했지만 C2C 이익은 2012보다 낮음 |
| 2021 | $5.07bn | $1.12bn | $1.97 | — | 디지털 성장·팬데믹 회복, 매출은 장기 정체 |
| 2023 | $4.36bn | $0.82bn | $1.68 | — | Business Solutions 매각 후 core의 구조적 축소 확인 |

2007~2017 C2C transactions는 167.7m에서 275.8m으로 약 64% 늘었다. 그러나 2012~2017
C2C revenue는 $4.58bn에서 $4.35bn으로 5% 감소하고 C2C operating income은 $1.27bn에서
$1.00bn으로 21% 줄었다. **network 사용량은 성장했지만 transaction당 수익과 margin은
하락했다.** 이것이 숏이 맞힌 부분이다.

그럼에도 회사는 매년 큰 operating cash flow를 만들고 자사주를 샀다. 2012~2017에만
공시상 약 $2.67bn을 자사주에 투입했다. 낮은 시작 multiple, 배당, share count 감소와
붕괴하지 않은 현금흐름 때문에 2012년 숏은 사업지표를 맞히고도 큰 손실을 냈다.

---

# Part A. 2007년 Long

## 3. 원 투자논지

주가 $20.75에서 이민·국경간 remittance가 장기성장하고 WU의 점유율이 2003년 약 10%에서
15%로 올라간다고 봤다. 305,000개 agent, 강한 브랜드, 무점포 asset-light 구조와 2006년
$1.3bn operating profit이 근거였다. 10년 10%, 이후 5년 6% 성장 DCF로 $32를 제시했다.

스핀오프 때 First Data에 지급한 $2.4bn dividend 때문에 생긴 $3.5bn debt도 연 $500m
상환 가능한 predictable FCF로 보아 큰 위험이 아니라고 했다. 휴대전화 송금 우려는
unbanked 고객이 ATM·카드가 없어 먼 미래라고 판단했다.

## 4. 결과와 판정

2007 revenue는 9% 늘었지만 operating income은 1% 증가에 그쳤고 margin은 2005년 32%,
2006년 29%, 2007년 26%로 하락했다. volume·international growth가 곧 같은 속도의 이익
성장을 의미하지 않는 첫 반증이었다.

가격은 1년 +16.4%였으나 2년 -18.3%, 3년 -23.1%, 5년 -16.8%였다. $32 목표와 장기복리
모두 실패했다. 사업은 사라지지 않았지만 18x trailing earnings는 margin·가격하락과
스핀오프 부채를 감안한 충분한 안전마진이 아니었다.

**종합판정: 실패.** network 존재를 정확히 봤지만 `거래량 성장 → 이익 10% 성장` 사이의
agent commission, 가격, compliance와 mix bridge가 없었다.

---

# Part B. 2011년 Long

## 5. 원 투자논지

Travelex 인수를 포함해 $16.50, TEV $11.8bn, 2011E unlevered FCF $1.17bn의 10.1x라고
계산했다. C2C 매출의 대부분은 cash-to-cash이며 unbanked migrant에게 위치와 신뢰가
중요하므로 은행·PayPal·모바일이 쉽게 대체하지 못한다고 봤다. WU transaction은 2위
MoneyGram의 약 5배이고 규제가 오히려 대형사 지위를 강화한다는 논리였다.

저성장에서도 organic revenue 4~5%, 안정 margin과 자사주·배당으로 주가 50~60% 상승을
기대했다. PE 인수도 옵션으로 제시했다.

## 6. 결과와 판정

가격은 1년 +18.5%, 2년 +20.6%, 3년 +11.6%, 5년 +44.3%였다. 배당을 제외한 5년 CAGR은
약 7.6%로 양수지만 원문의 50~60%와 고품질 복리 기대에는 못 미쳤다.

2012 revenue는 3% 늘었지만 operating income은 4% 감소했다. 2013 가격 reset 뒤 revenue
-2%, operating income -17%로 `stable margin`이 깨졌다. 다만 cash-to-cash network가
즉시 대체되지 않았고 cash flow·환원이 계속돼 영구손실은 피했다.

**종합판정: 부분 성공.** 낮은 가격과 FCF가 downside를 방어했지만 moat를 `impregnable`로
표현하고 가격하락·Travelex 자본배분을 과소평가했다.

---

# Part C. 2012년 Short

## 7. 원 투자논지

30% YTD 하락 뒤에도 WU가 더 좋은 숏이라고 주장했다. $500 Mexico 송금가격을 오프라인
WU $25, MoneyGram $10, online WU $7, Xoom $5로 비교했다. 발송이 온라인으로 이동하면
send agent commission은 줄어도 절대 fee와 margin dollar가 훨씬 감소하고 가격발견이
모든 corridor로 퍼진다고 봤다.

2013 consensus EPS가 $1.91에서 $1.51로 낮아졌어도 추가 margin 압박을 반영하지 못했고
2014 EPS가 $1 미만, 주가는 한 자릿수, 50%+ downside라고 예상했다. buyback은 나빠지는
사업에 capital을 오배분한다고 봤다.

## 8. 결과와 판정

**사업 인과는 상당 부분 맞았다.** 2013 C2C transaction은 5% 증가했지만 C2C revenue는
3%, operating income은 19% 감소하고 margin은 28%에서 23%로 내려갔다. 회사는 가격인하와
compliance action이 원인이라고 공시했다. 2017 C2C transaction은 2012보다 19% 많았지만
C2C revenue는 5%, operating income은 21% 낮았다.

그러나 주가는 반대로 1년 42.8%, 3년 60.7%, 5년 80.9% 상승했다. 원문의 단순 숏손익은
그만큼 마이너스이며 배당·대차비용까지 넣으면 더 나쁘다. $12 부근의 8배대 P/E는 이미
가격 reset을 반영했고, 이익이 $1 아래로 붕괴하지 않았으며 buyback은 낮은 가격에서
주당가치를 지지했다.

**종합판정: 치명적 실패.** `사업악화는 맞고 주식은 틀린` 대표 사례다. 정상가치가 아니라
현재 가격이 이미 요구하는 붕괴속도를 역산했어야 했다.

---

# Part D. 2013년 6월 Short

## 9. 원 투자논지

제목부터 `smartphone이 만드는 Kodak moment`였다. 신흥국 핵심고객 smartphone penetration이
2012년 28.4%에서 2015년 61.7%로 올라가면 디지털 network effect가 임계점을 넘고 WU
transaction이 감소한다고 예상했다. MoneyGram agent 수도 빠르게 늘고 가격이 낮아
offline moat도 약해진다고 봤다.

2014 revenue -5%를 volume -3%, price -2%로 만들고 operating leverage에 따라 net income
-9~-19.7%를 예상했다. 약 10x P/E는 declining earnings에 싸지 않다고 주장했다.

## 10. 결과와 판정

스마트폰 보급은 맞았지만 `스마트폰 보유 → 양쪽 고객의 계좌·신뢰·KYC 해결 → WU volume
감소`라는 변환율 가정이 없었다. WU는 자체 digital front-end와 기존 payout network를
결합했고 C2C transaction은 2012년 231m에서 2017년 276m으로 늘었다.

주가는 1년 거의 보합이었으나 2년 +37.1%, 5년 +45.4% 올라 숏은 실패했다. revenue와
margin 압박은 맞았지만 9~20%의 연속 net-income 감소와 Kodak식 급사는 발생하지 않았다.

**종합판정: 실패.** 기술 보급률을 기업 대체율로 직접 연결한 오류다. 기술이 고객의
마지막 현금 mile과 규제를 해결하는지, incumbent가 기술을 채택할 수 있는지를 봐야 한다.

---

# Part E. 2013년 8월 Short

## 11. 원 투자논지

이 글은 다른 숏보다 균형적이었다. 510,000개 last-mile network, 현금 선호, 디지털 발송이
send-agent commission을 줄이는 upside와 B2B 기회를 인정했다. 동시에 2004~2012 ROIC가
연평균 190bp, tangible return이 690bp씩 하락했고 operating profit은 2006년 이후 거의
정체됐다고 지적했다.

$18은 2013E 13x unlevered FCF, 10.6x EBIT, 11.7x P/E로 구조적 악화에 안전마진이 없으며
DCF fair value $11~14, downside case $4, upside $20을 제시했다. base case는 2020년까지
revenue 2.5% 성장이나 price 약 -5%를 포함했다.

## 12. 결과와 판정

사업진단은 대체로 맞았다. 2012~2017 consolidated revenue는 거의 정체했고 C2C margin은
28%에서 23%, core operating income은 21% 감소했다. management의 pricing과 buyback이
EPS·가격을 지지한다는 지적도 정확했다.

하지만 $18에서 upside $20로 제한한 분포가 틀렸다. 가격은 6개월 6.7% 하락해 전술적
수익이 났지만 1년에는 2.6% 상승, 3년 34.3%, 5년 26.2% 상승했다. 숏의 carry와 제한된
downside target을 감안하면 위험보상이 부족했다.

**종합판정: 대체로 실패.** thesis quality는 높았지만 valuation distribution과 촉매가
약했다. 장기 악화가 곧 단기간 multiple 하락을 뜻하지 않는다.

---

# Part F. 2014년 Long

## 13. 원 투자논지

Mexico corridor 가격재설정과 compliance 비용 급증을 구조적 파괴가 아닌 일시적 headwind로
봤다. WU는 200개국, 16,000 corridor와 500,000 agent를 가진 시장 1위이고 digital은 매출
5%에서 두 자릿수 성장했다. Xoom은 banked·소수 corridor, M-Pesa는 국내송금 중심이어서
core cash cross-border와 직접 동일하지 않다고 구분했다.

2014 revenue 성장 재개, 2015 profit 성장, compliance 비용 peak, 연 $0.9~1.0bn levered FCF,
$500m buyback과 offshore cash 활용으로 5년 +20% IRR을 기대했다.

## 14. 결과와 판정

2014 revenue +1.2%, operating income +3.0%, EPS $1.59로 단기 촉매는 맞았다. 주가도 1년
+23.1%, 3년 +35.2%였다. 그러나 2015~2016 revenue와 operating income은 다시 감소했고
5년 가격수익은 +27.8%, CAGR 약 5.0%로 20% IRR 목표를 크게 하회했다.

핵심 오류는 `일시적 요인도 존재한다`에서 `구조적 요인은 중요하지 않다`로 넘어간 것이다.
Mexico와 compliance 기저효과는 끝났지만 pricing·digital mix·경쟁으로 장기 성장은
복원되지 않았다.

**종합판정: 부분 성공.** 1년 촉매와 가격은 성공, 장기 compounder·20% IRR은 실패다.

---

# Part G. 2015년 Long

## 15. 원 투자논지

12x fully taxed FCF, 65.5% ROE와 2008년 이후 transaction volume 5.2% 성장을 강조했다.
90%가 cross-border이고 고객 대부분이 unbanked이므로 기술보다 regulation이 중요하며,
Xoom은 banked 고객을 대상으로 해 직접 대체가 아니라고 봤다. rising compliance가 작은
경쟁자를 퇴출시키고 WU의 scale을 강화한다는 논리였다.

2007년 이후 $5.6bn을 환원했고 10년 FCF $9.5bn을 만들었다. 실패한 B2B 인수와 compliance
정상화는 upside option으로 처리했다.

## 16. 결과와 판정

네트워크와 FCF는 유지됐지만 주가는 1년 -0.5%, 2년 +0.4%, 3년 +1.9%, 5년 +15.3%에
그쳤다. 배당을 포함하면 개선되나 요구수익과 시장 기회비용에는 부족했다. 2015~2017
C2C revenue와 operating income은 성장하지 않았다.

`barring Bitcoin, technological disruption is not likely`라는 결론은 기술이 회사를
즉시 없애지 않는다는 뜻에서는 맞았지만, digital price transparency와 자기잠식이
수익성을 서서히 낮추는 경로를 배제했다. 12x FCF는 현금이 안정적일 뿐 성장하지 않는다면
압도적 저평가가 아니다.

**종합판정: 실패.** 기업생존과 주주 복리를 혼동했다. moat가 남아 있다는 증거보다
증분 FCF·주당 FCF 성장의 원천이 필요했다.

---

# Part H. 2016년 Short

## 17. 원 투자논지

경쟁·가격압력, 2008~2011 대비 600~700bp margin 하락, 낮은 세율과 buyback이 가린 pretax
profit 감소를 지적했다. 핵심은 agent contract cost, software와 capex 자본화가 급증해
분기 EPS를 $0.04~0.05 높였다는 `accounting manipulation` 주장과 insider selling이었다.

촉매는 earnings miss와 시장이 자본화 관행을 인식하는 것이었다.

## 18. 결과와 판정

가격은 3개월에 0.7% 내려 잠깐 숏수익이었지만 1년 9.3%, 3년 6.1%, 5년 56.5% 상승했다.
명시한 earnings miss·회계 재평가 촉매도 주가를 지속적으로 낮추지 못했다.

margin과 pretax 압박은 사실이었지만 계약취득원가와 내부사용 software의 자본화는 경제적
판단이 필요한 회계정책이다. 분기 증가만으로 의도적 조작과 earnings miss를 확정하려면
상각기간, 신규·갱신계약 증가, cash capex와 감사·규제 restatement 증거가 필요했다.
회사는 이후에도 약 $1bn 안팎의 operating cash flow를 만들었다.

**종합판정: 실패.** 회계 quality 경고는 유효했지만 공격적인 회계와 fraud성 manipulation을
구분하지 않았고, 가격목표·손실한도도 부족했다.

---

# Part I. 2017년 Long

## 19. 원 투자논지

11년간 주가가 $19 부근에 정체됐고 share count는 37% 감소했다. 11x 2017E EPS에서
WU.com이 매출의 2016년 8%에서 2020년 15%로 커지고 20% 성장하면 전체 revenue에 300bp를
보태 2020 EPS 10~13% 성장을 만든다고 봤다. RemainCo는 1~2%만 성장하면 됐다.

WU.com을 3.5x revenue, RemainCo를 10x EBITDA로 평가해 2020년 $33, 배당 포함 3.5년 IRR
21%를 제시했다. MoneyGram 인수경쟁과 Xoom 거래를 비교하고 LBO 가능성도 촉매로 봤다.
intercompany working-capital program이 2019년경 끝나 buyback 재원이 줄 수 있다는 점은
인식했지만 debt capacity와 세제개편으로 보완 가능하다고 봤다.

## 20. 결과와 판정

가격은 1년 +5.1%, 2년 +32.8%, 3년 +34.5%로 양호했지만 $19→$33의 74% 상승과 21% IRR에는
못 미쳤고 5년에는 -3.2%로 반전했다. 배당을 포함하면 5년 총수익은 양수일 가능성이 높지만
lost decade 종료와 고성장 rerating은 실패했다.

WU의 디지털 적응 자체는 맞았다. 그러나 작은 고성장 segment의 기여를 계산할 때
RemainCo flat과 self-cannibalization, 낮은 digital pricing, 추가 technology·marketing
비용이 동시에 필요했다. 2019 total revenue는 전년보다 5.3%, 2020은 8.6% 감소했고,
2022 Business Solutions 매각 뒤 revenue base도 작아졌다.

**종합판정: 부분 성공.** 2~3년 가격과 digital asset 발견은 성공했지만 2020 EPS acceleration,
$33와 지속가능한 주당가치 성장에는 실패했다.

---

## 21. 9건을 관통하는 성공·실패 유형

### 유형 ① `moat exists`와 `moat economics stable`의 혼동

WU의 브랜드·agent·compliance network는 실제로 존재했고 회사는 살아남았다. 그러나
거래량이 늘어도 가격·agent·regulatory cost 때문에 revenue와 operating income은 줄었다.
moat의 존재는 지대의 방향과 크기를 보장하지 않는다.

### 유형 ② 기술 보급률을 기업 대체율로 바로 연결

2013년 smartphone 숏은 방향은 맞았지만 adoption에서 WU transaction 감소까지 필요한
banking, KYC, trust, receive method와 incumbent response를 건너뛰었다. 기술은 파괴자뿐
아니라 incumbent의 새 distribution channel이기도 했다.

### 유형 ③ 사업악화는 맞고 숏은 실패

2012·2013 숏은 margin 하락을 정확히 봤지만 낮은 시작가격, 현금흐름·buyback·배당과
붕괴하지 않은 terminal value를 과소평가했다. 숏에는 나쁜 기업이 아니라 시장 예상보다
더 빠른 악화와 촉매가 필요하다.

### 유형 ④ 일시적 headwind와 구조적 headwind의 동시 존재

2014 롱은 Mexico 가격 reset과 compliance 기저효과를 맞혔다. 하지만 일시적 문제가
해소돼도 장기 가격압력은 남았다. 사건의 정상화가 과거 성장률 복귀를 뜻하지 않는다.

### 유형 ⑤ 자사주가 만드는 EPS와 주주가치의 간극

buyback은 저가에서 주당가치를 지지했지만 영업이익 정체를 영구적으로 해결하지 못했다.
해외현금·intercompany payable·추가부채에 기대는 환원은 재원이 유한하다. `EPS growth`를
매출·영업이익·share count bridge로 분리해야 한다.

### 유형 ⑥ 작은 성장사업의 대기업 구원 오류

WU.com은 실제로 성장했지만 8%의 사업이 92%의 RemainCo 정체를 상쇄하려면 성장률뿐 아니라
절대 revenue contribution, margin과 cannibalization을 계산해야 했다.

---

## 22. 아이디어별 학습 태그

| 아이디어 | 태그 |
|---|---|
| 2007 Long | `network_moat`, `volume_to_profit_error`, `spin_debt`, `quality_at_wrong_price` |
| 2011 Long | `cash_to_cash_resilience`, `fcf_floor`, `impregnable_moat`, `partial_success` |
| 2012 Short | `thesis_right_price_wrong`, `expectations_already_low`, `buyback_support`, `short_carry` |
| 2013-06 Short | `technology_adoption_error`, `kodak_analogy`, `incumbent_adaptation` |
| 2013-08 Short | `good_business_analysis_bad_short`, `weak_catalyst`, `distribution_error` |
| 2014 Long | `temporary_vs_structural`, `catalyst_success`, `irr_miss`, `capital_return` |
| 2015 Long | `survival_vs_compounding`, `fcf_value_trap`, `digital_underestimation` |
| 2016 Short | `accounting_quality`, `capitalization_policy`, `fraud_inference`, `catalyst_failure` |
| 2017 Long | `small_segment_extrapolation`, `digital_self_disruption`, `sotp`, `timing_path` |

---

## 23. 재사용 체크리스트

1. transaction·subscriber가 늘 때 revenue per unit과 contribution profit도 늘고 있는가?
2. network가 유지되는 것과 take rate·margin이 유지되는 것을 분리했는가?
3. 신기술 보급률에서 실제 고객전환까지 필요한 조건과 conversion rate를 적었는가?
4. incumbent가 기존 브랜드·규제·distribution 위에 신기술을 얹을 수 있는가?
5. 숏 목표가가 현재가격에 이미 내재된 악화보다 충분히 나쁜 시나리오인가?
6. 배당·buyback·short carry를 포함해 촉매까지 기다릴 수 있는가?
7. 일시적 비용 정상화 뒤에도 구조적 단위경제성이 개선되는가?
8. 작은 고성장 segment의 절대 profit이 legacy decline을 상쇄하는 연도를 계산했는가?
9. EPS를 organic operating profit, 세율, share count와 일회성으로 분해했는가?
10. 회계 자본화가 공격적이라는 주장에 상각·cash flow·감사·restatement 증거가 있는가?

---

## 24. 주요 근거

- VIC 원문: [2007 Long](https://www.valueinvestorsclub.com/idea/Western_Union/6132878409),
  [2011 Long](https://www.valueinvestorsclub.com/idea/WESTERN_UNION_CO/2087178507),
  [2012 Short](https://www.valueinvestorsclub.com/idea/WESTERN_UNION_CO/0857797488),
  [2017 Long](https://www.valueinvestorsclub.com/idea/Western_Union/7865090123). 나머지 5건은
  제공 SQL 본문에 공개 URL이 없으므로 원문 텍스트 자체를 근거로 보존했다.
- [Western Union 2007 Form 10-K](https://www.sec.gov/Archives/edgar/data/1365135/000119312508038154/d10k.htm)
- [Western Union 2011 Form 10-K](https://www.sec.gov/Archives/edgar/data/1365135/000119312512078259/d257693d10k.htm)
- [Western Union 2012 Form 10-K](https://www.sec.gov/Archives/edgar/data/1365135/000136513513000008/wu-12312012x10k.htm)
- [Western Union 2013 Form 10-K](https://www.sec.gov/Archives/edgar/data/1365135/000136513514000014/wu-12312013x10k.htm)
- [Western Union 2017 Form 10-K](https://www.sec.gov/Archives/edgar/data/1365135/000136513518000013/wu-12312017x10k.htm)
- [Western Union 2021 Form 10-K](https://www.sec.gov/Archives/edgar/data/1365135/000095017022001962/wu-20211231.htm)
- [Western Union 2022 Form 10-K](https://www.sec.gov/Archives/edgar/data/1365135/000095017023004146/wu-20221231.htm)
- [Western Union 2023 Form 10-K](https://www.sec.gov/Archives/edgar/data/1365135/000095017024018751/wu-20231231.htm)
- [SEC Companyfacts — 연도별 revenue·operating income·EPS·cash flow·repurchase 교차검증](https://data.sec.gov/api/xbrl/companyfacts/CIK0001365135.json)

### 데이터 해석 주의

- 2016·2017 GAAP operating income와 EPS에는 DOJ/FTC 합의, 세금 등 큰 일회성 항목이 있어
  core C2C operating income과 구분했다.
- 장기 사업판정에는 평가기준일 현재 공개된 2023 실적까지만 사용했다.
- 가격은 VIC SQL 가격비율이며 dividend, benchmark, short borrow와 거래비용을 제외했다.
- 따라서 고배당 WU의 롱 총수익은 표보다 높고, 숏 총수익은 표보다 낮다.
