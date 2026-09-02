# Batch 001 — Farfetch (FTCH) 상세 분석

평가기준일: 2024-01-31
분석일: 2026-09-02
대상 VIC 아이디어: 2019-08-08 Short, 2021-08-03 Long

## 결론부터

| VIC 아이디어 | 실제 방향 | 가격 결과 | 논지 결과 | 종합판정 |
|---|---:|---:|---:|---:|
| 2019-08-08 | Short | 최종적으로 매우 큰 성공 | 절반 정도 적중 | 성공, 단 경로위험 매우 큼 |
| 2021-08-03 | Long | 사실상 전액 손실 | 핵심 수익성·점유율 가정 실패 | 치명적 실패 |

두 글을 함께 보면 Farfetch 사례의 핵심이 더 선명해진다.

> **Farfetch의 marketplace와 기술자산에는 실제 가치가 있었지만, 그 자산이 높은
> 수익성을 가진 연결기업과 안전한 상장주주 지분을 보장하지는 않았다.**

2019년 숏은 적자 플랫폼의 높은 밸류에이션과 전사 비용구조를 정확히 의심했다.
게시 다음 날 주가는 $18.25에서 $10.13으로 44% 넘게 하락했고 2023년 말 기존
보통주의 잔존가치는 사실상 0이 됐다. 그러나 브랜드의 즉각적인 DTC 이탈과
Alibaba·LVMH 24S가 붕괴를 만든다는 구체적 인과는 맞지 않았다. 더구나 주가는
2021년 $73.35까지 올라 숏 포지션은 최종 결론이 맞기 전에 파괴될 수 있었다.

2021년 롱은 명품 온라인화, e-concession의 효용, Farfetch의 폭넓은 상품·브랜드
네트워크라는 사업적 장점을 잘 봤다. 하지만 이를 `GMV 성장 → 네트워크 효과 →
30% EBITDA margin → $60~90bn 가치`로 직선 외삽했다. 연결기업에는 New Guards,
Browns, Stadium Goods, 재고, 기술개발비, 마케팅비, M&A와 전환사채가 함께 있었다.
결국 사업·자산은 Coupang에 인수돼 살아남았지만 Farfetch Limited의 기존 보통주는
그 가치를 가져가지 못했다.

---

## 1. Farfetch는 무슨 기업이었나

Farfetch를 단순히 “명품 온라인 쇼핑몰”로 보면 두 투자 아이디어를 모두 잘못
이해하게 된다. 회사는 시기별로 네 가지 성격이 섞인 복합기업이었다.

### ① Farfetch Marketplace — 제3자 명품 마켓플레이스

세계 각지의 명품 브랜드와 독립 부티크가 가진 재고를 한 앱과 웹사이트에 모아
글로벌 소비자에게 보여주는 사업이다. 소비자는 여러 부티크를 따로 방문할 필요 없이
폭넓은 브랜드와 SKU를 한 번에 검색·결제할 수 있다.

거래 흐름은 대체로 다음과 같다.

> 브랜드·부티크가 재고와 상품정보 제공
> → Farfetch가 고객획득·검색·결제·국가별 현지화·배송연결·CS 제공
> → 판매자가 상품을 출고
> → Farfetch가 거래액의 약 30%와 경우에 따라 물류 관련 수익을 수취

전통적인 온라인 리테일러가 상품을 먼저 사서 재고위험을 부담하는 것과 달리,
Farfetch의 제3자 거래는 판매자가 재고를 보유했다. 그래서 핵심 Marketplace만 보면
재고 부담이 작고 GMV가 늘 때 수수료 매출이 따라오는 asset-light 모델이었다.

### ② e-concession — 브랜드가 통제권을 유지하는 입점 방식

명품 브랜드는 일반 도매판매를 꺼린다. 리테일러가 할인하거나 잘못된 맥락에서
상품을 진열하면 희소성과 가격질서가 훼손될 수 있기 때문이다.

Farfetch의 e-concession에서는 브랜드가 다음을 계속 통제할 수 있었다.

