# Batch 003 — American Express (AXP), 금융위기 전후 완전 재분석 v2

대상: 2007-04-01 Long / 2008-06-12 Long / 2008-12-31 Long

## 0. 결론

| 게시일 | 방향 | 실제 가격경로 | 판정 |
|---|---|---|---|
| 2007-04-01 | Long | 1년 -21.7%, 2년 -75.6%, 5년 +5.2% | 실패 |
| 2008-06-12 | Long | 6개월 -47.9%, 1년 -43.7%, 3년 +8.4%, 5년 +77.0% | 진입 실패 |
| 2008-12-31 | Long | 1년 +109.6%, 2년 +122.0%, 5년 +382.8% | 매우 성공 |

SQL raw flag는 모두 Short지만 세 원문은 모두 Long이다. 핵심은 같은 franchise를 세 번 분석했는데 결과가 달랐다는 점이다. **사업품질은 거의 동일했고 바뀐 것은 credit loss, funding survival과 가격이었다.**

## 1. AXP는 무슨 기업인가

AXP는 Visa 같은 network-only 회사도, Capital One 같은 lender-only 회사도 아니다. 카드회원 모집·카드발급·가맹점 계약·결제 network·카드대출을 결합한 closed-loop spend-and-lend platform이다.

카드회원이 $100를 쓰면 가맹점은 AXP에 merchant discount를 지불한다. AXP는 rewards와 partner economics를 지급하고, 일부 고객에게는 revolving loan을 제공해 이자도 번다. 반면 가맹점에는 고객에게 돈을 받기 전에 결제대금을 지급해야 하므로 receivable funding이 필요하다.

따라서 flywheel은 `affluent member → 높은 spend → merchant가 높은 discount를 감수 → rewards/service 재투자 → retention과 spend 증가`다. 하지만 금융위기에는 반대 루프가 작동한다. `소비감소 → discount revenue 감소 + 실업 → charge-off 증가 + wholesale funding 경색 → 자본환원 중단`이다.

### 용어

- Billed business: 카드망을 통과한 총 결제액. 회사 매출이 아니다.
- Discount rate: 가맹점이 AXP에 지급하는 결제액 대비 수수료율.
- Charge-off: 회수가 어렵다고 판단해 손실 처리한 카드대출.
- Securitization: 카드채권을 묶어 증권화해 외부투자자에게 팔고 자금을 조달하는 방식.
- Bank holding company 전환: 예금·Fed 유동성 등 더 안정적인 금융조달에 접근하는 데 중요한 제도 변화.

## 2. 돈의 흐름과 핵심 KPI

`Billed business × merchant economics + card fees + net interest income - rewards/partner payments - marketing/service - credit losses - funding cost = shareholder earnings`.

따라서 billed business만 성장해도 credit provision과 funding cost가 더 빨리 오르면 equity earnings는 감소한다. 금융위기 배치의 핵심 KPI는 billed business, loan growth, delinquency, net write-off, provision/loan, wholesale funding 만기, deposit growth, capital ratio와 buyback capacity다.

# Part A — 2007-04-01 Long

## 3. 원 논지

약 15~17배 이익에 35% 전후 ROE, 두 자릿수 EPS 성장, 강한 closed-loop moat를 사는 아이디어였다. 2006 EPS $3.00+, 2007 $3.40, 2008 $3.80을 기대하고 18배를 적용해 약 $68 목표를 제시했다.

사업관찰은 상당히 정확했다. billed business와 cards-in-force는 증가했고 discount rate도 견조했다. 오류는 대출자산 약 $50bn을 시가총액 약 $67bn과 비교해 위험이 작다고 본 부분이다. **시가총액은 신용손실 흡수자본이 아니다.** 손실은 장부자기자본과 당기이익이 흡수하고, 단기채무는 실제 funding access가 결정한다.

2007년 managed lending balance가 빠르게 늘던 가운데 provision 증가율이 대출 증가율을 크게 웃돌기 시작했다. 수준값인 EPS/ROE는 좋았지만 변화율인 credit cost가 먼저 악화되고 있었다.

## 4. 실제 결과 / RECAP

1년 -21.7%, 2년 -75.6%, 3년에도 -26.1%, 5년 +5.2%였다. 배당을 넣어도 원래 기대한 두 자릿수 복리와 거리가 멀다.

- 맞춘 것: franchise quality, affluent spend, closed-loop economics.
- 틀린 것: lending/funding risk와 cyclicality.
- 숨은 가정: 높은 ROE가 funding regime과 무관하게 지속된다.
- 경고신호: provision growth, delinquency, securitization/funding spread.
- Valuation: 정상 EPS를 peak earnings에 적용.
- Timing: 실패.
- 최종: **좋은 기업을 잘못된 balance-sheet regime에서 산 실패.**

