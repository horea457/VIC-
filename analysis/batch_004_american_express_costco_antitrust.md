# Batch 004 — American Express, Costco 이탈과 반독점 완전 재분석 v2

대상: 2015-05-11 Long / 2016-07-05 Long / 2018-06-14 Short

## 0. 결론

| 아이디어 | 방향 | 실제 가격경로 | 판정 |
|---|---|---|---|
| 2015 Long | Long | 1년 -16.6%, 2년 +3.0%, 3년 +34.8%, 5년 +17.0% | 부분 성공 |
| 2016 Long | Long | 6개월 +27.3%, 1년 +45.2%, 3년 +120.8%, 5년 +207.8% | 매우 성공 |
| 2018 Short | Short | 3개월 -9.9%, 1년 -25.7%, 3년 -74.1% 숏 가격손익 | 치명적 실패 |

raw SQL은 모두 Short지만 2015/2016은 명백한 Long이다.

## 1. 기업과 가치사슬

AXP는 카드회원과 가맹점을 직접 연결하고 카드발급·network·merchant acquiring·일부 lending을 함께 수행하는 closed-loop 플랫폼이다. 이 구조 때문에 Costco 같은 대형 partner는 단순 매출고객이 아니다. 회원획득, 카드사용, loan balance와 merchant volume을 동시에 제공한다.

공동브랜드 계약에서 돈의 흐름은 대략 `partner가 고객접점 제공 → AXP가 카드 발급/보상 제공 → 회원이 partner 및 외부에서 지출 → AXP가 merchant discount·interest·fee 획득 → partner에 rebate/경제성 지급`이다. 계약갱신 때 partner의 협상력이 높아지면 AXP의 economics가 압박받는다.

**Steering**은 가맹점이 고객에게 더 싼 결제수단을 권하거나 유도하는 행위다. AXP의 anti-steering 조항은 가맹점이 높은 AXP 수수료를 피하기 위해 다른 카드를 권하는 것을 제한했다. 따라서 반독점 소송은 법률문제가 곧 take-rate 문제였다.

## 2. 핵심 KPI

Billed business, discount rate/revenue, cards-in-force, cobrand concentration, partner payments, rewards expense, loan balances/provision, share count, organic revenue ex-partner loss를 본다. 특히 event-driven 분석에서는 headline EPS가 아니라 `lost partner economics → replacement spend → acquisition cost → normalized EPS` bridge가 필요하다.

# Part A — 2015-05-11 Long

## 3. 논지

약 $79.50, 14배 P/E에서 Costco·JetBlue 이탈과 anti-steering 1심 패소가 과도하게 반영됐다고 봤다. affluent customer와 closed-loop moat가 유지되고 Costco를 수익성 나쁜 조건으로 갱신하지 않은 것은 오히려 자본배분 규율이라는 해석이었다.

Costco는 회원·billings·loan book에 동시에 영향을 주므로 손실 규모가 단순 revenue percentage보다 복잡하다. AXP는 Costco loan portfolio를 넘기고 회원관계를 잃으며 replacement acquisition을 해야 했다. 따라서 진짜 질문은 “Costco가 없어도 회사가 좋은가?”가 아니라 **기존 EPS에서 Costco contribution을 제거하고 replacement investment를 넣은 뒤 얼마를 버는가**였다.

원문은 2017년 성장 재개와 multiple expansion을 촉매로 봤다. 방향은 맞았지만 2015년에는 아직 earnings reset의 바닥이 확인되지 않았다.

## 4. 실제 결과 / RECAP

2016년 billed business와 discount revenue는 Costco 이탈 영향으로 흔들렸고 headline EPS에는 portfolio sale gain이 섞였다. 2017년에는 Costco와 FX 영향을 제외한 revenue가 다시 성장하고 cardmember spending이 회복됐다. 즉 franchise destruction은 일어나지 않았다.

가격은 1년 -16.6%, 2년 +3.0%, 3년 +34.8%, 5년 +17.0%. 5년 CAGR은 약 3% 수준으로 opportunity cost가 컸다.

- 맞춘 것: moat 생존, Costco 포기의 장기 합리성, 2017 성장 재개.
- 틀린 것: reset 전 14배가 충분히 싸다는 판단.
- 숨은 가정: replacement economics가 빠르게 나타난다.
- 경고신호: organic EPS bridge가 불명확한데 one-time sale gain이 headline을 지지.
- 최종: **사업논지는 맞았으나 진입가격/시점은 평범.**