- 어떤 상품을 올릴지
- 재고를 얼마나 배정할지
- 판매가격과 할인정책
- 브랜드 표현과 고객경험의 일부

따라서 브랜드 입장에서는 “제3자에게 재고를 넘긴 도매”보다 **Farfetch 안에 만든
자기 매장**에 가까웠다. 이것이 2021년 롱이 본 가장 중요한 경쟁우위였다.

### ③ Farfetch Platform Solutions(FPS) — 명품업계용 전자상거래 인프라

FPS는 Farfetch.com만 운영하는 사업이 아니다. 브랜드와 백화점이 자체 사이트를
운영할 때 필요한 기술, 주문관리, 결제, 국가별 세금·통화, 글로벌 배송, 고객서비스,
재고연결을 흰색상표 형태로 제공했다.

즉 소비자에게 보이는 marketplace가 아니라 기업 고객의 뒤에서 작동하는
**명품산업용 Shopify + 결제·물류·현지화 인프라**에 가까운 사업이다. 2022년
Richemont·YNAP 계약은 이 사업이 Cartier, Van Cleef & Arpels 같은 대형 브랜드의
인프라가 될 가능성을 보여준 사건이었다. 그러나 계약 발표와 실제 onboarding은
다른 문제였다.

### ④ 직접 보유 리테일·브랜드 사업 — asset-light가 아닌 부분

연결재무제표에는 Marketplace 외에도 다음 사업이 들어 있었다.

- **Browns**: 런던 명품 부티크와 자체 온라인 리테일
- **Stadium Goods**: 스니커즈 리셀 플랫폼·리테일
- **New Guards Group(NGG)**: Off-White, Palm Angels 등 브랜드의 디자인·생산·
  라이선스·도매유통을 담당하는 Brand Platform
- 직접 운영 점포와 자체 보유 재고

특히 2019년 $675m로 발표된 New Guards 인수는 Farfetch를 “수수료만 받는
marketplace”에서 재고·브랜드·생산·도매가 섞인 기업으로 바꿨다. SEC 자료상 최종
인수대가는 취득현금을 제외하기 전 $704.1m였다. 이후 연결실적의 매출과 마진,
운전자본, 재고위험을 해석할 때 Marketplace의 asset-light 특성만 적용할 수 없게
됐다.

---

# Part A. 2019년 Short

## 2. 원래 투자 논지

2019년 글은 Farfetch가 매출 약 6.5배에 거래되지만 흑자와는 거리가 멀다는 데서
출발한다. 저자는 시장의 강세론을 “명품의 Amazon, 최종 category killer”라고
요약하고 그 전제가 틀렸다고 주장했다.

### 논지 ① 성공한 브랜드가 플랫폼을 졸업한다

초기 브랜드에는 Farfetch가 유용하다. 전 세계 고객에게 노출되고 물류·결제·마케팅을
직접 만들 필요가 없기 때문이다. 그러나 브랜드가 충분한 인지도를 얻으면 약 30%의
take rate를 계속 낼 이유가 줄어든다.

원문의 예상 메커니즘은 다음과 같다.

> Farfetch가 신생 브랜드를 키움
> → 브랜드가 임계규모 도달
> → 자체 DTC 채널 구축
> → Farfetch에서 인기 브랜드 이탈
> → Farfetch는 계속 새로운 브랜드를 발굴해야 함

즉 네트워크 효과가 누적되는 플랫폼이 아니라, 성공한 공급자가 빠져나가는
“브랜드 교체 treadmill”이라는 주장이다.

### 논지 ② 인기 재고는 브랜드가 자체 채널에 남긴다

명품은 수요보다 공급이 적다는 느낌을 유지해야 한다. 따라서 브랜드 관리자는
인기 SKU를 자사몰과 직영점에 우선 배정하고, 판매가 어려운 상품만 Farfetch에
보낼 유인이 있다는 논리다.

이 주장이 맞으면 Farfetch의 36만개 SKU 같은 외형적 폭은 커져도 실제 소비자가
원하는 핵심 상품의 질은 낮을 수 있다. 선택의 폭이 네트워크 효과가 아니라
열위재고의 집합이 될 위험을 지적한 것이다.

