# Alliance Gaming (AGI) — 2000-08-29 VIC Long

> **Idea unit:** 2000-08-29 Alliance Gaming common equity Long.
> **Research as-of:** 2026-09-18. SQL company mapping은 Alamos Gold로 잘못 덮였고 raw Short도 오류다. 실제는 **Alliance Gaming Long**이다.

---

## 0. Idea Snapshot

| 항목 | 내용 |
|---|---|
| 회사 / 당시 Ticker | Alliance Gaming Corporation / AGI |
| VIC 게시일 / 작성자 | 2000-08-29 / david88 |
| 실제 방향 | Common equity Long |
| 원 SQL 방향 | **Short — 오류** |
| SQL company mapping | **Alamos Gold — 오류** |
| 당시 EV/EBITDA | 약 **7.1x** |
| debt / equity value | 약 **$345m / $25m** |
| TTM EBITDA | 약 **$51.7m** before unusual items |
| interest expense | 약 **$33.6m** |
| 핵심 upside | Native American gaming expansion + replacement cycle + shared-revenue games |
| 2006 event | 회사명 **Bally Technologies**로 변경 |
| 2014 terminal event | Scientific Games **$83.30 cash/share** 인수 |
| 최종 판정 | **장기 매우 강한 성공 — leveraged gaming call option이 major strategic asset으로 성장** |

> **결론:** 이 AGI는 Alamos Gold가 아니라 slot-machine maker **Alliance Gaming**이다. 원문은 governance가 나쁘고 debt가 매우 높지만, gaming-machine replacement cycle과 California Native American casinos, cashless gaming, recurring participation games가 조금만 개선돼도 equity가 크게 convex하다고 봤다. 회사는 살아남아 2006 Bally Technologies로 이름을 바꾸고 industry leader로 성장했으며, 2014 Scientific Games가 $83.30 cash/share에 인수했다. 과거 split history가 완전히 재구성되지 않았으므로 2000 가격과 $83.30을 직접 나눠 exact multiple은 만들지 않지만 **장기 thesis는 매우 강한 성공**이다.

---

## 1. 왜 AGI mapping이 틀렸는가

현재 SQL companies table은 ticker AGI를 Alamos Gold에 연결하지만 historical ticker reuse 때문에 2000 idea가 잘못 매핑됐다.

원문은 slots, gaming systems, Native American casinos, Betty Boop participation game을 다룬다. 따라서 legal entity는 명백히 **Alliance Gaming Corporation**이다.

---

## 2. 당시 구조

Alliance Gaming은 매우 leveraged했다.

- debt 약 $345m
- equity market value 약 $25m
- TTM EBITDA 약 $51.7m
- interest expense 약 $33.6m

즉 common은 사실상 **call option on enterprise value above debt stack**이었다.

---

## 3. Claim Map

### C1. gaming replacement cycle 개선 — **강한 성공 방향**
Bally는 이후 gaming equipment/systems major supplier로 성장했다.

### C2. recurring/participation games — **성공**
gaming operations와 systems가 recurring revenue source가 됐다.

### C3. California/tribal gaming opportunity — **성공 방향**
Native American gaming expansion은 industry growth driver가 됐다.

### C4. debt leverage가 equity convexity 제공 — **강한 성공**
회사가 insolvency 없이 EBITDA를 키우면서 equity residual이 크게 확대됐다.

### C5. governance/management risk — **초기 real risk**
management void와 governance issue는 discount 이유였으나 terminal outcome을 막지 않았다.

---

## 4. 실제 경로

| 시점 | 사건 |
|---|---|
| 2000-08 | VIC Long |
| 2000s | gaming equipment/systems 성장 |
| 2006-03 | Alliance Gaming → **Bally Technologies** name change |
| 2013 | SHFL acquisition |
| 2014-08 | Scientific Games merger agreement |
| 2014-11-21 | acquisition completed at **$83.30 cash/share** |

---

## 5. 왜 exact return을 만들지 않는가

장기간 security에는 share-count changes와 potential splits가 있어 현재 $83.30 takeout을 2000 nominal quote와 단순 비교하면 오류 가능성이 있다.

따라서 corporate lineage와 terminal value는 확인하되 exact IRR은 유보한다.

---

## 6. 재사용 가능한 교훈

1. historical ticker는 legal entity/date로 검증한다.
2. highly leveraged equity는 downside와 upside 모두 option-like다.
3. debt가 많아도 EBITDA growth path가 명확하면 equity convexity가 매우 클 수 있다.
4. industry replacement cycle은 new-unit growth와 다른 demand driver다.
5. 장기 corporate-action return은 split history 없이는 억지로 정밀화하지 않는다.

---

## 7. 최종 Scorecard

| 평가축 | 판정 |
|---|---|
| Entity identification | SQL 교정 필요 |
| Industry thesis | 강한 성공 |
| Leverage convexity | 강한 성공 |
| Strategic exit | 강한 성공 |
| Thesis score | 9.6/10 |
| Process score | 9.9/10 |
| 종합 | **장기 매우 강한 성공 — Alliance Gaming → Bally → $83.30 cash acquisition** |

### 한 문장 교훈

> 부채가 큰 cyclical equity는 **살아남아 EBITDA가 커질 경우 residual equity가 비선형적으로 커진다.**

---

## 8. Sources / Validation Notes

1. VIC original: https://www.valueinvestorsclub.com/idea/Alliance_Gaming/1840155701
2. SEC confirming Alliance Gaming changed name to Bally Technologies March 6, 2006: https://www.sec.gov/Archives/edgar/data/2491/000110465906032286/a06-11460_18k.htm
3. Scientific Games/Bally merger agreement and $83.30 cash consideration: https://www.sec.gov/Archives/edgar/data/2491/000110465914056205/a14-18280_28k.htm
4. Acquisition completion: https://www.sec.gov/Archives/edgar/data/2491/000110465914083450/a14-25061_28k.htm

### 데이터 품질
- T0 thesis: **A**
- identity/name change/takeout: **A**
- exact historical IRR: **미확정**
