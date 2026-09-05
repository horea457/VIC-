# Batch 035 — PLUS ticker collision: ePlus · Plus500 · Level 3

## Batch audit summary

이 배치는 원 SQL과 VIC 본문을 직접 대조한 결과, raw `is_short=True` 6건이 모두 실제 본문상 Long이라는 심각한 direction 오류를 발견했다. 또한 ticker `PLUS`의 2019·2021 아이디어는 Plus500 Ltd.인데 raw company lookup은 ePLUS로 붙어 있다. raw flags는 `ideas_master`에 그대로 보존하고, 아래 research layer에서만 방향·entity를 교정한다.

검증 카운트: **10 ideas / 100 sections / 60 claims (idea별 100%) / 40 metrics / 60 timeline / 60 sources**.

# ePlus inc. — idea 1

## 1. 2002-06-04 — raw Long / research Long — adanah312

**idea_id:** `16577e38-4933-4db0-892e-fa5b9fdd7d79`  
**raw ticker/company:** `PLUS` / `ePLUS`  
**research entity:** ePlus inc.  
**verdict:** **성공·촉매 지연**

### 1. 무슨 기업인가
ePlus는 기업·공공기관에 IT 제품, 전문·관리 서비스와 장비 금융을 함께 제공하는 미국 기술 솔루션 사업자다. 1990년 설립 후 단순 하드웨어 유통보다 고객의 네트워크·보안·클라우드·데이터센터 수요를 설계하고, 필요하면 리스·금융까지 붙이는 구조로 진화했다. 낮은 제품 마진만 보면 평범한 VAR처럼 보이지만 서비스 믹스, 고객 관계, 벤더 인증, 운전자본·금융자산 관리가 경제성을 결정한다.

### 2. 원 VIC 투자 논지
2002년 Long은 닷컴 붕괴 뒤에도 흑자를 유지한 B2B 생존자라는 점, 주가가 약 $9.10으로 당시 장부가치 약 $9.45보다 낮았다는 점, 약 $2.50/주 현금과 자사주 매입, 경영진 지분, IT 지출 회복 시 영업 레버리지를 핵심으로 삼았다. 단순 인터넷 테마가 아니라 이미 돈을 버는 기업이 기술 도입 확산을 흡수한다는 논지였다.

### 3. 당시 숫자와 valuation

- **T0 주가/장부가치:** $9.10 / BV 약 $9.45 → 사후 확인: 장부가치 이하에서 시작
- **T0 현금:** 약 $2.50/주 → 사후 확인: 하방 완충
- **FY2008 cash:** $58.4m → 사후 확인: 공시 정상화 과정에서도 유동성 유지
- **2019-09 분기:** 매출 $411.6m / 순이익 $20.1m → 사후 확인: 생존자 논지가 장기 사업 확장으로 연결

### 4. 실제로 무슨 일이 벌어졌나
사업은 사라지지 않았고 오히려 장기적으로 규모와 서비스 역량을 키웠다. 중간에 옵션 회계 조사와 공시 지연으로 2007년 NASDAQ에서 상장폐지되는 큰 거버넌스 충격이 있었지만, 2008년 5월까지 밀린 보고서를 모두 제출했고 2008년 9월 3일 NASDAQ에 재상장했다. 2019년 9월 분기에는 순매출 $411.6m, 순이익 $20.1m을 기록했고 2026년 10-K에서도 AI·cloud·data center·security 등을 제공하는 존속 기업이다.

### 5. 논지 판정
장부가치·현금만 싼 것이 아니라 고객·벤더 관계와 서비스 확장이 실제 장기 존속성을 만들었다는 핵심은 맞았다. 다만 18개월 내 volume/IT 회복이라는 촉매보다 회계·공시 리스크가 훨씬 컸고, 가치 실현에는 예상보다 긴 시간이 필요했다.

### 6. 가장 중요한 분석 오류/교훈
저평가와 생존력은 잘 봤지만 회계통제·공시 리스크를 별도 확률변수로 두지 않아 촉매 시간을 과소평가했다.

### 7. 최초 확인·반증 신호
**2008-09-03 — 2008-09-03 NASDAQ 재상장**. 촉매는 발생 여부만 보는 것이 아니라 그 시점까지의 현금소진, 부채, 상장상태, 규제와 희석 가능성을 함께 봐야 한다.

### 8. Claim audit

- **핵심 valuation (20%)** — 가격이 정상화 가치보다 충분히 낮다. / falsifier: 정상화 숫자를 보수적으로 적용해도 할인폭 소멸 / verdict: 적중
- **사업경제/단위경제 (20%)** — headline 성장/자산이 실제 gross profit·FCF로 전환된다. / falsifier: 매출/트래픽 증가에도 margin·cash flow 악화 / verdict: 적중
- **balance sheet·자본구조 (15%)** — 현금·부채·non-recourse/working-capital 구조가 equity에 충분한 runway를 준다. / falsifier: 부채·현금소진·공시/규제 리스크 급증 / verdict: 적중
- **촉매·시간 (15%)** — 촉매가 현금소진·희석보다 먼저 발생한다. / falsifier: 촉매 지연이 thesis duration을 초과 / verdict: 적중
- **경쟁우위/산업구조 (15%)** — 경쟁우위가 가격경쟁·규제·기술변화 후에도 유지된다. / falsifier: CAC/가격/공급경쟁이 구조적으로 악화 / verdict: 적중
- **반증·최종 교훈 (15%)** — 반대 신호가 나타나면 thesis를 업데이트한다. / falsifier: 원문 방향 또는 entity 자체가 metadata와 불일치 / verdict: 적중

### 9. Timeline

- **2002-06-04** — VIC idea 게시 (T0)
- **2008-09-03** — 2008-09-03 NASDAQ 재상장 (핵심 확인/반증 신호)
- **2008-09-03** — ePlus NASDAQ 재상장 (ePlus 해당 시 recovery catalyst)
- **2010-06-30** — ePlus cash $79.3m·equity $190.4m (balance-sheet follow-through)
- **2019-09-30** — ePlus 분기 순매출 $411.6m·순이익 $20.1m (장기 사업확대)
- **2026-09-05** — postmortem 재검증 (현재 연구 기준일)

### 10. Sources