### 논지 ③ 고객획득비와 프로모션 때문에 주문이 전사적으로 적자다

저자는 전직 임원 인터뷰와 검색·웹트래픽·카드데이터를 근거로 미국에서 keyword
bid와 CAC가 급등하고 있다고 주장했다. 2019년 2분기와 7월 프로모션 강도가 과거
어느 때보다 높아졌으며, 전직 Chief Growth Officer의 취지상 모든 주문이
below-the-line에서 손실이라는 설명도 제시했다.

핵심은 “주문 총이익이 양수인가”가 아니라 다음 비용까지 포함한 뒤 돈을 버는가였다.

- 고객획득·재구매 마케팅
- 글로벌 배송과 반품·관세 보조
- 기술개발·데이터센터
- 고객서비스와 본사인력
- 주식보상과 인수 후 고정비

### 논지 ④ 지역별 경쟁이 동시에 강해진다

- 미국: 브랜드의 DTC 광고투자 확대
- 중국: Alibaba의 명품 marketplace 진출
- 유럽: LVMH의 24S 확장

Farfetch가 winner-take-most 플랫폼이 되지 못하면 적자기업의 6.5배 매출가치는
유지되기 어렵다는 논리였다.

### 논지 ⑤ 하방은 20%가 아니라 거의 0이다

이 숏은 단기 실적 미스에 따른 20% 조정을 노린 것이 아니었다. 시장이 부여한
category winner 지위가 무너지면 최종 equity value가 “0 + 조금”까지 갈 수
있다고 봤다. 다만 저자도 타이밍 확신이 낮고 주가가 단기 급등할 수 있다고 명시했다.

## 3. 실제 결과

### 게시 직후: 가격은 즉시 맞았지만 촉매는 더 복합적이었다

2019년 8월 8일 종가 $18.25였던 주가는 다음 날 $10.13으로 44% 넘게 하락했다.
같은 날 Farfetch는 Q2 손실 확대와 New Guards Group 인수를 발표했다. Q2 매출은
예상을 웃돌았지만 순손실은 전년 $17.6m에서 $89.6m으로 커졌고, $675m 규모의
인수가 marketplace의 자본집약도와 자본배분 우려를 키웠다.

따라서 **“실적 약화가 높은 밸류에이션을 무너뜨린다”는 촉매는 적중**했지만,
하락 전부를 브랜드 이탈·24S·Alibaba 경쟁의 증거로 볼 수는 없다. 시장이 가장
크게 반응한 것은 확대된 손실과 대형 M&A였다.

### 2019~2021년: 핵심 경쟁 인과는 오히려 반대로 움직였다

Farfetch의 GMV는 2019년 $2bn을 넘었고, 2021년에는 $4.2bn까지 성장했다. 2020년
Alibaba와 Richemont는 Farfetch에 각각 $300m를 투자하고 중국 JV에도 각각
$250m를 투자하기로 했다. 숏이 두려워한 Alibaba는 단순 경쟁자가 아니라 Farfetch의
중국 유통 파트너가 됐다.

2021년에는 active consumer와 브랜드 관계가 확대됐고, 2022년에는 Richemont의
대부분 Maisons와 YNAP가 FPS를 채택하고 다수 브랜드가 Farfetch에 e-concession을
열기로 한 계약까지 발표됐다. 이것은 “브랜드가 빠르게 졸업해 플랫폼이 곧
공동화된다”는 강한 형태의 숏 논지와 맞지 않는다.

### 그러나 거래 성장과 전사 수익성의 간극은 끝내 닫히지 않았다

2021년 GMV $4.2bn, 매출 $2.3bn을 기록했지만 full-year adjusted EBITDA는
$1.6m, 마진 0.1%였다. 2022년 GMV는 $4.1bn으로 감소했고 2023년 Q2 adjusted
EBITDA는 -$30.6m, 마진 -6.4%였다.

2019년 숏이 본 “주문 성장과 전사 돈벌이는 다르다”는 문제는 정확했다. 다만 실제
손실의 원인은 CAC 하나가 아니라 다음이 결합됐다.

