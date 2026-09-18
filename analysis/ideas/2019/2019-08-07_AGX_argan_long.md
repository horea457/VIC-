# Argan Inc. (AGX) — 2019-08-07 VIC Long

> **Idea unit:** 2019-08-07 Argan common equity Long.
> **Research as-of:** 2026-09-18. 원 SQL은 Short지만 원문은 명백한 **Long**이다.

---

## 0. Idea Snapshot

| 항목 | 내용 |
|---|---|
| 회사 / Ticker | Argan Inc. / AGX |
| VIC 게시일 / 작성자 | 2019-08-07 / Dr1004 |
| 실제 방향 | Common equity Long |
| 원 SQL 방향 | **Short — 오류** |
| 당시 가격 | 약 **$40** |
| backlog | 약 **$1.4bn**, 원문 기대 **$2.5bn** |
| revenue thesis | **~$200m run-rate → >$1bn** |
| EPS forecasts | FY21 **$5.60**, FY22 **$7.50**, FY23 **$7.10** |
| target | **$70~80** |
| actual FY2020 diluted EPS | **-$2.73** |
| actual FY2021 diluted EPS | **$1.51** |
| actual FY2022 diluted EPS | **$2.40** |
| actual FY2022 revenue | **$509.4m** |
| 2022 YE stock | mid-$30s |
| 최종 판정 | **명확한 실패 — backlog를 revenue/EPS로 너무 빠르게 환산** |

> **결론:** 2019 글은 $40 주가에 약 $19/share net cash와 $1.4bn backlog를 갖고 있어, backlog가 $2.5bn까지 늘고 revenue가 $1bn을 넘으면 $70~80 가치가 가능하다고 봤다. 그러나 backlog에는 financing/NTP가 지연된 projects가 포함돼 있었고 실제 revenue ramp는 훨씬 느렸다. FY2020 EPS는 -$2.73, FY2021 $1.51, FY2022 $2.40으로 원문 $5.60/$7.50 forecasts에 크게 못 미쳤다. FY2022 revenue도 $509m이었다. **backlog 자체는 존재했지만 timing-adjusted backlog가 아니었다.**

---

## 1. 원문 투자논지

원문:
- net cash ~$19/share
- backlog $1.4bn
- prospective backlog $2.5bn
- revenue run-rate ~$200m
- expected revenue >$1bn
- three-year cumulative FCF ~$20/share
- EPS $5.60 / $7.50 / $7.10
- target $70~80

을 제시했다.

핵심은 **project awards가 빠르게 NTP를 받고 3년 안에 P&L로 전환**된다는 가정이었다.

---

## 2. Claim Map

### C1. backlog grows materially — **부분 성공**
수주 파이프라인은 존재했지만 일부 프로젝트가 financing/NTP에서 오래 지연됐다.

### C2. revenue >$1bn quickly — **실패**
FY2022 revenue **$509.4m**.

### C3. FY21 EPS $5.60 — **강한 실패**
actual **$1.51**.

### C4. FY22 EPS $7.50 — **강한 실패**
actual **$2.40**.

### C5. $70~80 within thesis horizon — **실패**
2022 year-end mid-$30s.

---

## 3. 실제 경로

| FY | Revenue | Diluted EPS |
|---|---:|---:|
| 2020 | ~$239.0m | **-$2.73** |
| 2021 | ~$392.2m | **$1.51** |
| 2022 | **$509.4m** | **$2.40** |

2021~22에도 일부 대형 projects는 schedule/NTP 지연을 겪었다.

---

## 4. 왜 Backlog가 틀렸나

Backlog는 회계상 확정 매출이 아니다.

EPC에서는:

**Expected backlog value = contract value × financing probability × NTP probability × schedule factor**

로 보는 편이 더 현실적이다.

2019 thesis는 contract value를 너무 빠르게 revenue와 EPS로 연결했다.

---

## 5. 2013/2016과 무엇이 달랐나

2013·2016:
- near-term financing/NTP evidence가 강함
- actual cash conversion이 빠름

2019:
- larger headline backlog
- project timing uncertainty 큼
- 일부 projects가 오랫동안 backlog에 머묾

즉 **headline backlog는 커졌지만 quality-adjusted backlog는 낮았다.**

---

## 6. 재사용 가능한 교훈

1. backlog에 financing probability를 곱한다.
2. EPC earnings forecast는 project start dates에 매우 민감하다.
3. net cash가 있어도 idle period earnings를 보상하지 못할 수 있다.
4. multi-year FCF forecast는 individual project schedules로 분해한다.
5. 이전 성공 vintage의 모델을 새 backlog에 그대로 복사하지 않는다.

---

## 7. 최종 Scorecard

| 평가축 | 판정 |
|---|---|
| Backlog headline | 일부 맞음 |
| Revenue forecast | 실패 |
| EPS forecast | 강한 실패 |
| Valuation target | 실패 |
| Thesis score | 3.0/10 |
| Process score | 9.8/10 |
| 종합 | **명확한 실패 — NTP-adjusted backlog를 보지 않은 오류** |

### 한 문장 교훈

> EPC backlog는 **계약금액이 아니라 financing과 NTP를 통과한 확률가중 미래매출**로 봐야 한다.

---

## 8. Sources / Validation Notes

1. VIC original / uploaded SQL, 2019-08-07.
2. Argan FY2020–FY2022 filings — revenue and diluted EPS.
3. Argan backlog/project-delay disclosures.
4. Historical AGX price series.

### 데이터 품질
- T0 thesis: **A**
- operating actuals: **A**
- historical price: **B**
