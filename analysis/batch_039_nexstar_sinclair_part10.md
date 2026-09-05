<!-- idea:8bdb5e43-ba08-4a61-8e15-7733116ba20d -->
## 10. 2015-08-16 — 2015 FCF yield + $2bn spectrum optionality Long
### 1. 결론부터

**종합판정: 혼합·core 성공 / spectrum 옵션 실패.** 이 아이디어는 core FCF와 event optionality를 섞은 전형적 사례다. core business valuation은 저렴했고 단기 실적도 좋았지만 spectrum을 management estimate로 곧바로 equity value에 더한 부분은 실패했다.

### 2. 원 투자논지

성장투자 전 18%, 성장투자 후 16% 수준의 FCF yield에 retrans 성장과 2016 정치광고를 기본가치로 두고, 경영진이 언급한 약 $2bn spectrum monetization 가능성을 큰 무료 옵션으로 봤다. spectrum만으로 시총의 약 75% 가치를 주장했다.

원문 SQL에는 `is_short=true`가 저장돼 있지만 실제 증권 방향은 **Long**이다. 이 차이는 raw 데이터 자체를 수정하지 않고 research layer의 `research_direction_ko`와 `security_instrument_ko`에 명시했다.

### 3. 사업과 돈의 흐름

Sinclair의 경제성은 local/national advertising, election-cycle political advertising, retransmission/distribution, digital에서 발생한다. station 운영은 fixed-cost 비중이 높아 추가 매출의 incremental margin이 높을 수 있지만, network affiliation fee와 debt service가 이를 흡수할 수 있다. 그래서 `gross retrans 성장 → EBITDA 성장`이라는 단순 연결보다 **net retrans contribution, leverage, cash interest, capex, share count**를 함께 봐야 한다.

### 4. 핵심 가정과 당시 관찰 가능 변수

당시 투자자가 확인할 수 있었던 것은 retrans 계약 갱신과 carriage dispute, station별/시장별 규모, 정치광고 cycle, 인수 multiple과 financing, covenant/leverage, network affiliation fee, station divestiture 필요성, 그리고 FCF 대비 market capitalization이었다. 이 아이디어의 핵심 가정은 다음과 같다.

1. contractual distribution economics가 advertising cycle보다 안정적일 것.
2. acquisition synergies가 headline multiple을 실제 cash yield로 낮출 것.
3. debt가 equity optionality를 파괴하기 전에 FCF로 빠르게 줄어들 것.
4. 정치광고를 정상화해도 valuation이 충분히 낮을 것.
5. 규제·ownership cap 때문에 생기는 divestiture가 deal economics를 훼손하지 않을 것.

### 5. 실제 전개

2016년 Sinclair revenue는 $2.737bn(+23.3%), operating income $602.9m(+42.6%)로 core/정치광고 쪽은 강했다. 그러나 2017 incentive auction에서 Sinclair가 발표한 gross proceeds는 약 $313m에 불과했고 operations의 material change도 없다고 했다. $2bn optionality는 약 6분의 1 수준으로 크게 빗나갔다.

### 6. 주장별 검증

- **방향:** 원문 기준 Long; raw SQL Short flag는 오류 또는 security-level 분류 미흡이다.
- **사업:** 성장투자 전 18%, 성장투자 후 16% 수준의 FCF yield에 retrans 성장과 2016 정치광고를 기본가치로 두고, 경영진이 언급한 약 $2bn spectrum monetization 가능성을 큰 무료 옵션으로 봤다. spectrum만으로 시총의 약 75% 가치를 주장했다.
- **촉매:** 2016년 Sinclair revenue는 $2.737bn(+23.3%), operating income $602.9m(+42.6%)로 core/정치광고 쪽은 강했다. 그러나 2017 incentive auction에서 Sinclair가 발표한 gross proceeds는 약 $313m에 불과했고 operations의 material change도 없다고 했다. $2bn optionality는 약 6분의 1 수준으로 크게 빗나갔다.
- **밸류에이션/청구권:** 이 아이디어는 core FCF와 event optionality를 섞은 전형적 사례다. core business valuation은 저렴했고 단기 실적도 좋았지만 spectrum을 management estimate로 곧바로 equity value에 더한 부분은 실패했다.
- **반증:** spectrum clearing price, relinquishable MHz, tax/repack cost를 station-by-station로 계산하면 $2bn이 성립하지 않는 경우 optionality는 valuation에 넣지 말아야 한다.
- **사후평가:** 혼합·core 성공 / spectrum 옵션 실패