- Marketplace 외 Brand Platform·직접 리테일의 재고와 고정비
- New Guards, Stadium Goods 등 M&A와 통합비용
- 기술개발비와 자본화된 프로젝트
- 주식보상·감가상각·본사비
- 중국·미국 수요둔화와 markdown 증가
- 차입과 유동성 악화

### 최종 상태: equity는 사실상 0

2023년 12월 NYSE는 거래를 즉시 정지했다. Farfetch는 자산매각이 완료되면 Class
A/B 보통주와 전환사채 보유자에게 남는 가치가 없을 것으로 예상한다고 공시했다.
2024년 1월 Coupang 컨소시엄은 사업·자산을 인수하고 기존 term loan $633m을
인수했다. 사업자산은 살아남았지만 기존 상장주주의 청구권은 살아남지 못했다.

## 4. 2019년 숏에서 맞은 것과 틀린 것

| 원래 주장 | 판정 | 구체적 이유 |
|---|---:|---|
| 적자기업의 6.5배 매출가치는 취약 | 맞음 | Q2 손실·M&A 발표 직후 44% 하락, 최종적으로 equity 잔존가치 없음 |
| 주문 증가가 전사 이익으로 연결되지 않음 | 맞음 | 2021년 기록적 GMV에도 adjusted EBITDA margin 0.1% |
| 성공 브랜드가 빠르게 플랫폼을 졸업 | 대체로 틀림 | 브랜드·GMV 확대와 Richemont 계약은 반대 정황; 최종 붕괴의 직접 원인도 아님 |
| 인기 SKU가 자사채널에만 남음 | 검증 불충분 | SKU별 채널 배정과 판매속도 자료가 없어 공개자료만으로 판정 곤란 |
| Alibaba와 24S가 플랫폼을 압박 | 대체로 틀림 | Alibaba는 대형 투자자·JV 파트너가 됐고 24S가 붕괴의 주원인이라는 증거 없음 |
| 최종 하방은 거의 0 | 맞음 | 2023년 회사가 보통주 잔존가치가 없을 것으로 예상 |

## 5. 2019년 숏의 최종 판정

**종합은 성공**이다. 게시 다음 날 큰 수익기회가 있었고 최종 방향도 완전히 맞았다.
그러나 “강한 성공”으로 분류하지 않는 이유는 두 가지다.

첫째, 원문이 제시한 핵심 경쟁 인과보다 **대형 M&A, 연결기업 비용구조, 현금소모와
부채**가 실제 붕괴에 더 중요했다. 둘째, 주가는 2021년 2월 $73.35까지 올라
게시일 종가 대비 약 4배가 됐다. 초기 급락 때 이익을 실현하지 않고 terminal short를
유지했다면 300%가 넘는 mark-to-market 역행을 견뎌야 했다.

> **학습점:** 숏은 최종 결론만 맞으면 되는 투자가 아니다. 촉매, 보유기간,
> 최대 역행폭과 대차·마진 생존까지 맞아야 실제 투자로 성공한다.

---

# Part B. 2021년 Long

## 6. 원래 투자 논지

2021년 글은 시가총액 $16.5bn에서 Farfetch를 장기 보유할 수 있는 명품산업의
독보적 플랫폼으로 봤다. 논리는 세 개의 성장률이 겹친다는 데서 출발한다.

### 논지 ① 명품시장 자체가 성장한다

당시 글로벌 개인명품 시장을 약 $300bn으로 봤고, 2030년에는 약 $600bn까지
확대될 수 있다고 예상했다. 밀레니얼·Z세대와 중국 소비자가 성장을 이끈다는
전제였다.

### 논지 ② 명품의 온라인 침투율이 상승한다

명품 브랜드는 브랜드 통제와 고객경험 때문에 온라인 전환이 늦었지만, 소비자가
온라인을 싫어해서가 아니라 Amazon 같은 범용 플랫폼이 명품에 맞지 않았기
때문이라고 해석했다. 코로나로 2020년 온라인 비중이 약 23%까지 올라갔고,
2025년에는 최소 35% 수준이 가능하다고 봤다.