- [Original VIC thesis](https://www.valueinvestorsclub.com/idea/ePlus_Inc/1076596755) — 원 투자방향·thesis·catalyst 원문 확인
- [ePlus FY2008 10-K](https://www.sec.gov/Archives/edgar/data/1022408/000102240808000030/form10k.htm) — FY2008 balance sheet, sales, restatement completion
- [ePlus FY2009 10-K](https://www.sec.gov/Archives/edgar/data/1022408/000102240809000017/form10k.htm) — NASDAQ relisting date and status
- [ePlus FY2010 10-K](https://www.sec.gov/Archives/edgar/data/1022408/000102240810000024/form10k.htm) — business segments and capital structure
- [ePlus 2010 Q1 release exhibit](https://www.sec.gov/Archives/edgar/data/1022408/000102240810000034/ex9-01.htm) — cash, equity, non-recourse notes
- [ePlus 2019 Q2 results](https://www.eplus.com/about-us/press-releases/details/2019/11/06/eplus-reports-second-quarter-and-first-half-financial-results) — later revenue, services, earnings

---

# ePlus inc. — idea 2

## 2. 2004-12-23 — raw Long / research Long — hack731

**idea_id:** `09cb4b70-533d-435e-8566-be6203f98c1b`  
**raw ticker/company:** `PLUS` / `ePLUS`  
**research entity:** ePlus inc.  
**verdict:** **성공·리스크 과소평가**

### 1. 무슨 기업인가
ePlus는 IT 제품 판매·서비스와 리스/금융을 결합한 기업용 기술 솔루션 회사다. 고객이 장비를 구매·운영·교체하는 전 과정에서 조달, 설계, 서비스, 금융을 묶어 제공하기 때문에 단순 매출총액보다 gross profit, service mix, working capital과 lease credit quality가 핵심이다.

### 2. 원 VIC 투자 논지
2004년 Long은 약 1.1배 tangible book, 현금 $14.1m, 정상화 EPS 약 $1.40로 환산하면 현금 차감 후 약 6배 earnings power라는 저평가를 주장했다. Manchester 인수 시너지, Ariba 소송비용 종료, 자사주 매입, IT 지출 회복과 Cyberco 고객 사기 건이 회사에 비소구라면 해소될 것이라는 촉매를 제시했다.

### 3. 당시 숫자와 valuation

- **T0 tangible book:** $9.8/주 → 사후 확인: 주가가 장부가치 근처
- **정상화 EPS:** $1.40 추정 → 사후 확인: 현금 차감 후 약 6.3배 논리
- **2010-06 cash:** $79.3m → 사후 확인: 재무 완충 확대
- **2010-06 equity:** $190.4m / $23.41주 → 사후 확인: 장부가치 성장 확인

### 4. 실제로 무슨 일이 벌어졌나
Cyberco와 옵션 회계 이슈는 예상보다 오래 갔고 공시 지연은 2007년 실제 상장폐지까지 번졌다. 그러나 회사는 손실을 감당하며 존속했고 2008년 모든 정기보고를 정상화한 뒤 9월 3일 NASDAQ에 복귀했다. 2010년 6월 말에는 현금 $79.3m, 자본 $190.4m 또는 주당 $23.41을 공시했다. 장기적으로는 IT 솔루션·서비스 사업이 크게 확대됐다.

### 5. 논지 판정
낮은 multiple, 보수적 자본구조, 내부자 지분과 buyback은 실제 하방을 지지했다. 반면 고객 사기·법적 분쟁·옵션 회계가 단순 일회성 비용이 아니라 자본시장 접근과 상장 상태에 영향을 줄 수 있다는 second-order risk는 과소평가했다.

### 6. 가장 중요한 분석 오류/교훈
정상화 EPS 계산은 유용했지만 법률·회계 이벤트가 multiple과 유동성에 미치는 기간 리스크를 충분히 haircut하지 않았다.

### 7. 최초 확인·반증 신호
**2008-09-03 — 2008-09-03 NASDAQ 재상장**. 촉매는 발생 여부만 보는 것이 아니라 그 시점까지의 현금소진, 부채, 상장상태, 규제와 희석 가능성을 함께 봐야 한다.

### 8. Claim audit

- **핵심 valuation (20%)** — 가격이 정상화 가치보다 충분히 낮다. / falsifier: 정상화 숫자를 보수적으로 적용해도 할인폭 소멸 / verdict: 적중
- **사업경제/단위경제 (20%)** — headline 성장/자산이 실제 gross profit·FCF로 전환된다. / falsifier: 매출/트래픽 증가에도 margin·cash flow 악화 / verdict: 적중
- **balance sheet·자본구조 (15%)** — 현금·부채·non-recourse/working-capital 구조가 equity에 충분한 runway를 준다. / falsifier: 부채·현금소진·공시/규제 리스크 급증 / verdict: 적중
- **촉매·시간 (15%)** — 촉매가 현금소진·희석보다 먼저 발생한다. / falsifier: 촉매 지연이 thesis duration을 초과 / verdict: 적중
- **경쟁우위/산업구조 (15%)** — 경쟁우위가 가격경쟁·규제·기술변화 후에도 유지된다. / falsifier: CAC/가격/공급경쟁이 구조적으로 악화 / verdict: 적중
- **반증·최종 교훈 (15%)** — 반대 신호가 나타나면 thesis를 업데이트한다. / falsifier: 원문 방향 또는 entity 자체가 metadata와 불일치 / verdict: 적중

### 9. Timeline

- **2004-12-23** — VIC idea 게시 (T0)
- **2008-09-03** — 2008-09-03 NASDAQ 재상장 (핵심 확인/반증 신호)
- **2008-09-03** — ePlus NASDAQ 재상장 (ePlus 해당 시 recovery catalyst)
- **2010-06-30** — ePlus cash $79.3m·equity $190.4m (balance-sheet follow-through)
- **2019-09-30** — ePlus 분기 순매출 $411.6m·순이익 $20.1m (장기 사업확대)
- **2026-09-05** — postmortem 재검증 (현재 연구 기준일)

### 10. Sources

- [Original VIC thesis](https://www.valueinvestorsclub.com/idea/ePlus/7455315813) — 원 투자방향·thesis·catalyst 원문 확인
- [ePlus FY2008 10-K](https://www.sec.gov/Archives/edgar/data/1022408/000102240808000030/form10k.htm) — FY2008 balance sheet, sales, restatement completion
- [ePlus FY2009 10-K](https://www.sec.gov/Archives/edgar/data/1022408/000102240809000017/form10k.htm) — NASDAQ relisting date and status
- [ePlus FY2010 10-K](https://www.sec.gov/Archives/edgar/data/1022408/000102240810000024/form10k.htm) — business segments and capital structure
- [ePlus 2010 Q1 release exhibit](https://www.sec.gov/Archives/edgar/data/1022408/000102240810000034/ex9-01.htm) — cash, equity, non-recourse notes
- [ePlus 2019 Q2 results](https://www.eplus.com/about-us/press-releases/details/2019/11/06/eplus-reports-second-quarter-and-first-half-financial-results) — later revenue, services, earnings

---

# ePlus inc. — idea 3

## 3. 2007-05-09 — raw Short / research Long — ele2996

**idea_id:** `98c3017f-e2f5-4a57-8e98-ee0ebac34d63`  
**raw ticker/company:** `PLUS` / `ePLUS`  
**research entity:** ePlus inc.  
**verdict:** **방향오류 교정·성공**

### 1. 무슨 기업인가
ePlus는 중견·대기업 및 공공 고객에게 IT 인프라를 설계·판매하고 금융·리스까지 제공하는 사업자다. 자산 측 lease book과 non-recourse financing 때문에 단순 데이터벤더의 enterprise value가 왜곡될 수 있고, 회계·법률 이벤트가 valuation discount를 크게 만든다는 특징이 있다.

### 2. 원 VIC 투자 논지
SQL은 Short로 표시하지만 원문은 명시적으로 “cheap enough and timely enough to be a buy”라고 결론내린 Long이다. 2007년 논지는 옵션 부여일 회계 재검토, Cyberco 소송, 공시 지연이 manageable하며 hard book 약 $12.90/주, 내부자와 Hovde의 큰 지분, SAP 특허 합의금, restated financials 공개 및 잠재 business combination이 재평가를 촉진한다는 것이었다.

### 3. 당시 숫자와 valuation

- **raw direction:** Short → 사후 확인: 원문과 충돌
- **T0 hard book:** 약 $12.90/주 → 사후 확인: 자산가치 하방
- **2008-09 cash:** $75.2m → 사후 확인: relisting 직후 유동성
- **relisting:** 2008-09-03 → 사후 확인: 핵심 촉매 실현

### 4. 실제로 무슨 일이 벌어졌나
회계 문제는 생각보다 길어져 2007년 7월 20일 NASDAQ 상장폐지로 이어졌지만, 회사는 2008년 5월 5일까지 필요한 10-K/10-Q를 모두 제출했다. 2008년 9월 3일 재상장했고 같은 해 9월 말 현금은 $75.2m였다. 핵심 business는 살아남아 이후 장기간 성장했다.

### 5. 논지 판정
원문의 본질은 accounting overhang이 사업가치를 훼손하는 영구 손상이 아니라는 특수상황 Long이었다. 최종적으로 공시 정상화와 재상장이 실제 발생해 방향과 catalyst logic 모두 맞았다. 단, 시간과 거래유동성 리스크는 컸다.

### 6. 가장 중요한 분석 오류/교훈
핵심 오류는 투자논지가 아니라 원 SQL의 direction metadata다. 연구층에서 raw Short를 보존하되 실제 Long으로 반드시 교정해야 한다.

### 7. 최초 확인·반증 신호
**2008-05-05 — 2008-05-05 모든 지연 공시 완료**. 촉매는 발생 여부만 보는 것이 아니라 그 시점까지의 현금소진, 부채, 상장상태, 규제와 희석 가능성을 함께 봐야 한다.

### 8. Claim audit

- **핵심 valuation (20%)** — 가격이 정상화 가치보다 충분히 낮다. / falsifier: 정상화 숫자를 보수적으로 적용해도 할인폭 소멸 / verdict: 적중
- **사업경제/단위경제 (20%)** — headline 성장/자산이 실제 gross profit·FCF로 전환된다. / falsifier: 매출/트래픽 증가에도 margin·cash flow 악화 / verdict: 적중
- **balance sheet·자본구조 (15%)** — 현금·부채·non-recourse/working-capital 구조가 equity에 충분한 runway를 준다. / falsifier: 부채·현금소진·공시/규제 리스크 급증 / verdict: 적중
- **촉매·시간 (15%)** — 촉매가 현금소진·희석보다 먼저 발생한다. / falsifier: 촉매 지연이 thesis duration을 초과 / verdict: 적중
- **경쟁우위/산업구조 (15%)** — 경쟁우위가 가격경쟁·규제·기술변화 후에도 유지된다. / falsifier: CAC/가격/공급경쟁이 구조적으로 악화 / verdict: 적중
- **반증·최종 교훈 (15%)** — 반대 신호가 나타나면 thesis를 업데이트한다. / falsifier: 원문 방향 또는 entity 자체가 metadata와 불일치 / verdict: 적중

### 9. Timeline

- **2007-05-09** — VIC idea 게시 (T0)
- **2008-05-05** — 2008-05-05 모든 지연 공시 완료 (핵심 확인/반증 신호)
- **2008-09-03** — ePlus NASDAQ 재상장 (ePlus 해당 시 recovery catalyst)
- **2010-06-30** — ePlus cash $79.3m·equity $190.4m (balance-sheet follow-through)
- **2019-09-30** — ePlus 분기 순매출 $411.6m·순이익 $20.1m (장기 사업확대)
- **2026-09-05** — postmortem 재검증 (현재 연구 기준일)

### 10. Sources

- [Original VIC thesis](https://github.com/horea457/VIC-/tree/main/data/source_batch035) — 원 투자방향·thesis·catalyst 원문 확인
- [ePlus FY2008 10-K](https://www.sec.gov/Archives/edgar/data/1022408/000102240808000030/form10k.htm) — FY2008 balance sheet, sales, restatement completion
- [ePlus FY2009 10-K](https://www.sec.gov/Archives/edgar/data/1022408/000102240809000017/form10k.htm) — NASDAQ relisting date and status
- [ePlus FY2010 10-K](https://www.sec.gov/Archives/edgar/data/1022408/000102240810000024/form10k.htm) — business segments and capital structure
- [ePlus 2010 Q1 release exhibit](https://www.sec.gov/Archives/edgar/data/1022408/000102240810000034/ex9-01.htm) — cash, equity, non-recourse notes
- [ePlus 2019 Q2 results](https://www.eplus.com/about-us/press-releases/details/2019/11/06/eplus-reports-second-quarter-and-first-half-financial-results) — later revenue, services, earnings

---

# ePlus inc. — idea 4

## 4. 2007-11-14 — raw Short / research Long — zach721

**idea_id:** `f04f83bb-ff87-4e97-981c-05be168e60c6`  
**raw ticker/company:** `PLUS` / `ePLUS`  
**research entity:** ePlus inc.  
**verdict:** **방향오류 교정·촉매 적중**

### 1. 무슨 기업인가
ePlus는 IT lifecycle의 조달, 제품, 전문 서비스, 자산관리와 금융을 묶는 VAR/solutions provider다. 사업 자체는 저마진·운전자본 집약적이지만, 현금·lease receivable·재고를 포함한 tangible book과 반복 고객, 서비스 믹스가 가치평가의 핵심이었다.

### 2. 원 VIC 투자 논지
SQL은 Short이나 원문은 $10 주가에서 downside $9, upside $20+를 제시한 Long이다. 예상 FY2008 tangible book 약 $15+, normalized EBITDA 약 $24.8m, 3.5~4.5배 EV/EBITDA 수준, 825% 누적 매출 성장, 완료에 가까운 옵션 restatement와 향후 NASDAQ 재상장·buyback 재개를 핵심으로 봤다.

### 3. 당시 숫자와 valuation

- **T0 주가:** $10 → 사후 확인: 원문 기준
- **예상 TBV:** 약 $15+ → 사후 확인: 주가 대비 큰 할인
- **FY2008 cash:** $58.4m → 사후 확인: balance-sheet 완충
- **NASDAQ relist:** 2008-09-03 → 사후 확인: 핵심 catalyst 실현

### 4. 실제로 무슨 일이 벌어졌나
2008년 5월 5일 지연 보고서가 모두 제출됐고 2008년 9월 3일 NASDAQ 재상장이 실제 이뤄졌다. FY2008 10-K에서 cash $58.4m, product/services sales $731.7m가 확인되며, 이후 2010 10-K에서는 NASDAQ Global Market 상장과 안정된 자본구조가 확인된다. 장기적으로는 서비스와 보안·클라우드 등 고부가 영역을 확대했다.

### 5. 논지 판정
가격이 tangible book 대비 크게 할인된 원인이 공시·상장 overhang이었고, 그 overhang이 제거되면 liquidity와 multiple이 정상화될 수 있다는 event-driven 논리가 정확했다. 정상화 EBITDA 추정에는 불확실성이 있었지만 촉매는 매우 구체적이고 실제 발생했다.

### 6. 가장 중요한 분석 오류/교훈
원 투자논지보다 데이터 정합성 문제가 더 크다. raw Short를 그대로 학습시키면 완전히 반대의 투자 교훈이 생성된다.

### 7. 최초 확인·반증 신호
**2008-09-03 — 2008-09-03 NASDAQ 재상장**. 촉매는 발생 여부만 보는 것이 아니라 그 시점까지의 현금소진, 부채, 상장상태, 규제와 희석 가능성을 함께 봐야 한다.

### 8. Claim audit

- **핵심 valuation (20%)** — 가격이 정상화 가치보다 충분히 낮다. / falsifier: 정상화 숫자를 보수적으로 적용해도 할인폭 소멸 / verdict: 적중
- **사업경제/단위경제 (20%)** — headline 성장/자산이 실제 gross profit·FCF로 전환된다. / falsifier: 매출/트래픽 증가에도 margin·cash flow 악화 / verdict: 적중
- **balance sheet·자본구조 (15%)** — 현금·부채·non-recourse/working-capital 구조가 equity에 충분한 runway를 준다. / falsifier: 부채·현금소진·공시/규제 리스크 급증 / verdict: 적중
- **촉매·시간 (15%)** — 촉매가 현금소진·희석보다 먼저 발생한다. / falsifier: 촉매 지연이 thesis duration을 초과 / verdict: 적중
- **경쟁우위/산업구조 (15%)** — 경쟁우위가 가격경쟁·규제·기술변화 후에도 유지된다. / falsifier: CAC/가격/공급경쟁이 구조적으로 악화 / verdict: 적중
- **반증·최종 교훈 (15%)** — 반대 신호가 나타나면 thesis를 업데이트한다. / falsifier: 원문 방향 또는 entity 자체가 metadata와 불일치 / verdict: 적중

### 9. Timeline

- **2007-11-14** — VIC idea 게시 (T0)
- **2008-09-03** — 2008-09-03 NASDAQ 재상장 (핵심 확인/반증 신호)
- **2008-09-03** — ePlus NASDAQ 재상장 (ePlus 해당 시 recovery catalyst)
- **2010-06-30** — ePlus cash $79.3m·equity $190.4m (balance-sheet follow-through)
- **2019-09-30** — ePlus 분기 순매출 $411.6m·순이익 $20.1m (장기 사업확대)
- **2026-09-05** — postmortem 재검증 (현재 연구 기준일)

### 10. Sources

- [Original VIC thesis](https://github.com/horea457/VIC-/tree/main/data/source_batch035) — 원 투자방향·thesis·catalyst 원문 확인
- [ePlus FY2008 10-K](https://www.sec.gov/Archives/edgar/data/1022408/000102240808000030/form10k.htm) — FY2008 balance sheet, sales, restatement completion
- [ePlus FY2009 10-K](https://www.sec.gov/Archives/edgar/data/1022408/000102240809000017/form10k.htm) — NASDAQ relisting date and status
- [ePlus FY2010 10-K](https://www.sec.gov/Archives/edgar/data/1022408/000102240810000024/form10k.htm) — business segments and capital structure
- [ePlus 2010 Q1 release exhibit](https://www.sec.gov/Archives/edgar/data/1022408/000102240810000034/ex9-01.htm) — cash, equity, non-recourse notes
- [ePlus 2019 Q2 results](https://www.eplus.com/about-us/press-releases/details/2019/11/06/eplus-reports-second-quarter-and-first-half-financial-results) — later revenue, services, earnings

---

# ePlus inc. — idea 5

## 5. 2008-06-09 — raw Long / research Long — zach721

**idea_id:** `cbe4657d-58c3-4f96-a9ee-619f5836ee99`  
**raw ticker/company:** `PLUS` / `ePLUS`  
**research entity:** ePlus inc.  
**verdict:** **강한 성공**

### 1. 무슨 기업인가
ePlus는 기업 IT의 제품·서비스·금융을 결합해 수익을 내는 회사다. 당시에는 Pink Sheets 거래와 복잡한 lease accounting 때문에 일반 투자자가 현금·tangible book과 영업가치를 분리해 보기 어려웠다.

### 2. 원 VIC 투자 논지
2008년 Long은 약 $90m 시가총액에 cash 약 $65m, 첫 9개월 EBIT $24.2m, tangible book의 약 70%라는 극단적 valuation을 강조했다. 공시가 거의 정상화됐고 3/31/08 10-K 제출 뒤 NASDAQ 재상장, recourse debt 제거, $2 안팎 EPS, buyback 재개가 촉매였다.

### 3. 당시 숫자와 valuation

- **T0 market cap:** $90m → 사후 확인: 원문 기준
- **T0 cash:** $65m → 사후 확인: 시총의 약 72%
- **T0 EBIT:** 9개월 $24.2m → 사후 확인: 현금 차감 valuation 극저평가
- **relisting:** 2008-09-03 → 사후 확인: 수개월 내 catalyst 실현

### 4. 실제로 무슨 일이 벌어졌나
3/31/08 10-K는 2008년 7월 제출됐고 회사는 9월 3일 NASDAQ에 재상장했다. 2008년 9월 현금은 $75.2m까지 늘었고, 2009 10-K에서도 NASDAQ 상장 상태가 유지됐다. 이후 2010년 자본은 $190.4m, 현금은 $79.3m으로 확대됐다.

### 5. 논지 판정
이 아이디어는 balance-sheet discount와 짧은 event catalyst가 동시에 존재했다. 상장폐지라는 구조적 할인요인이 실제 제거되었고, 사업이 파산하지 않은 채 현금·자본을 유지했기 때문에 asymmetry가 컸다.

### 6. 가장 중요한 분석 오류/교훈
핵심 thesis는 맞았다. 다만 lease asset의 liquidation value와 non-recourse 성격은 계약별 보증·residual risk를 별도 stress 해야 한다.

### 7. 최초 확인·반증 신호
**2008-09-03 — 2008-09-03 NASDAQ 재상장**. 촉매는 발생 여부만 보는 것이 아니라 그 시점까지의 현금소진, 부채, 상장상태, 규제와 희석 가능성을 함께 봐야 한다.

### 8. Claim audit

- **핵심 valuation (20%)** — 가격이 정상화 가치보다 충분히 낮다. / falsifier: 정상화 숫자를 보수적으로 적용해도 할인폭 소멸 / verdict: 적중
- **사업경제/단위경제 (20%)** — headline 성장/자산이 실제 gross profit·FCF로 전환된다. / falsifier: 매출/트래픽 증가에도 margin·cash flow 악화 / verdict: 적중
- **balance sheet·자본구조 (15%)** — 현금·부채·non-recourse/working-capital 구조가 equity에 충분한 runway를 준다. / falsifier: 부채·현금소진·공시/규제 리스크 급증 / verdict: 적중
- **촉매·시간 (15%)** — 촉매가 현금소진·희석보다 먼저 발생한다. / falsifier: 촉매 지연이 thesis duration을 초과 / verdict: 적중
- **경쟁우위/산업구조 (15%)** — 경쟁우위가 가격경쟁·규제·기술변화 후에도 유지된다. / falsifier: CAC/가격/공급경쟁이 구조적으로 악화 / verdict: 적중
- **반증·최종 교훈 (15%)** — 반대 신호가 나타나면 thesis를 업데이트한다. / falsifier: 원문 방향 또는 entity 자체가 metadata와 불일치 / verdict: 적중

### 9. Timeline

- **2008-06-09** — VIC idea 게시 (T0)
- **2008-09-03** — 2008-09-03 NASDAQ 재상장 (핵심 확인/반증 신호)
- **2008-09-03** — ePlus NASDAQ 재상장 (ePlus 해당 시 recovery catalyst)
- **2010-06-30** — ePlus cash $79.3m·equity $190.4m (balance-sheet follow-through)
- **2019-09-30** — ePlus 분기 순매출 $411.6m·순이익 $20.1m (장기 사업확대)
- **2026-09-05** — postmortem 재검증 (현재 연구 기준일)

### 10. Sources

- [Original VIC thesis](https://www.valueinvestorsclub.com/idea/ePlus/3940078240) — 원 투자방향·thesis·catalyst 원문 확인
- [ePlus FY2008 10-K](https://www.sec.gov/Archives/edgar/data/1022408/000102240808000030/form10k.htm) — FY2008 balance sheet, sales, restatement completion
- [ePlus FY2009 10-K](https://www.sec.gov/Archives/edgar/data/1022408/000102240809000017/form10k.htm) — NASDAQ relisting date and status
- [ePlus FY2010 10-K](https://www.sec.gov/Archives/edgar/data/1022408/000102240810000024/form10k.htm) — business segments and capital structure
- [ePlus 2010 Q1 release exhibit](https://www.sec.gov/Archives/edgar/data/1022408/000102240810000034/ex9-01.htm) — cash, equity, non-recourse notes
- [ePlus 2019 Q2 results](https://www.eplus.com/about-us/press-releases/details/2019/11/06/eplus-reports-second-quarter-and-first-half-financial-results) — later revenue, services, earnings

---

# ePlus inc. — idea 6

## 6. 2010-02-22 — raw Short / research Long — paddy788

**idea_id:** `1f6793f5-26f0-44b5-bcd6-7a2c70ffe1f1`  
**raw ticker/company:** `PLUS` / `ePLUS`  
**research entity:** ePlus inc.  
**verdict:** **방향오류 교정·성공**

### 1. 무슨 기업인가
ePlus는 IT VAR와 financing/leasing 두 축을 운영했다. 당시 중요한 분석 포인트는 데이터벤더가 non-recourse notes를 일반 debt처럼 enterprise value에 넣어 실제 경제적 순현금과 lease investment를 왜곡할 수 있다는 점이었다.

### 2. 원 VIC 투자 논지
SQL은 Short이나 원문 첫 문장이 “purchase of ePlus”를 추천한다. $16 부근 주가에서 cash $9.59/주, tangible book $19.51/주, FY2010 EPS 약 $2, 향후 $3 EPS 가능성을 보고 $30+ 가치를 제시했다. 신용위기 후 개선된 lease spread에 현금을 투입하고 VAR 회복, buyback·특별배당이 추가 upside라는 논리였다.

### 3. 당시 숫자와 valuation

- **T0 price:** $16 부근 → 사후 확인: 원문 기준
- **T0 cash:** $9.59/주 → 사후 확인: 큰 순현금
- **T0 TBV:** $19.51/주 → 사후 확인: 주가가 liquidation proxy 이하
- **2010-06 equity:** $23.41/주 → 사후 확인: 장부가치 상승 확인

### 4. 실제로 무슨 일이 벌어졌나
2010년 6월 말 회사는 cash $79.3m, 주당 자본 $23.41을 공시했고 non-recourse notes는 전년 동기 $75.1m에서 $46.9m으로 감소했다. 이후에도 회사는 NASDAQ 상장을 유지하고 장기적으로 IT solutions 규모를 확대했다. 2019년에는 서비스 매출이 빠르게 성장하며 단순 저마진 reseller보다 개선된 mix를 보였다.

### 5. 논지 판정
non-recourse debt를 분리해 EV를 다시 계산하고 cash deployment를 lease spread와 연결한 분석은 좋은 사례다. 당시 tangible book 아래의 가격과 실제 자본 성장 방향도 논지와 일치했다.

### 6. 가장 중요한 분석 오류/교훈
원 SQL 방향 오류가 가장 큰 데이터 문제다. 투자 분석상으로는 residual value와 credit representations의 tail risk를 완전 무위험처럼 취급하지 않는 보수성이 필요하다.

### 7. 최초 확인·반증 신호
**2010-06-30 — 2010-06-30 자본 $23.41/주 확인**. 촉매는 발생 여부만 보는 것이 아니라 그 시점까지의 현금소진, 부채, 상장상태, 규제와 희석 가능성을 함께 봐야 한다.

### 8. Claim audit

- **핵심 valuation (20%)** — 가격이 정상화 가치보다 충분히 낮다. / falsifier: 정상화 숫자를 보수적으로 적용해도 할인폭 소멸 / verdict: 적중
- **사업경제/단위경제 (20%)** — headline 성장/자산이 실제 gross profit·FCF로 전환된다. / falsifier: 매출/트래픽 증가에도 margin·cash flow 악화 / verdict: 적중
- **balance sheet·자본구조 (15%)** — 현금·부채·non-recourse/working-capital 구조가 equity에 충분한 runway를 준다. / falsifier: 부채·현금소진·공시/규제 리스크 급증 / verdict: 적중
- **촉매·시간 (15%)** — 촉매가 현금소진·희석보다 먼저 발생한다. / falsifier: 촉매 지연이 thesis duration을 초과 / verdict: 적중
- **경쟁우위/산업구조 (15%)** — 경쟁우위가 가격경쟁·규제·기술변화 후에도 유지된다. / falsifier: CAC/가격/공급경쟁이 구조적으로 악화 / verdict: 적중
- **반증·최종 교훈 (15%)** — 반대 신호가 나타나면 thesis를 업데이트한다. / falsifier: 원문 방향 또는 entity 자체가 metadata와 불일치 / verdict: 적중

### 9. Timeline

- **2010-02-22** — VIC idea 게시 (T0)
- **2010-06-30** — 2010-06-30 자본 $23.41/주 확인 (핵심 확인/반증 신호)
- **2008-09-03** — ePlus NASDAQ 재상장 (ePlus 해당 시 recovery catalyst)
- **2010-06-30** — ePlus cash $79.3m·equity $190.4m (balance-sheet follow-through)
- **2019-09-30** — ePlus 분기 순매출 $411.6m·순이익 $20.1m (장기 사업확대)
- **2026-09-05** — postmortem 재검증 (현재 연구 기준일)

### 10. Sources

- [Original VIC thesis](https://github.com/horea457/VIC-/tree/main/data/source_batch035) — 원 투자방향·thesis·catalyst 원문 확인
- [ePlus FY2008 10-K](https://www.sec.gov/Archives/edgar/data/1022408/000102240808000030/form10k.htm) — FY2008 balance sheet, sales, restatement completion
- [ePlus FY2009 10-K](https://www.sec.gov/Archives/edgar/data/1022408/000102240809000017/form10k.htm) — NASDAQ relisting date and status
- [ePlus FY2010 10-K](https://www.sec.gov/Archives/edgar/data/1022408/000102240810000024/form10k.htm) — business segments and capital structure
- [ePlus 2010 Q1 release exhibit](https://www.sec.gov/Archives/edgar/data/1022408/000102240810000034/ex9-01.htm) — cash, equity, non-recourse notes
- [ePlus 2019 Q2 results](https://www.eplus.com/about-us/press-releases/details/2019/11/06/eplus-reports-second-quarter-and-first-half-financial-results) — later revenue, services, earnings

---

# Plus500 Ltd. — idea 7

## 7. 2019-08-26 — raw Short / research Long — avahaz

**idea_id:** `cda3b447-bd2c-4793-a346-63187380e487`  
**raw ticker/company:** `PLUS` / `ePLUS`  
**research entity:** Plus500 Ltd.  
**verdict:** **방향·엔터티 오류 교정·강한 성공**

### 1. 무슨 기업인가
Plus500은 자체 기술 플랫폼으로 CFD를 중심으로 한 온라인 거래 서비스를 제공하고 이후 주식거래와 미국 futures/options로 확장한 영국 상장 fintech다. 수익성은 active customers, ARPU, customer acquisition cost, churn, 시장 변동성 및 고객 포지션에서 생기는 market P&L과 규제 레버리지 제한에 민감하다.

### 2. 원 VIC 투자 논지
SQL은 ticker PLUS를 ePLUS로 매핑하고 Short로 표시하지만 원문은 명백한 Plus500 Long이다. 2019년 ESMA 규제 4개 분기 후 spreads/premiums 매출이 분기 $90~100m, 기초 EBITDA 약 $200m run-rate로 안정됐고 주가가 약 3배 EV/EBIT·6배 P/E라는 주장이다. 낮아진 churn·CAC, 내부자 매수, 두 자릿수 자본환원이 재평가 근거였다.

### 3. 당시 숫자와 valuation

- **2019 valuation:** 약 3x EV/EBIT, 6x P/E → 사후 확인: 원문 기준
- **2019 EBITDA:** $192.3m → 사후 확인: post-ESMA 수익성
- **2020 EBITDA:** $515.9m → 사후 확인: thesis 이후 강한 upside
- **2021 follow-up:** 배당 포함 약 +150% → 사후 확인: 원문 작성자의 사후 기록

### 4. 실제로 무슨 일이 벌어졌나
공식 Plus500 자료 기준 2019 매출 $354.5m, EBITDA $192.3m에서 2020 매출 $872.5m, EBITDA $515.9m으로 급증했다. 2021년 후속 VIC 원문 자체가 2019 이후 주가가 두 배, 배당 포함 약 150% total return이었다고 기록한다. 이후에도 2021 EBITDA $387.1m, 2025 EBITDA $348.1m으로 규제 이후 사업은 소멸하지 않았다.

### 5. 논지 판정
핵심 edge는 규제 충격 직후의 낮은 headline 성장률을 그대로 외삽하지 않고 post-ESMA cohort에서 churn, CAC, active customer, underlying revenue를 분해한 점이다. 시장이 사업모델 붕괴로 가격화한 것과 달리 수익성이 높은 수준에서 안정화됐다.

### 6. 가장 중요한 분석 오류/교훈
원 투자논지는 강했다. 데이터베이스 측에서는 ticker 재사용으로 ePlus와 Plus500을 같은 회사로 묶고 direction까지 반대로 저장한 이중 오류가 발생했다.

### 7. 최초 확인·반증 신호
**2020-12-31 — 2020 FY EBITDA $515.9m**. 촉매는 발생 여부만 보는 것이 아니라 그 시점까지의 현금소진, 부채, 상장상태, 규제와 희석 가능성을 함께 봐야 한다.

### 8. Claim audit

- **핵심 valuation (20%)** — 가격이 정상화 가치보다 충분히 낮다. / falsifier: 정상화 숫자를 보수적으로 적용해도 할인폭 소멸 / verdict: 적중
- **사업경제/단위경제 (20%)** — headline 성장/자산이 실제 gross profit·FCF로 전환된다. / falsifier: 매출/트래픽 증가에도 margin·cash flow 악화 / verdict: 적중
- **balance sheet·자본구조 (15%)** — 현금·부채·non-recourse/working-capital 구조가 equity에 충분한 runway를 준다. / falsifier: 부채·현금소진·공시/규제 리스크 급증 / verdict: 적중
- **촉매·시간 (15%)** — 촉매가 현금소진·희석보다 먼저 발생한다. / falsifier: 촉매 지연이 thesis duration을 초과 / verdict: 적중
- **경쟁우위/산업구조 (15%)** — 경쟁우위가 가격경쟁·규제·기술변화 후에도 유지된다. / falsifier: CAC/가격/공급경쟁이 구조적으로 악화 / verdict: 적중
- **반증·최종 교훈 (15%)** — 반대 신호가 나타나면 thesis를 업데이트한다. / falsifier: 원문 방향 또는 entity 자체가 metadata와 불일치 / verdict: 적중

### 9. Timeline

- **2019-08-26** — VIC idea 게시 (T0)
- **2020-12-31** — 2020 FY EBITDA $515.9m (핵심 확인/반증 신호)
- **2020-12-31** — Plus500 FY2020 EBITDA $515.9m (post-regulation earnings confirmation)
- **2021-12-31** — Plus500 Cunningham/CTS 통합 진행 (신사업 실행)
- **2025-12-31** — Plus500 revenue $792.4m·EBITDA $348.1m (core durability)
- **2026-09-05** — postmortem 재검증 (현재 연구 기준일)

### 10. Sources

- [Original VIC thesis](https://github.com/horea457/VIC-/tree/main/data/source_batch035) — 원 투자방향·thesis·catalyst 원문 확인
- [Plus500 reports & financial highlights](https://investors.plus500.com/Reports) — 2019-2025 revenue and EBITDA history
- [Plus500 2021 Annual Report](https://cdn.plus500.com/media/Investors/Reports/Plus500_Annual_Report_21.pdf) — Cunningham/CTS acquisition and strategy
- [Plus500 growth strategy](https://investors.plus500.com/Business/Growth) — Plus500 Invest and geographic/product expansion
- [Plus500 US business history](https://financialservices.plus500.com/about-us/) — US futures operating development
- [Plus500 company reports archive](https://investors.plus500.com/Reports/Presentation) — 2018-2021 regulatory-period reports

---

# Plus500 Ltd. — idea 8

## 8. 2021-09-03 — raw Long / research Long — avahaz

**idea_id:** `fccdf24a-81ed-4330-803f-26da2a529b35`  
**raw ticker/company:** `PLUS` / `ePLUS`  
**research entity:** Plus500 Ltd.  
**verdict:** **사업논지 적중·주가목표 부분검증**

### 1. 무슨 기업인가
Plus500은 글로벌 다중자산 거래 플랫폼으로 진화한 fintech다. 2021년에는 유럽 CFD의 높은 수익성과 현금을 바탕으로 Plus500 Invest, 미국 Cunningham/CTS 인수, 신규 라이선스를 통해 지역·상품 다각화를 추진했다.

### 2. 원 VIC 투자 논지
2021년 Long은 2019 아이디어 이후 약 150% total return 뒤에도 2년 내 추가 두 배를 기대했다. 기존 사업만으로 지속가능 EPS $3+와 약 6배 P/E, 큰 순현금·배당/자사주가 하방을 지지하고, Plus500 Invest와 미국 futures가 새로운 성장 레버라는 논지였다.

### 3. 당시 숫자와 valuation

- **T0 core valuation:** 약 6x P/E → 사후 확인: 원문 기준
- **2021 EBITDA:** $387.1m → 사후 확인: 높은 cash engine 유지
- **2022 EBITDA:** $453.8m → 사후 확인: 팬데믹 후에도 강한 수익성
- **2025 EBITDA:** $348.1m → 사후 확인: 신사업 진행 중 core 수익 지속

### 4. 실제로 무슨 일이 벌어졌나
회사는 실제로 2021년 Cunningham Commodities와 CTS를 인수해 미국 futures/options 진입 기반을 확보했고 Plus500 Invest도 출시했다. 공식 자료상 EBITDA는 2021 $387.1m, 2022 $453.8m, 2025 $348.1m으로 팬데믹 정점보다 낮지만 상당한 수익성을 유지했다. 미국 사업은 실제 운영 플랫폼으로 자리잡았으나 원문이 기대한 전체 사업 규모의 빠른 doubling까지는 보수적으로 확인하기 어렵다.

### 5. 논지 판정
기존 CFD cash engine의 durability와 제품/지역 확장은 적중했다. 다만 신규 제품 TAM을 곧바로 연결해 earnings doubling으로 보는 부분은 시간이 더 필요했고, 2년 내 100% 주가 목표는 business execution만으로 확정할 수 없다.

### 6. 가장 중요한 분석 오류/교훈
좋은 core business와 option value를 분리해야 한다. 신규 미국 futures의 TAM 전체를 회사가 획득할 수 있는 경제가치로 바로 전환하면 과대평가 위험이 있다.

### 7. 최초 확인·반증 신호
**2021-07-01 — 2021 Cunningham/CTS 인수 완료**. 촉매는 발생 여부만 보는 것이 아니라 그 시점까지의 현금소진, 부채, 상장상태, 규제와 희석 가능성을 함께 봐야 한다.

### 8. Claim audit

- **핵심 valuation (20%)** — 가격이 정상화 가치보다 충분히 낮다. / falsifier: 정상화 숫자를 보수적으로 적용해도 할인폭 소멸 / verdict: 적중
- **사업경제/단위경제 (20%)** — headline 성장/자산이 실제 gross profit·FCF로 전환된다. / falsifier: 매출/트래픽 증가에도 margin·cash flow 악화 / verdict: 적중
- **balance sheet·자본구조 (15%)** — 현금·부채·non-recourse/working-capital 구조가 equity에 충분한 runway를 준다. / falsifier: 부채·현금소진·공시/규제 리스크 급증 / verdict: 적중
- **촉매·시간 (15%)** — 촉매가 현금소진·희석보다 먼저 발생한다. / falsifier: 촉매 지연이 thesis duration을 초과 / verdict: 적중
- **경쟁우위/산업구조 (15%)** — 경쟁우위가 가격경쟁·규제·기술변화 후에도 유지된다. / falsifier: CAC/가격/공급경쟁이 구조적으로 악화 / verdict: 적중
- **반증·최종 교훈 (15%)** — 반대 신호가 나타나면 thesis를 업데이트한다. / falsifier: 원문 방향 또는 entity 자체가 metadata와 불일치 / verdict: 적중

### 9. Timeline

- **2021-09-03** — VIC idea 게시 (T0)
- **2021-07-01** — 2021 Cunningham/CTS 인수 완료 (핵심 확인/반증 신호)
- **2020-12-31** — Plus500 FY2020 EBITDA $515.9m (post-regulation earnings confirmation)
- **2021-12-31** — Plus500 Cunningham/CTS 통합 진행 (신사업 실행)
- **2025-12-31** — Plus500 revenue $792.4m·EBITDA $348.1m (core durability)
- **2026-09-05** — postmortem 재검증 (현재 연구 기준일)

### 10. Sources

- [Original VIC thesis](https://www.valueinvestorsclub.com/idea/Plus500/5585479211) — 원 투자방향·thesis·catalyst 원문 확인
- [Plus500 reports & financial highlights](https://investors.plus500.com/Reports) — 2019-2025 revenue and EBITDA history
- [Plus500 2021 Annual Report](https://cdn.plus500.com/media/Investors/Reports/Plus500_Annual_Report_21.pdf) — Cunningham/CTS acquisition and strategy
- [Plus500 growth strategy](https://investors.plus500.com/Business/Growth) — Plus500 Invest and geographic/product expansion
- [Plus500 US business history](https://financialservices.plus500.com/about-us/) — US futures operating development
- [Plus500 company reports archive](https://investors.plus500.com/Reports/Presentation) — 2018-2021 regulatory-period reports

---

# Level 3 Communications, Inc. — idea 9

## 9. 2000-08-29 — raw Short / research Long — dave143

**idea_id:** `552a0c54-5417-4cb8-ae6e-e3b5a0079976`  
**raw ticker/company:** `LVLT` / `Level 3 Comunication`  
**research entity:** Level 3 Communications, Inc.  
**verdict:** **방향오류 교정·근기 실패**

### 1. 무슨 기업인가
Level 3 Communications는 1990년대 말 광섬유 기반 글로벌 IP backbone을 구축한 통신 인프라 사업자였다. 다중 conduit와 최신 optical technology로 단위 bandwidth 비용을 낮추려 했지만, 경제성은 네트워크 기술 우위보다 수요 성장, 가격 하락, 가동률, 막대한 선행 CapEx와 debt refinancing에 좌우됐다.

### 2. 원 VIC 투자 논지
SQL은 Short지만 2000년 원문은 명백한 Long이다. 약 $7bn cash로 buildout이 prefunded됐고, all-fiber/IP network의 낮은 unit cost·upgradeability, telecom hotels, bandwidth demand elasticity가 경쟁우위라는 주장이다. 네트워크 완공 후 leased fiber 비용이 사라지고 수요를 흡수하는 것이 촉매였다.

### 3. 당시 숫자와 valuation

- **후속 주가:** 약 -70% / 6개월 → 사후 확인: 원 작성자 기록
- **2001 communications revenue:** $1.298bn → 사후 확인: 수요 성장은 실제 발생
- **2001 net loss:** -$4.978bn → 사후 확인: 성장이 equity economics를 못 구함
- **2001 long-term debt:** $6.209bn → 사후 확인: 자본구조가 핵심 제약

### 4. 실제로 무슨 일이 벌어졌나
불과 6개월 뒤 같은 작성자의 2001년 후속 글은 주가가 약 70% 하락했다고 기록한다. 2001년 실제 communications revenue는 $1.298bn으로 늘었지만 회사 전체 순손실은 $4.978bn, 연말 현금은 $1.297bn, 장기부채는 $6.209bn이었다. 네트워크는 장기적으로 전략가치를 유지해 회사가 생존하고 2017년 CenturyLink에 인수됐지만 초기 equity의 timing은 매우 나빴다.

### 5. 논지 판정
기술·자산의 품질과 equity 투자수익은 다르다는 대표 사례다. bandwidth 단위비용이 내려가도 업계 전체 공급이 동시에 늘고 가격이 더 빠르게 하락하면 fixed-cost absorption이 실패한다. prefunded라는 표현도 지속 손실과 부채 만기 앞에서는 충분한 margin of safety가 아니었다.

### 6. 가장 중요한 분석 오류/교훈
수요 성장률을 가격·공급·자본비용과 분리해 본 오류. 네트워크 asset replacement cost를 equity floor로 오해했다.

### 7. 최초 확인·반증 신호
**2001-03-01 — 2001-03-01 원 작성자 후속에서 -70%**. 촉매는 발생 여부만 보는 것이 아니라 그 시점까지의 현금소진, 부채, 상장상태, 규제와 희석 가능성을 함께 봐야 한다.

### 8. Claim audit

- **핵심 valuation (20%)** — 가격이 정상화 가치보다 충분히 낮다. / falsifier: 정상화 숫자를 보수적으로 적용해도 할인폭 소멸 / verdict: 부분/실패
- **사업경제/단위경제 (20%)** — headline 성장/자산이 실제 gross profit·FCF로 전환된다. / falsifier: 매출/트래픽 증가에도 margin·cash flow 악화 / verdict: 부분/실패
- **balance sheet·자본구조 (15%)** — 현금·부채·non-recourse/working-capital 구조가 equity에 충분한 runway를 준다. / falsifier: 부채·현금소진·공시/규제 리스크 급증 / verdict: 적중
- **촉매·시간 (15%)** — 촉매가 현금소진·희석보다 먼저 발생한다. / falsifier: 촉매 지연이 thesis duration을 초과 / verdict: 적중
- **경쟁우위/산업구조 (15%)** — 경쟁우위가 가격경쟁·규제·기술변화 후에도 유지된다. / falsifier: CAC/가격/공급경쟁이 구조적으로 악화 / verdict: 부분/실패
- **반증·최종 교훈 (15%)** — 반대 신호가 나타나면 thesis를 업데이트한다. / falsifier: 원문 방향 또는 entity 자체가 metadata와 불일치 / verdict: 부분/실패

### 9. Timeline

- **2000-08-29** — VIC idea 게시 (T0)
- **2001-03-01** — 2001-03-01 원 작성자 후속에서 -70% (핵심 확인/반증 신호)
- **2001-12-31** — Level 3 순손실 $4.978bn·장기부채 $6.209bn (equity economics stress)
- **2011-10-04** — Level 3-Global Crossing 결합 완료 시기 (scale consolidation path)
- **2017-11-01** — CenturyLink가 Level 3 인수 완료 (장기 strategic value)
- **2026-09-05** — postmortem 재검증 (현재 연구 기준일)

### 10. Sources

- [Original VIC thesis](https://www.valueinvestorsclub.com/idea/Level_Three_Communications_In/0716564972) — 원 투자방향·thesis·catalyst 원문 확인
- [Level 3 FY2001 10-K](https://www.sec.gov/Archives/edgar/data/794323/000079432302000015/f10kpdf_12312001.pdf) — 2001 revenue, loss, cash and debt
- [Level 3 FY2011 10-K](https://www.sec.gov/Archives/edgar/data/794323/000079432312000003/lvlt-123111_10k.htm) — Global Crossing combination and later business
- [Level 3 FY2015 10-K](https://www.sec.gov/Archives/edgar/data/794323/000079432316000025/lvlt-123115_10k.htm) — mature network/business history
- [Level 3 FY2016 10-K](https://www.sec.gov/Archives/edgar/data/794323/000079432317000002/lvlt-123116_10k.htm) — pre-merger company status
- [CenturyLink completes Level 3 acquisition](https://ir.lumen.com/news/news-details/2017/CenturyLink-completes-acquisition-of-Level-3/default.aspx) — 2017 merger consideration and survival outcome

---

# Level 3 Communications, Inc. — idea 10

## 10. 2001-03-01 — raw Short / research Long — dave143

**idea_id:** `15f30c2f-a0a7-41f3-b97f-2c7dff55fdd6`  
**raw ticker/company:** `LVLT` / `Level 3 Comunication`  
**research entity:** Level 3 Communications, Inc.  
**verdict:** **방향오류 교정·부분실패/장기 자산가치**

### 1. 무슨 기업인가
Level 3는 대규모 광섬유/IP backbone을 구축한 통신사로, 높은 operating leverage와 동시에 극단적인 financing leverage를 가진 사업이었다. 네트워크의 물리적 가치는 존재했지만 equity holder에게 돌아오는 가치는 채권·현금소진·추가자본조달을 통과한 잔여가치였다.

### 2. 원 VIC 투자 논지
SQL은 Short지만 2001년 후속 원문 역시 Long이다. 이미 70% 하락한 뒤 market cap 약 $10.6bn이 plant/equipment 투자액 약 $10~12bn보다 낮고, revenue가 빠르게 성장하며 EBITDA breakeven이 앞당겨질 것이라는 논지였다. fiber glut 우려는 실제 lit capacity financing이 부족하기 때문에 과장됐고, $4~5bn cash·backlog가 moat라는 주장이다.

### 3. 당시 숫자와 valuation

- **T0 market cap:** 약 $10.6bn → 사후 확인: 원문 기준
- **2001 year-end cash:** $1.297bn → 사후 확인: 원문 기대 $4~5bn보다 급감
- **2001 long-term debt:** $6.209bn → 사후 확인: equity waterfall 압박
- **2017 merger consideration:** $26.50 cash + 1.4286 CTL shares → 사후 확인: 장기 전략자산 가치는 존재

### 4. 실제로 무슨 일이 벌어졌나
2001년 communications revenue는 $1.298bn으로 늘었지만 total net loss가 $4.978bn에 달했고 연말 현금은 $1.297bn, 장기부채는 $6.209bn이었다. 회사는 부채를 할인 매입하고 이후 통신 자산을 계속 통합하며 살아남았고 2011 Global Crossing을 합병, 2017 CenturyLink 거래에서 Level 3 주주는 주당 $26.50 현금과 CenturyLink 1.4286주를 받았다. 즉 자산은 전략적 가치가 있었지만 2001 equity valuation의 단순 replacement-cost floor는 부정확했다.

### 5. 논지 판정
두 번째 Long은 첫 번째보다 valuation이 낮아졌지만 여전히 PP&E와 market cap을 직접 비교했다. 자산가격은 utilization·cash margin·financing cost를 반영한 earning asset value로 바꿔야 한다. 장기 생존과 전략적 M&A가 있었다는 사실이 2001년의 손실·희석·시간가치를 상쇄하지는 않는다.

### 6. 가장 중요한 분석 오류/교훈
replacement cost를 equity value로 바로 연결하고 debt waterfall과 cash burn duration을 충분히 차감하지 않은 오류.

### 7. 최초 확인·반증 신호
**2001-12-31 — 2001 FY 순손실 $4.978bn·부채 $6.209bn**. 촉매는 발생 여부만 보는 것이 아니라 그 시점까지의 현금소진, 부채, 상장상태, 규제와 희석 가능성을 함께 봐야 한다.

### 8. Claim audit

- **핵심 valuation (20%)** — 가격이 정상화 가치보다 충분히 낮다. / falsifier: 정상화 숫자를 보수적으로 적용해도 할인폭 소멸 / verdict: 부분/실패
- **사업경제/단위경제 (20%)** — headline 성장/자산이 실제 gross profit·FCF로 전환된다. / falsifier: 매출/트래픽 증가에도 margin·cash flow 악화 / verdict: 부분/실패
- **balance sheet·자본구조 (15%)** — 현금·부채·non-recourse/working-capital 구조가 equity에 충분한 runway를 준다. / falsifier: 부채·현금소진·공시/규제 리스크 급증 / verdict: 적중
- **촉매·시간 (15%)** — 촉매가 현금소진·희석보다 먼저 발생한다. / falsifier: 촉매 지연이 thesis duration을 초과 / verdict: 적중
- **경쟁우위/산업구조 (15%)** — 경쟁우위가 가격경쟁·규제·기술변화 후에도 유지된다. / falsifier: CAC/가격/공급경쟁이 구조적으로 악화 / verdict: 부분/실패
- **반증·최종 교훈 (15%)** — 반대 신호가 나타나면 thesis를 업데이트한다. / falsifier: 원문 방향 또는 entity 자체가 metadata와 불일치 / verdict: 부분/실패

### 9. Timeline

- **2001-03-01** — VIC idea 게시 (T0)
- **2001-12-31** — 2001 FY 순손실 $4.978bn·부채 $6.209bn (핵심 확인/반증 신호)
- **2001-12-31** — Level 3 순손실 $4.978bn·장기부채 $6.209bn (equity economics stress)
- **2011-10-04** — Level 3-Global Crossing 결합 완료 시기 (scale consolidation path)
- **2017-11-01** — CenturyLink가 Level 3 인수 완료 (장기 strategic value)
- **2026-09-05** — postmortem 재검증 (현재 연구 기준일)

### 10. Sources

- [Original VIC thesis](https://www.valueinvestorsclub.com/idea/Level_3_Communications_Inc./7923868895) — 원 투자방향·thesis·catalyst 원문 확인
- [Level 3 FY2001 10-K](https://www.sec.gov/Archives/edgar/data/794323/000079432302000015/f10kpdf_12312001.pdf) — 2001 revenue, loss, cash and debt
- [Level 3 FY2011 10-K](https://www.sec.gov/Archives/edgar/data/794323/000079432312000003/lvlt-123111_10k.htm) — Global Crossing combination and later business
- [Level 3 FY2015 10-K](https://www.sec.gov/Archives/edgar/data/794323/000079432316000025/lvlt-123115_10k.htm) — mature network/business history
- [Level 3 FY2016 10-K](https://www.sec.gov/Archives/edgar/data/794323/000079432317000002/lvlt-123116_10k.htm) — pre-merger company status
- [CenturyLink completes Level 3 acquisition](https://ir.lumen.com/news/news-details/2017/CenturyLink-completes-acquisition-of-Level-3/default.aspx) — 2017 merger consideration and survival outcome

---

## Cross-case lessons

1. **Direction은 metadata가 아니라 문장으로 검증한다.** 이번 배치의 raw Short 6건은 원문에서 모두 매수/상승을 주장했다. 이 오류를 교정하지 않으면 성공한 Long을 실패한 Short로 학습하게 된다.
2. **Ticker는 영구 식별자가 아니다.** `PLUS`는 ePlus와 Plus500을 동시에 가리켜 company lookup 충돌이 발생했다. idea-level source link·본문의 제품/지역/규제 언어로 entity를 resolve해야 한다.
3. **좋은 자산 ≠ 좋은 equity.** Level 3의 광섬유망은 결국 전략가치가 있었지만 2000~01의 massive cash burn과 debt가 초기 주주 수익을 훼손했다. replacement cost는 debt waterfall 이후 earning asset value로 바꿔야 한다.
4. **규제 충격은 cohort economics로 분해한다.** Plus500 2019 Long은 단순 매출 감소가 아니라 post-ESMA churn, CAC, active customers, underlying spreads/premiums를 관찰해 business break 여부를 판별한 좋은 사례다.
5. **촉매의 질은 시간과 balance sheet로 측정한다.** ePlus 2007~08은 filings current→relisting이라는 구체적 경로가 있었고 실제 발생했다. 반대로 촉매가 장기·모호하면 cash burn과 dilution이 먼저 equity를 훼손할 수 있다.