### 7. 핵심 수치

| 지표 | 값 | 단위 | 근거 |
|---|---:|---|---|
| pre-growth FCF yield | 18 | % | VIC |
| post-growth FCF yield | 16 | % | VIC |
| management spectrum value | 2.0 | USD bn | VIC/management estimate |
| actual auction gross proceeds | 313 | USD m | Sinclair |

### 8. 촉매와 타임라인

| 날짜 | 이벤트 | 의미 |
|---|---|---|
| 2015-08-16 | VIC Long 게시 | FCF + spectrum optionality |
| 2016-02-01 | retrans renewals / political setup | company outlook |
| 2016-12-31 | FY16 results | revenue $2.737bn |
| 2017-02-09 | auction result announced | gross $313m |
| 2017-07-01 | auction proceeds received/restricted | cash realization |
| 2017-12-31 | FY17 results | political comp faded; core remained |

### 9. 반증조건과 놓치기 쉬운 변수

**사전 반증조건:** spectrum clearing price, relinquishable MHz, tax/repack cost를 station-by-station로 계산하면 $2bn이 성립하지 않는 경우 optionality는 valuation에 넣지 말아야 한다.

또한 local TV는 구조적으로 cord-cutting, network fee inflation, audience fragmentation, political cycle, FCC ownership rules, refinancing cost에 노출된다. 과거의 높은 FCF yield가 terminal decline을 반영한 것인지, 아니면 계약수익과 자본배분으로 상쇄 가능한 할인인지 분리해야 한다.

### 10. 재사용 가능한 교훈

**규제 auction optionality는 management headline estimate가 아니라 probability-weighted net proceeds로만 더해야 한다.**

이 아이디어를 다른 기업에 재사용할 때는 단순히 `FCF yield가 높다`는 사실이 아니라, (a) FCF의 반복가능성, (b) debt와 maturity, (c) incremental acquisition/buyback return, (d) 규제 이벤트의 net cash proceeds, (e) 주당가치로 귀속되는 비율을 순서대로 검증해야 한다.

---
# 배치 공통 소스·감사 메모

## 주요 1차자료

- Nexstar 2005 Form 10-K: https://www.sec.gov/Archives/edgar/data/1142417/000119312506055276/d10k.htm
- Nexstar Newport acquisition (2012): https://www.nexstar.tv/nexstar-broadcasting-and-mission-broadcasting-to-acquire-12-television-stations-in-eight-markets-and-inergize-digital-e-media-operations-from-newport-television-llc-for-285-5-million-in-cash-in-an-a/
- Nexstar Q4 2012 results: https://www.nexstar.tv/wp-content/uploads/2015/12/Nexstar-Broadcasting-Group-Q4-2012-Results.pdf
- Nexstar Media General close: https://www.nexstar.tv/nexstar-broadcasting-group-completes-acquisition-of-media-general-creating-nexstar-media-group-the-nations-second-largest-television-broadcaster/
- Nexstar Tribune close (2019-09-19): https://www.nexstar.tv/nexstar_completes_tribune_transaction_2019/
- Nexstar FY2020 results: https://www.nexstar.tv/nexstar-media-group-reports-record-fourth-quarter-net-revenue-of-1377-million/
- Nexstar 2022 buyback authorization: https://www.nexstar.tv/dividend_share_repurchase_authorization_board_declassify_2022/
- Sinclair 2015 Form 10-K: https://www.sec.gov/Archives/edgar/data/912752/000091275216000020/sbgi-20151231x10k.htm
- Sinclair FY2016 results: https://sbgi.net/sinclair-reports-fourth-quarter-2016-financial-results/
- Sinclair spectrum auction result (2017-02-09): https://sbgi.net/sinclair-announces-results-of-spectrum-auction/
- Sinclair 2017 Form 10-K: https://www.sec.gov/Archives/edgar/data/912752/000091275218000006/sbgi-20171231x10k.htm

## 데이터 품질

- 모든 10개 idea_id는 원본 `vic_full_local.db` / `VIC_IDEAS(2).sql` 계열에서 재조회했다.
- raw `is_short`는 10건 모두 true이나, 본문에서 실제 recommendation/security를 직접 판독해 research direction을 교정했다.
- SBGI의 raw company mapping `Diamond Sports`는 issuer entity 오류로 판단해 curated layer에서 Sinclair Broadcast Group으로 교정했다.
- 가격수익률이 원본 DB에 없으므로 인위적으로 만들지 않았다. 대신 사업·증권·촉매 결과를 1차자료로 postmortem했다.