### 논지 ③ Farfetch가 온라인 안에서도 점유율을 높인다

2020년 온라인 명품시장 약 $59bn에서 Farfetch GMV $3bn은 5.4% 점유율이었다.
2017년 3.4%에서 이미 상승했으므로 5~7년 안에 온라인 점유율이 다시 두 배가 될 수
있다고 예상했다.

세 효과를 결합하면 다음과 같다.

> 전체 명품시장 성장
> × 온라인 침투율 상승
> × Farfetch 온라인 점유율 상승
> = 5~7년 뒤 GMV $15~20bn

### 논지 ④ SKU 폭과 e-concession이 네트워크 효과를 만든다

2020년 말 약 36만 SKU, 3,500개 브랜드, 1,400개 판매자를 보유해 경쟁사보다
압도적인 선택폭을 갖췄다고 봤다. 소비자는 여러 브랜드 앱을 설치하는 대신 상품이
가장 많은 Farfetch를 선택하고, 고객이 모이면 더 많은 브랜드가 입점하는 선순환을
기대했다.

e-concession이 브랜드의 가격·재고 통제권을 보장하므로 대형 브랜드가 플랫폼을
떠날 유인도 크게 줄었다고 봤다. YNAP처럼 재고를 직접 사는 전통 온라인
리테일러보다 Farfetch가 더 asset-light하고 빠르게 확장할 수 있다는 비교였다.

### 논지 ⑤ Alibaba JV가 중국의 비대칭 성장기회를 연다

중국은 세계 명품수요의 약 3분의 1이며 수년 내 절반까지 커질 수 있다고 예상했다.
Farfetch가 Tmall Luxury Pavilion의 핵심 위치에 들어가 Alibaba의 방대한 이용자에게
접근하고, 중국에 없던 다수 글로벌 브랜드를 공급하면 중국 고객을 빠르게 확보할 수
있다는 논리였다.

### 논지 ⑥ 현재 적자는 성장투자이며 장기 EBITDA margin 30%가 가능하다

저자는 높은 LTV/CAC와 개선되는 고객획득 회수기간을 근거로 당장의 적자를 문제로
보지 않았다. 고객을 싸게 확보할 수 있을 때 마케팅을 줄여 흑자를 만드는 것보다
점유율을 먼저 확보하는 것이 합리적이라는 판단이었다.

규모가 커지면 다음 비용이 매출보다 느리게 늘어난다고 봤다.

- G&A와 기술 플랫폼 고정비
- 국가 간 물류비 비중
- 고객획득비
- 개인화·로열티 운영비

그래서 장기 adjusted EBITDA margin 30%를 “충분히 달성 가능”하다고 평가했다.

### 논지 ⑦ 밸류에이션은 장기 EBITDA 잠재력에 비해 싸다

원문의 가치계산은 다음과 같다.

| 항목 | 장기 가정 |
|---|---:|
| GMV | $20bn |
| 매출 | $10bn |
| adjusted EBITDA margin | 30% |
| adjusted EBITDA | $3bn |
| 적용 배수 | 20~30배 |
| 암시 가치 | $60~90bn |

당시 시가총액 $16.5bn과 비교하면 약 3.6~5.5배의 가치상승 여지가 있다는 계산이다.
2030년 $600bn 명품시장의 10~15%가 Farfetch를 통과하는 경우도 비현실적이지
않다고 봤다.

## 7. 이 논지가 당시 매력적으로 보였던 이유

사후 결과만 보면 무리한 낙관처럼 보이지만 2021년 당시에는 강세론을 지지하는
증거가 있었다.

- Q1 2021 GMV $916m, Digital Platform GMV $790m으로 각각 50%, 60% 성장
- Q2 2021 demand generation expense가 Digital Platform Services Revenue의
  19.9%에서 18.9%로 낮아짐
- Q2 2021 기술비 비중도 9.5%에서 7.9%로 낮아짐
- Alibaba·Richemont가 Farfetch와 중국 JV에 대규모 자본 투입
- 2021년까지 active consumer와 브랜드·판매자 네트워크 확대

