# TOWNSQUARE MEDIA INC  (TSQ) — 2022-03-14 VIC Long

**idea_id:** `2eec41d0-f8d6-47ba-822f-c361725a37ee`  
**원 SQL 방향:** Short  
**원문 검증 방향:** **Long**  
**분석 security:** TSQ common equity  
**종합 판정:** **혼합 / 구조적 논지 성공, 목표수익 실패**

## 1. 결론부터

“라디오로 보이는 회사 안의 디지털 회사”라는 핵심 진단은 맞았지만 2.9x/46% IRR이라는 시간·가격 경로를 과도하게 압축했다. 사업 변환이 맞더라도 고레버리지 소형주의 rerating은 EBITDA와 FCF의 절대성장, 금리, refinancing 조건에 의해 늦어질 수 있다.

이 아이디어는 단순히 이후 주가가 올랐는지 내렸는지를 보는 사례가 아니다. 원문이 무엇을 **가격에 잘못 반영된 변수**로 보았는지, 그 변수가 실제 영업·자본구조에서 어떻게 전개됐는지, 그리고 common equity까지 가치가 전달됐는지를 분리해서 평가했다. raw SQL의 `is_short`는 수정하지 않고 research layer에서만 실제 방향을 교정했다.

## 2. 원 투자논지

약 24% forward FCF yield에서 디지털 사업이 곧 매출·현금흐름의 과반이 되고, 디레버리징·2023년 리파이낸싱·$50m 자사주가 주당가치를 끌어올려 2024년 말 2.9x/46% IRR이 가능하다는 Long.

원문을 재구성할 때 valuation 숫자만 떼지 않고, 작성자가 기대한 **인과사슬**을 기준으로 읽었다. 즉 `사업/자산의 경제성 → 현금흐름 또는 asset value → 부채·preferred·deal condition → common equity 가치 → 촉매와 시간` 순서다.

## 3. 사업과 돈의 흐름

Townsquare는 중소도시 라디오를 고객접점과 현금창출 기반으로 쓰면서 Townsquare Ignite의 programmatic digital advertising과 Townsquare Interactive의 SMB subscription marketing을 판매한다. 핵심은 radio 자체의 성장보다 기존 지역 영업조직·퍼스트파티 데이터·광고주 관계를 디지털 상품으로 재활용하는 데 있다.

이 산업에서 회계상 EBITDA와 주주가치가 크게 벌어질 수 있는 이유는 고정비, 광고 경기민감도, secular audience migration, 높은 leverage가 동시에 존재하기 때문이다. 그래서 headline revenue보다 **organic ad trend, normalized EBITDA, debt service, asset-sale proceeds의 waterfall**을 우선해서 봤다.

## 4. 핵심 가정

디지털이 radio 감소를 상쇄할 정도로 빠르게 성장하고, 높은 margin을 유지하며, FCF가 부채감축과 자사주로 연결되어야 했다. 특히 2024년까지의 rerating 속도는 디지털 성장과 자본구조 개선이 동시에 진행된다는 가정에 민감했다.

이 가정들 가운데 어느 하나가 깨졌을 때 다른 가정이 자동으로 보완해 주는지 여부가 중요하다. 특히 radio/media에서는 scale이 커져도 산업 revenue pool이 줄면 fixed-cost synergy가 debt burden을 이기지 못할 수 있고, SOTP 자산가치가 맞아도 minority common에 현금이 늦게 도달할 수 있다.

## 5. 실제 전개

2022년 digital revenue는 $231m(+16%)로 총매출과 adjusted operating income의 50%가 됐고 net leverage는 4.29x까지 낮아졌다. 하지만 회사가 제시한 2024 digital revenue $275m 목표와 달리 2024 digital revenue는 약 $234m에 그쳤다. 그럼에도 2025 digital은 총매출 55%, 2026년 상반기 57%로 구조적 mix shift 자체는 지속됐다. VIC SQL 가격비율은 1개월 1.061x, 3개월 0.780x, 6개월 0.751x로 초기 주가경로는 목표와 반대였다.

사후검증은 가능한 한 회사 SEC filing·공식 IR·거래공시를 우선했다. 정확한 historical stock-return series가 원 SQL에 없는 아이디어는 임의의 가격수익률을 만들어내지 않고, **논지의 영업·자본구조 결과와 확정 corporate event**를 중심으로 판정했다.

