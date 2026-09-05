# EMMIS COMMUNICATIONS CP-CL A (EMMS) — 2005-12-30 VIC Long

**idea_id:** `56eb0e52-b78e-4a38-94c6-20d3fb879b14`  
**원 SQL 방향:** Short  
**원문 검증 방향:** **Long**  
**분석 security:** EMMS Class A common equity  
**종합 판정:** **이벤트 논지 부분 성공, 장기 복리 실패**

## 1. 결론부터

raw SQL은 Short지만 원문은 TV 자산 매각, debt paydown, 대규모 Dutch tender 뒤 남는 radio stub을 싸게 사는 명백한 Long이다. **asset-sale/tender event 자체는 상당히 정확히 맞았지만, 남은 radio business가 5~10% FCF/share compounder가 될 것이라는 장기 가정은 실패**했다.

## 2. 원 투자논지

회사는 20.2m주, 당시 shares outstanding의 약 36%를 $19.50에 tender했고 이를 TV 자산매각으로 조달했다. 작성자는 TV sale을 약 $1.3bn pretax, $1.1~1.2bn after-tax로 예상하면서 post-sale debt가 크게 줄고, remaining company가 약 12x pro forma FCF 또는 부진한 Chicago stations를 제외하면 8~9x FCF에 불과하다고 봤다. 이후 debt paydown·buyback을 통해 FCF/share가 연 5~10% 성장한다는 구조였다.

## 3. 사업과 돈의 흐름

Emmis는 major-market radio, 16개 TV station, magazines를 가진 levered media conglomerate였다. 투자 논지는 저수익/비핵심 TV를 현금화해 debt와 share count를 동시에 줄이면 radio cash flow의 per-share 가치가 커진다는 전형적인 **asset monetization + capital allocation** thesis였다.

## 4. 핵심 가정

TV assets가 예상가격에 팔리고 proceeds가 debt reduction에 실제 사용되어야 했다. tender 뒤 남는 radio assets의 EBITDA와 FCF가 안정적이어야 했으며, New York·LA·Chicago 대도시 spectrum scarcity가 secular listener decline보다 오래 지속되어야 했다.

## 5. 실제 전개

회사는 실제로 20.25m주를 $19.50, 총 약 $394.9m에 tender했다. 2005~2008년 TV 16개 station을 모두 팔았고 gross proceeds는 약 $1.24bn이었다. 즉 핵심 corporate actions는 원 thesis와 매우 가까웠다. 그러나 이후 radio의 구조적 압력, 반복적인 preferred/governance 이슈와 자본구조 변동으로 안정적 compounding이 나오지 않았고, Emmis는 2020년 Nasdaq에서 자진 상장폐지했다.

## 6. 주장별 검증

**TV sale:** 성공. 16개 station 전부 매각, gross proceeds 약 $1.24bn.  
**대규모 tender:** 성공. $19.50에 20.25m주를 실제 매입.  
**deleveraging으로 residual equity 질 개선:** 부분 성공. asset monetization은 진행됐지만 장기 사업질과 governance discount가 남았다.  
**5~10% FCF/share compounder:** 실패. 향후 구조는 안정적 radio compounder보다 지속적인 asset/capital-structure event에 가까웠다.

## 7. 핵심 수치

| 지표 | 값 | 의미 |
|---|---:|---|
| Tender shares | 20.25m | 큰 share-count 축소 |
| Tender price | $19.50 | 실제 repurchase price |
| Tender cash | 약 $394.9m | TV sale proceeds 활용 |
| TV gross sale proceeds | 약 $1.24bn | 16개 station 전체 |

## 8. 촉매와 타임라인

- **2005-05** — Dutch tender 승인.
- **2005** — 20.25m주를 $19.50에 tender 완료.
- **2005-12-30** — VIC Long 게시.
- **2005~2008** — TV portfolio 순차 매각.
- **2008-07-18** — 마지막 TV station sale 완료, 누적 gross proceeds 약 $1.24bn.
- **2020-05-13** — Nasdaq 마지막 거래일.

## 9. 반증조건

TV 매각가격이 예상보다 크게 낮거나 proceeds가 debt/share reduction이 아닌 새 risky M&A로 재투자되고, radio FCF가 지속적으로 감소한다면 thesis가 깨진다. 실제 장기 결과는 두 번째 단계, 즉 residual business의 quality를 충분히 보수적으로 보지 못한 데 있었다.

## 10. 재사용 가능한 교훈

**이벤트 수익과 stub 수익을 분리하라.** 자산매각과 tender가 성공해도 남은 사업이 좋은 compounder가 된다는 보장은 없다. event-driven SOTP에서는 `sale price → tax → debt waterfall → share count → residual normalized FCF`를 계산한 뒤, residual business에는 별도의 duration multiple을 적용해야 한다.

### Sources

- [VIC 2005 Emmis Long](https://www.valueinvestorsclub.com/idea/Emmis_Communications/7932687054)
- Emmis Dutch tender SEC/company filing
- Emmis TV divestiture completion SEC filing
- [Emmis MediaCo transaction](https://www.sec.gov/Archives/edgar/data/783005/000156459019024775/emms-10q_20191130.htm)
- [MediaCo separation filing](https://www.sec.gov/Archives/edgar/data/1784254/000104746919006201/a2240029zex-99_1.htm)
- [Emmis 2020 Form 10-K](https://www.sec.gov/Archives/edgar/data/783005/000156459020025335/emms-10k_20200229.htm)