즉 초기 operating leverage 신호와 전략적 파트너의 검증이 실제로 있었다. 오류는
이 신호가 장기 30% 전사 EBITDA와 안전한 주주가치를 거의 확정한다고 본 데 있다.

## 8. 실제로 무슨 일이 일어났나

### ① GMV 성장률이 빠르게 꺾였다

2021년 GMV는 $4.2bn으로 33% 성장했지만 2022년에는 약 $4.1bn으로 감소했다.
러시아 영업중단, 중국 봉쇄, 환율과 소비둔화가 영향을 줬다. 2023년 Q2 전체 GMV는
1.2% 성장에 그쳤고 Marketplace AOV는 $596에서 $561로 낮아졌다. markdown
비중 증가와 미국 Digital Platform GMV 감소가 나타났다.

이는 산업의 온라인화가 계속돼도 특정 플랫폼의 점유율이 자동으로 상승하지는
않는다는 것을 보여준다.

### ② Marketplace의 양호한 공헌이익이 전사 FCF로 연결되지 않았다

2021년 adjusted EBITDA margin은 0.1%였다. 2022년 Q4에는 -6.3%, 2023년 Q2에는
-6.4%였다. Q2 2023 Digital Platform gross margin은 49.3%였지만 전사 SG&A는
$456.4m, adjusted EBITDA는 -$30.6m이었다.

`거래 한 건에서 남는 이익`과 `연결기업이 자본제공자에게 남기는 현금` 사이에는
다음 bridge가 빠져 있었다.

> Digital Platform gross profit
> − demand generation
> − technology expense와 자본화 개발비
> − G&A·주식보상
> − 감가상각·인수무형자산 상각
> − Brand Platform·직영점 손실과 재고
> − 이자·운전자본·capex
> = 기존 주주에게 남는 FCF

30% EBITDA는 다른 인터넷 플랫폼의 성숙기 마진을 Farfetch의 연결 사업범위에
적용한 값에 가까웠다.

### ③ “asset-light marketplace”와 “Farfetch Limited”를 혼동했다

제3자 Marketplace만 보면 판매자가 재고를 보유한다. 그러나 Farfetch Limited에는
New Guards, Browns, Stadium Goods, 점포, 라이선스, 자체재고와 기술투자가 있었다.

2023년 Q2 Brand Platform GMV는 40.8%, 매출은 42.2% 감소했다. Browns 재고를
처분하기 위한 first-party 비중과 markdown 확대는 Digital Platform gross margin도
낮췄다. 좋은 marketplace unit economics가 연결기업 전체를 asset-light
compounder로 만들지 못했다.

### ④ 전략적 계약을 확정된 경제가치로 보기 어려웠다

2022년 발표된 Richemont·YNAP 거래는 2021년 롱의 플랫폼 논지를 강하게 확인해
주는 것처럼 보였다. 대부분 Richemont Maisons가 FPS를 채택하고 다수 브랜드가
e-concession을 열며, Farfetch가 YNAP 47.5%를 인수할 계획이었다.

그러나 이 계약은 규제승인, 거래종결, 기술이전과 실제 onboarding이라는 여러 단계를
거쳐야 했다. 2023년 12월 계약이 종료될 때까지 Richemont Maisons와 YNAP는 FPS를
도입하지 않았고 e-concession도 열지 않았다.

> **계약 발표 → backlog → onboarding → 거래발생 → 매출 → EBITDA → FCF**

각 단계에는 별도의 확률과 시간이 필요하다. Farfetch는 마지막 단계에 도달하기 전에
유동성이 먼저 악화됐다.

### ⑤ 유동성과 자본구조가 terminal value보다 먼저 문제됐다

2023년 6월 말 현금은 $453.8m이었고 6개월 동안 $287.2m 감소했다. borrowings는
약 $916.9m이었다. 회사는 $200m delayed-draw term loan을 높은 discount 조건으로
추가 확보했다.