# Part B — 2008-06-12 Long

## 5. 왜 더 싸졌는데도 아직 일렀나

두 번째 Long은 가격하락으로 valuation이 좋아졌고 GNS, network economics와 장기 전자결제 성장을 강조했다. 문제는 가격이 싸졌다는 사실이 credit/funding 악화의 끝을 의미하지 않는다는 것이다.

GNS는 제3자 은행이 Amex 카드를 발급해 AXP가 신용위험을 덜 지면서 network fee를 버는 고자본효율 사업이다. 하지만 consolidated AXP에는 여전히 proprietary loan/receivable이 컸다. 고ROIC segment가 존재한다고 HoldCo 전체의 funding tail이 사라지지 않는다.

이 시점에는 소비, 주택, 고용과 자본시장이 동시에 악화 중이었다. 따라서 `normalized EPS × 낮은 multiple`보다 먼저 `12~24개월 funding need - committed liquidity - deposit access - stress credit loss`를 계산했어야 했다.

## 6. 실제 결과 / RECAP

6개월 -47.9%, 1년 -43.7%였다. 3년 +8.4%, 5년 +77%로 결국 회복했지만 “3년 내 2배”라는 원 기대에는 못 미쳤고 초기 drawdown은 매우 컸다.

- 맞춘 것: 장기 franchise와 GNS의 자본효율.
- 틀린 것: crisis duration과 equity path.
- 숨은 가정: AXP가 기존 funding 구조로 스트레스를 통과한다.
- 가장 큰 오류: 싸진 가격을 충분한 margin of safety로 착각.
- 최종: **장기 방향은 맞았으나 진입과 위험조정수익 실패.**

# Part C — 2008-12-31 Long

## 7. 세 번째 Long은 무엇이 달랐나

가격이 약 $18까지 떨어진 것만이 차이가 아니었다. AXP는 bank holding company로 전환했고 정부자본, FDIC 보증채 발행, 예금기반 확대 등 생존경로가 가시화됐다. 즉 6월에 가장 중요한 미지수였던 funding tail이 크게 줄었다.

이 아이디어는 “신용손실이 끝났다”가 아니라 **손실이 계속돼도 회사가 살아남을 가능성이 크게 올라간 상태에서 정상 franchise를 매우 낮은 가격에 산 것**이다. 같은 EPS 정상화 가정이라도 생존확률이 달라지면 equity expected value가 완전히 달라진다.

2009년 billed business와 EPS는 더 악화됐고 write-off도 높았다. 즉 매수 후 즉시 business turnaround가 온 것이 아니다. 그럼에도 funding survival이 확보되자 시장은 terminal franchise value를 다시 가격에 반영했다.

## 8. 실제 결과와 실제 투자판정

기존 가격계열상 1년 +109.6%, 2년 +122.0%, 5년 +382.8%였다. 5년 가격 CAGR은 대략 37% 수준이다(배당 제외). 이 결과는 2007·2008년 6월과 동일한 “좋은 회사” 주장 때문이 아니라 **survival-adjusted valuation**이 바뀌었기 때문이다.

### RECAP

- 맞춘 것: franchise survival, funding regime 변화, 극단적 valuation.
- 틀릴 수 있었던 부분: credit loss의 절대규모는 여전히 매우 불확실했다.
- 숨은 가정: 정부/예금/보증 조달이 충분히 작동한다.
- 경고신호가 아니라 확인신호: deposit growth, capital support, liquidity access.
- Business: 적중.
- Valuation: 매우 적중.
- Catalyst: funding stabilization.
- Timing: 매우 좋음.
- Security selection: common equity의 convex recovery를 정확히 선택.
- 최종: **매우 성공.**

# 9. 통합 Postmortem

세 글의 차이는 quality score가 아니다. 같은 기업에 대해 `Enterprise quality × survival probability × normalized earnings / entry valuation`이 시간에 따라 달라졌다.

2007년에는 quality를 맞히고 survival/funding cyclicality를 무시했다. 2008년 6월에는 가격은 싸졌지만 funding tail이 열려 있었다. 2008년 12월에는 가격이 더 싸졌고 동시에 funding tail이 닫히기 시작했다.

따라서 금융회사의 margin of safety는 낮은 P/E만으로 측정하지 않는다. `stress loss를 반영한 tangible capital + 12~24개월 funding coverage + 정부/예금 backstop + 정상 earnings power`를 먼저 계산한 뒤 equity valuation을 한다.

가격성과는 기존 VIC DB 계열을 사용하며 배당은 별도 확인 전 제외한다.