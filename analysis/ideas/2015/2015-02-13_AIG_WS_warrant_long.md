# American International Group warrants (AIG.WS) — 2015-02-13 VIC Long

**판정: 실패.** 작성자 stanley339.

2015년 2월, stanley339는 AIG 워런트를 사자고 제안했다. 2013년 11월 같은 작성자가 보통주로 쓴 논지를 레버리지가 있는 증권으로 옮긴 글이다. SQL의 Short는 오류이고 실제는 Long이다. 작성자는 2021년 말 BVPS $140을 전제로 4~5배의 수익을 계산했다. 실제 2021년 말 BVPS는 $79.97이었고, 더 근본적으로 워런트는 그보다 약 11개월 전인 2021년 1월 19일에 만기를 맞았다. 계산상 만기 가치는 약 $0.02다.

## 투자 논지

AIG는 BVPS $78의 0.69배에 거래되었다. 작성자는 Black-Scholes가 장기 워런트를 체계적으로 저평가한다고 보고, 대신 보통주의 장기 내재가치로 워런트를 평가했다. 2015년 ROE 약 6%가 2021년 약 10%로 오르고, 2015~2018년 순이익만큼 자사주를 사면 BVPS가 연 약 9% 성장해 2021년 말 $140이 된다는 계산이다. 1배면 워런트는 $95, 연 27%이고, 1.2배면 $123, 연 32%였다. 원문에는 워런트 가격이 적혀 있지 않은데 이 수익률에서 역산하면 약 $23이다. 하방으로는 2년 뒤 주가가 애널리스트 목표 $62이고 변동성이 35%로 줄면 본전이라고 했고, $45 이하로 끝나면 0이 된다는 점과 Fairholme이 3분의 1을 보유해 유동성이 낮다는 점도 밝혔다.

## 실제로 일어난 일

게시 후 2년간 주가는 작성자의 보수적 시나리오를 넘어섰다. 2017년 2월 $66.14로 $62보다 높았고 고점 $67.20에서 내재가치는 약 $22.20이었다. 그러나 이 값은 역산 진입가 약 $23과 거의 같다. 시간가치를 뺀 하한이므로 실제 시세는 더 높았겠지만 일별 시세를 구하지 못해 얼마나 벌 수 있었는지는 말할 수 없다. 같은 달 2016년 4분기 $5.6bn의 준비금 강화가 나왔다. BVPS는 2016년 $76.66, 2018년 $65.04로 내렸고 조정 ROE는 2015년 3.7%, 2016년 0.6%, 2017년 4.1%, 2018년 2.1%였다. 합산비율은 2019년 99.6으로 돌아서기 시작했지만 2020년 3월 주가는 $18.78이 되었다. 주가 회복과 2022년 합산비율 91.9는 만기 뒤의 일이다.

## 왜 틀렸나

세 겹의 오류가 있다. 첫째, BV가 연 9% 복리로 성장한다는 전제가 틀렸다. 2012~2014년 BVPS가 $66.38에서 $77.69로 늘어 그럴듯해 보였지만 준비금 강화가 없어야 성립하는 계산이었고, 실제로는 약 7년간 $78에서 $79.97로 거의 움직이지 않았다. 둘째, 계산 시점이 틀렸다. 원문은 만기가 2021년 1월이라고 적으면서 2021년 말 BV로 가치를 계산했다. 2013년 5월의 다른 워런트 글에 있던 같은 불일치가 되풀이된 것이다. 셋째, 약 $14로 추정되는 시간가치를 지불했기 때문에 비슷한 판단을 보통주로 했을 때보다 여유가 훨씬 적었다. 보통주는 만기일까지 -21.7%(배당 제외)에 그쳤고 2026년 10월까지는 배당 포함 +99.9%였다.

뒤처지던 논지에 레버리지를 더했다는 점도 짚어야 한다. 2013년 11월 글은 ROE 10%를 전제로 했는데 15개월 뒤의 이 글은 2015년 ROE를 약 6%로 잡고 있었다. 이때 필요한 것은 논지 재검증이지 더 큰 레버리지가 아니었다.

## 앞으로 비슷한 아이디어를 볼 때

옵션의 수익표는 반드시 만기일 기준으로 다시 계산해야 한다. 장기 복리 전망을 쓸 때는 직전 몇 년의 성장이 어떤 충격 없이 나온 숫자인지 먼저 확인한다. 그리고 같은 논지를 보통주로 표현했을 때의 결과와 나란히 놓고, 시간가치를 내고도 더 나은지 따져 본다.

## 유사 사례

같은 증권의 다른 글은 [2011년 9월 워런트 Long](../2011/2011-09-26_AIG_WS_warrant_long.md)과 [2013년 5월 워런트 Long](../2013/2013-05-08_AIG_WS_warrant_long.md)이다. 작성자의 원래 논지는 [AIG 2013년 11월 Long](../2013/2013-11-06_AIG_long.md)에서 볼 수 있다. 같은 턴어라운드를 만기 없는 보통주로, 그것도 숫자가 돌아서기 직전에 산 사례가 [AIG 2018년 11월 보통주 Long](../2018/2018-11-18_AIG_common_long.md)이다.

## 근거 자료

VIC source-DB preserved original, [AIG FY2018 Form 10-K](https://www.sec.gov/Archives/edgar/data/5272/000000527219000023/maindocument001.htm), [AIG 424B2 — warrant terms as of 2018](https://www.sec.gov/Archives/edgar/data/0000005272/000119312518090260/d475031d424b2.htm), [AIG announces adjustments to warrant exercise price](https://www.nasdaq.com/press-release/aig-announces-adjustments-to-warrant-exercise-price-and-shares-receivable-upon-1), [AIG issues reminder regarding expiration of warrants](https://aig.gcs-web.com/news-releases/news-release-details/aig-issues-reminder-regarding-expiration-warrants), [AIG FY2019 results / Form 10-K](https://www.sec.gov/Archives/edgar/data/5272/000110465920023889/aig-20191231.htm), [AIG reports 4Q and FY2022 results](https://www.sec.gov/Archives/edgar/data/5272/000110465923022410/tm236915d1_ex99-1.htm), [AIG's losing streak continued in Q4](https://amp.insurancejournal.com/news/national/2017/02/15/441852.htm), [AIG daily close / adjusted close](https://finance.yahoo.com/quote/AIG/history/).

**검색 태그:** 워런트 · 옵션 만기 · 계산 시점 오류 · 장부가 복리 전망 · 시간가치 · 턴어라운드 · 레버리지 재표현