장기적으로 $3bn EBITDA가 가능하더라도 그 상태에 도달하기 전에 현금이 바닥나면
equity에는 가치가 남지 않는다. 전환사채도 주가가 전환가격보다 크게 낮아지면
희석주식이 아니라 상환·협상해야 하는 채권자 청구권이 된다.

### ⑥ 결국 사업가치와 주주가치가 분리됐다

2023년 12월 19일 NYSE는 FTCH 거래를 즉시 정지했다. 회사는 자산매각 후 보통주와
전환사채에 가치가 남지 않을 것으로 예상했다.

2024년 1월 Coupang·Greenoaks 컨소시엄은 Farfetch의 **사업과 자산**을 인수했다.
인수구조에는 기존 term loan $633m 인수, closing 시 추가 현금 $150m, 이미 제공된
$150m bridge loan의 출자전환, 이후 최대 $200m 추가자금 의무가 포함됐다.

이는 Farfetch의 고객·브랜드·기술자산이 쓸모없어서 0이 된 것이 아니라, 그 자산가치가
채권자·신규자금 제공자에게 귀속되고 기존 Farfetch Limited 주주에게는 남지 않았다는
뜻이다.

## 9. 2021년 롱에서 맞은 것과 틀린 것

| 원래 주장 | 판정 | 구체적 이유 |
|---|---:|---|
| 명품 온라인화는 장기 구조적 추세 | 대체로 맞음 | 온라인 채널과 Farfetch 사업자산은 인수 후에도 존속 |
| SKU 폭·e-concession은 브랜드와 소비자에게 가치 | 맞는 부분 있음 | 대형 전략투자와 Richemont 계약 추진이 제품가치를 확인 |
| Farfetch 온라인 점유율이 5~7년 내 두 배 | 틀림 | GMV가 2021년 $4.2bn에서 2022년 $4.1bn으로 감소 |
| GMV $15~20bn | 틀림 | 독립 상장사로서 목표기간을 완주하지 못하고 2023년 구조조정 |
| Alibaba JV가 중국 성장을 가속 | 대체로 틀림 | 접근권은 얻었지만 중국 봉쇄·수요둔화를 상쇄하지 못함 |
| 고정비 규모화로 EBITDA margin 30% | 완전히 틀림 | 2021년 0.1%, Q2 2023 -6.4% |
| Farfetch는 asset-light | Marketplace만 맞음 | 연결기업에는 브랜드·리테일·재고·M&A·기술투자가 포함 |
| $16.5bn에서 10년 시장수익률 상회 | 완전히 틀림 | 약 29개월 뒤 거래정지 및 보통주 잔존가치 없음 예상 |

## 10. 2021년 롱의 최종 판정

**치명적 실패**다. 명품 온라인화와 플랫폼 자산의 효용은 맞았지만, 투자자가 산 것은
“Farfetch 기술”이 아니라 **Farfetch Limited 보통주**였다. GMV 목표, 점유율 상승,
30% EBITDA margin, 장기 복리수익이라는 핵심 투자주장은 모두 실현되지 않았다.

가장 큰 오류는 다섯 가지다.

1. **산업성장과 기업점유율을 중복 외삽**했다.
2. **SKU 폭을 강한 네트워크 효과와 winner-take-most로 바로 해석**했다.
3. **Marketplace 단위경제성을 연결기업 EBITDA·FCF로 외삽**했다.
4. **New Guards·Browns·Stadium Goods·M&A와 재고를 asset-light 서사에서 제외**했다.
5. **terminal economics까지 버틸 현금·부채·희석·시간을 모델링하지 않았다.**

> **학습점:** 좋은 산업, 좋은 제품, 가치 있는 자산이 결합돼도 좋은 주식이 아닐 수
> 있다. 상장주식 분석의 마지막 질문은 “사업에 가치가 있는가”가 아니라
> “그 가치가 모든 선순위 청구권과 추가자금 필요를 지난 뒤 기존 주주에게 얼마나
> 남는가”여야 한다.

---

## 11. 성과 원인 분해