# Part B — 2016-07-05 Long

## 5. 왜 1년 뒤 같은 회사가 훨씬 좋은 투자가 됐나

이번에는 약 $59.15, 10.6배 수준이었다. 더 중요한 것은 Costco portfolio 이전과 손익 reset이 실제 숫자에 반영되기 시작했다는 점이다. uncertainty가 사건 전 추정치에서 사건 후 관측치로 바뀌었다.

Costco 회원을 잃은 뒤에도 proprietary spend, premium franchise와 다른 cobrand가 유지됐고 share repurchase가 낮아진 가격에서 더 많은 주식을 소각할 수 있었다. 따라서 `낮은 multiple + 정상화되는 organic growth + buyback`이 동시에 작동했다.

이 차이는 매우 중요하다. 2015년 Long은 “충격이 생각보다 작을 것”에 베팅했다. 2016년 Long은 “충격을 실제로 맞고도 남은 사업이 이 정도이며 가격은 더 낮다”에 베팅했다. 후자가 정보집합이 훨씬 좋다.

## 6. 실제 결과 / RECAP

6개월 +27.3%, 1년 +45.2%, 3년 +120.8%, 5년 +207.8%. 5년 가격 CAGR은 약 25%다.

- 맞춘 것: residual franchise, growth normalization, buyback convexity.
- valuation: 매우 좋음.
- catalyst: Costco base effect 종료와 organic growth 확인.
- timing: 매우 좋음.
- 최종: **같은 quality를 사건 후 낮은 가격에 산 매우 성공적인 Long.**

# Part C — 2018-06-14 Short

## 7. 이 숏은 사실상 법률확률 베팅이었다

핵심은 Supreme Court가 anti-steering 사건에서 AXP에 불리하게 판결할 확률을 약 90%로 보고, 패소 시 merchant discount 하락과 손해배상/경쟁압력으로 기업가치가 20~40% 훼손된다고 본 것이다.

이진 촉매에서는 expected value를 `P(win)×upside + P(loss)×downside`로 계산해야 한다. 여기서 가장 위험한 부분은 90%라는 확률이다. 법률전문가 의견, certiorari 통계와 oral argument 인상은 참고자료지만 독립된 90% 확률을 보장하지 않는다.

또한 판결이 불리해도 실제 merchant behavior가 얼마나 변하는지는 별도 단계다. `법적 패소 → steering 증가 → discount rate 하락 → billed business/retention 변화 → EPS`라는 여러 조건부 확률을 곱해야 한다. 원문은 첫 단계 확률을 높게 잡으면서 후속 경제효과도 강하게 연결했다.

## 8. 실제 결과 / RECAP

Supreme Court 결과는 핵심 전제와 반대로 나왔다. 그 순간 후속 fee compression thesis의 주요 촉매도 약해졌다. 숏 가격손익은 3개월 -9.9%, 1년 -25.7%, 3년 -74.1%였다. 배당과 borrow cost를 넣으면 더 나빴을 수 있다.

- 맞춘 것: merchant fee가 AXP moat의 중요한 경제적 변수라는 점.
- 틀린 것: 판결확률과 conditional damage.
- 숨은 가정: 전문가 consensus를 objective probability처럼 사용.
- 사전 경고: binary legal event에서 90% confidence 자체가 position-size 경고였다.
- Business: 판결 후 구조붕괴 없음.
- Valuation: 실패.
- Catalyst: 정반대.
- Security selection: unlimited-loss common short가 부적절하게 convex.
- 최종: **치명적 실패.**

# 9. 통합 Postmortem

이 배치는 event-driven investing에서 `사건 전 추정`과 `사건 후 관측`의 가치 차이를 보여준다. 2015 Costco Long은 결과가 아직 손익에 들어오기 전이었고, 2016 Long은 reset 후 잔존 franchise를 더 싼 가격에 샀다. 2018 Short는 반대로 결과가 나오기 전 법률확률에 과도한 확신을 부여했다.

앞으로 사건형 투자는 `base business value + event probability × incremental value - uncertainty haircut`으로 보고, 이진 법률/규제 촉매는 전문가 숫자를 그대로 확률로 쓰지 않는다.