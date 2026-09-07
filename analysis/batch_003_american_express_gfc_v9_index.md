# Batch 003 — American Express GFC V9 Index

> 기존 `analysis/batch_003_american_express_gfc.md`는 archive/reference로 유지한다.  
> V9에서는 **동일 회사라도 투자시점이 다르면 별도 아이디어 파일**로 관리한다.

## Canonical idea files

| VIC 게시일 | 방향 | 파일 | 핵심 판정 |
|---|---|---|---|
| 2007-04-01 | Long | [2007 AXP Long](ideas/2007/2007-04-01_AXP_long.md) | closed-loop moat는 맞았지만 credit/funding leverage를 놓쳐 실패 |
| 2008-06-12 | Long | [2008 June AXP Long](ideas/2008/2008-06-12_AXP_long.md) | 장기 franchise는 맞았지만 survival margin과 timing이 부족 |
| 2008-12-31 | Long | [2008 December AXP Long](ideas/2008/2008-12-31_AXP_long.md) | BHC·정부자본·예금으로 survival probability가 개선된 뒤 산 distressed quality Long, 매우 성공 |

## 세 아이디어를 함께 볼 때의 핵심

AXP의 franchise quality는 세 시점 모두 크게 바뀌지 않았다.

달라진 것은:

**Credit loss trajectory  
× Funding access  
× Capital buffer  
× Survival probability  
× Entry valuation**

이었다.

### 2007
- 높은 ROE와 moat에 집중
- market cap를 loss-absorbing capital처럼 해석
- buyback leverage를 긍정
- 결과: 2년 -75.6%

### 2008-06
- 위험을 더 많이 인식
- GNS/network SOTP와 정상화 가치를 계산
- 그러나 correlated stress를 equity waterfall에 반영하지 못함
- 결과: 6개월 -47.9%, 3년 +8.4%

### 2008-12
- 가격이 더 낮아짐
- BHC 전환
- Treasury capital
- deposit funding 확대
- 생존 bridge가 확인됨
- 결과: 1년 +109.6%, 5년 +382.8%

## Batch 003에서 추출되는 재사용 가능한 교훈

1. **금융사의 높은 ROE는 moat와 leverage/benign credit를 분리해야 한다.**
2. **시가총액은 손실흡수자본이 아니다.**
3. **낮은 P/E보다 stress-normalized EPS와 funding coverage가 먼저다.**
4. **위험을 나열하는 것과 확률가중 stress valuation을 하는 것은 다르다.**
5. **SOTP의 고ROIC segment가 legal/capital ring-fenced인지 확인해야 한다.**
6. **Distressed financial은 business bottom보다 survival bridge 확인이 먼저 투자기회가 될 수 있다.**
7. **같은 franchise라도 survival probability와 entry price가 달라지면 기대수익은 완전히 달라진다.**

## 추가 보강 항목

- 세 아이디어의 정확한 일별 MFE / MAE
- dividend-adjusted total return
- 각 시점의 funding maturity ladder
- securitization/CP spread와 deposit cost
- 당시 consensus EPS 추정치의 월별 하향 경로
- 2008-12 Treasury preferred/warrant의 정확한 희석·상환 효과