| 요인 | 원문 예상 여부 | 실제 영향 | 중요도 |
|---|---:|---|---:|
| 명품 온라인 성장 | 2021 Long 예상 | 사업자산 가치 유지에는 기여했으나 equity를 구하지 못함 | 중간 |
| e-concession·브랜드 네트워크 | 2021 Long 예상 | 전략투자·계약 추진을 이끌었으나 수익성 전환은 실패 | 중간 |
| 전사 고정비·마케팅비 | 2019 Short 예상 | 기록적 GMV에도 낮은 EBITDA를 만든 핵심 | 큼 |
| New Guards 등 M&A | 두 글 모두 충분히 예상 못함 | 자본집약도·복잡성·재고·통합비용 확대 | 매우 큼 |
| Richemont·YNAP 계약 | 두 글 게시 후 등장 | 플랫폼 가능성을 확인했지만 미실행 후 유동성 위기 촉발 | 큼 |
| 부채·현금소모 | 원문에서 불충분 | 계약이 경제가치로 전환되기 전에 기존 equity 소진 | 결정적 |
| 2019 게시 당일 실적·NGG 발표 | Short의 약세 촉매와 일부 일치 | 다음 날 44% 급락 | 매우 큼 |

## 12. 패턴 분석용 태그

### 2019 Short

- `thesis.overvaluation_short`
- `success.earnings`
- `failure.timing`
- `outcome.price_right_thesis_wrong`
- 보조 패턴: `right_terminal_wrong_path`, `unmodeled_capital_allocation`

### 2021 Long

- `thesis.platform_network`
- `thesis.quality_compounder`
- `failure.unit_to_fcf`
- `failure.balance_sheet`
- `failure.capital_allocation`
- `failure.catalyst`
- `failure.timing`
- 보조 패턴: `valuable_asset_zero_equity`, `industry_right_company_wrong`

## 주요 근거

- [Farfetch 2019 Form 20-F](https://www.sec.gov/Archives/edgar/data/1740915/000156459020009887/ftch-20f_20191231.htm)
- [New Guards 실제 인수대가 관련 SEC 자료](https://www.sec.gov/Archives/edgar/data/1740915/000119312520120146/d919492dex992.htm)
- [Farfetch FY2019 results](https://www.nasdaq.com/press-release/farfetch-announces-fourth-quarter-and-full-year-2019-results-2020-02-27)
- [Alibaba·Richemont·Farfetch 파트너십](https://www.sec.gov/Archives/edgar/data/1740915/000156459020051372/ftch-ex991_7.htm)
- [Farfetch Q1 2021 results](https://www.businesswire.com/news/home/20210513005816/en/Farfetch-Announces-First-Quarter-2021-Results)
- [Farfetch Q2 2021 results](https://www.businesswire.com/news/home/20210819005630/en/Farfetch-Announces-Second-Quarter-2021-Results)
- [Farfetch 2021 Form 20-F](https://www.sec.gov/Archives/edgar/data/1740915/000156459022008640/ftch-20f_20211231.htm)
- [Farfetch FY2021 results](https://www.businesswire.com/news/home/20220224005894/en/Farfetch-Announces-Fourth-Quarter-and-Full-Year-2021-Results)
- [Richemont·YNAP 거래구조와 FPS 계획](https://www.sec.gov/Archives/edgar/data/1740915/000119312522228027/d390762dex991.htm)
- [Farfetch FY2022 results](https://www.sec.gov/Archives/edgar/data/1740915/000119312523046569/d474360dex991.htm)
- [Farfetch Q2 2023 results](https://www.sec.gov/Archives/edgar/data/1740915/000095017023043201/ftch-ex99_1.htm)
- [Richemont의 계약 종료 발표](https://www.richemont.com/news-media/press-releases-news/richemont-farfetch-and-symphony-global-terminate-agreements/)
- [NYSE 거래정지·잔존가치 공시](https://www.sec.gov/Archives/edgar/data/1740915/000119312523298824/d534467dex991.htm)
- [Coupang 2023 Form 10-K — Farfetch 자산인수](https://www.sec.gov/Archives/edgar/data/1834584/000183458424000023/cpng-20231231.htm)
- [Farfetch 주가 이력](https://companiesmarketcap.com/farfetch/stock-price-history/)