## 6. 주장별 검증

“라디오로 보이는 회사 안의 디지털 회사”라는 핵심 진단은 맞았지만 2.9x/46% IRR이라는 시간·가격 경로를 과도하게 압축했다. 사업 변환이 맞더라도 고레버리지 소형주의 rerating은 EBITDA와 FCF의 절대성장, 금리, refinancing 조건에 의해 늦어질 수 있다.

따라서 판정은 “회사가 살아남았는가”나 “매출이 늘었는가”만으로 하지 않았다. 원문이 기대한 catalyst가 실제로 일어났는지, 그 뒤 incremental economics가 common equity에 귀속됐는지, 그리고 예상한 기간 안에 발생했는지를 따로 나눴다.

## 7. 핵심 수치

| 지표 | 값 | 단위 | 근거 |
|---|---:|---|---|
| Forward FCF yield | 24 | % | original VIC |
| 2022 digital revenue | 231 | USD m | primary |
| 2024 digital revenue | 234 | USD m | primary |
| 6-month raw price ratio | 0.7513321492 | x | raw SQL |

수치는 서로 같은 성격이 아니다. 원문 valuation/target은 **당시 투자자가 underwrite한 변수**, SEC/IR 수치는 **사후 관측값**이다. 두 종류를 섞어 hindsight target으로 만들지 않았다.

## 8. 촉매와 타임라인

- **2022-03-14** — VIC Long 게시: 24% FCF yield, 2024년 말 2.9x 목표
- **2022-12-31** — Digital 50% 도달: $231m digital revenue
- **2023-03-09** — 2022 결과 발표: net leverage 4.29x
- **2024-12-31** — 2024 digital 확인: 약 $234m, $275m 목표 미달
- **2025-12-31** — Digital 55%: 총매출의 과반 구조 고착
- **2026-06-30** — Digital 57%: 상반기 매출 mix 지속

이 타임라인은 원 VIC가 기대한 시간축과 실제 corporate-event 시간축의 차이를 보여준다. 좋은 SOTP나 구조적 transformation도 realization이 수년 늦어지면 IRR은 크게 달라진다.

## 9. 반증조건

digital revenue/profit 비중이 늘지 않거나 Interactive/ Ignite의 organic growth가 둔화하고, leverage가 4x대에서 내려오지 않으며 자사주가 부채비용보다 낮은 수익을 낸다면 thesis는 깨진다.

향후 유사 아이디어에서는 이 조건을 사전에 KPI로 저장해두고, 단순 가격하락을 thesis break로 오인하지 않되 실제 business/capital-structure falsification은 즉시 반영해야 한다.

## 10. 재사용 가능한 교훈

숨은 성장사업을 찾을 때는 “비중 증가”와 “절대 성장”을 분리해야 한다. mix가 좋아져도 전체 EBITDA가 정체되면 equity rerating은 예상보다 오래 걸린다.

### 연구 메모

- raw SQL의 `is_short=true`는 원천 데이터 보존을 위해 그대로 둔다.
- research direction은 원 VIC description의 명시적 추천 security와 payoff 구조를 기준으로 판정했다.
- ETM 2020처럼 hedge가 함께 언급된 경우에도 **primary recommendation**과 hedge를 구분했다.
- 사후 결과는 primary source를 우선하고, 원 SQL에 없는 historical return은 추정해 채우지 않았다.

### Sources

- [VIC 2022 TSQ Long](https://www.valueinvestorsclub.com/idea/TOWNSQUARE_MEDIA_INC/5454442109) — original
- [Townsquare FY2022 results](https://www.sec.gov/Archives/edgar/data/1499832/000149983223000027/a123122pressrelease.htm) — primary
- [Townsquare 2024 10-K](https://www.sec.gov/Archives/edgar/data/1499832/000149983225000040/tsq-20241231.htm) — primary
- [Townsquare FY2024 results](https://www.sec.gov/Archives/edgar/data/1499832/000149983225000038/a123124pressrelease.htm) — primary
- [Townsquare FY2025 results](https://www.sec.gov/Archives/edgar/data/1499832/000149983226000019/a123125pressrelease.htm) — primary
- [Townsquare Q2 2026 results](https://www.sec.gov/Archives/edgar/data/1499832/000149983226000044/a63026pressrelease.htm) — primary
