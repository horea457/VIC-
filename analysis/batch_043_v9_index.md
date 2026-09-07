# Batch 043 — V9 Candidate Index

> Batch 003 V9 규칙 적용: 투자시점별 독립 Idea Unit, claim-level C1/C2/... 검증, 실제 성과와 사후검증 중심.

| # | VIC date | ticker | company | raw flag | idea id | source |
|---:|---|---|---|---|---|---|
| 1 | 2000-08-29 22:38:00 | LVLT | Level 3 Comunication  |  | `552a0c54-5417-4cb8-ae6e-e3b5a0079976` | [VIC](https://www.valueinvestorsclub.com/idea/Level_Three_Communications_In/0716564972) |
| 2 | 2001-03-01 22:43:00 | LVLT | Level 3 Comunication  |  | `15f30c2f-a0a7-41f3-b97f-2c7dff55fdd6` | [VIC](https://www.valueinvestorsclub.com/idea/Level_3_Communications_Inc./7923868895) |
| 3 | 2002-04-19 11:36:00 | LVLT | Level 3 Comunication  |  | `6c53c36e-b9ee-4b7d-bc12-9eb3f7c84886` | [VIC](None) |
| 4 | 2003-03-17 10:53:00 | LVLT | Level 3 Comunication  |  | `6c4d3871-880a-45e2-8fc6-3706b125ddeb` | [VIC](https://www.valueinvestorsclub.com/idea/Level_3_Bank_Debt/9040413468) |
| 5 | 2004-12-30 16:21:00 | LVLT | Level 3 Comunication  |  | `107fd97a-4482-4f35-af20-b8f2ee3e325f` | [VIC](https://www.valueinvestorsclub.com/idea/Level_3/2370352061) |
| 6 | 2007-11-11 16:46:00 | LVLT | Level 3 Comunication  |  | `44312f7c-f1b7-4f46-b92b-dc8d08c79832` | [VIC](https://www.valueinvestorsclub.com/idea/Level_3_Communications/1821042905) |
| 7 | 2011-10-11 18:37:00 | LVLT | Level 3 Comunication  |  | `e32af27d-688a-4ce1-8cf4-f5df3499ae50` | [VIC](None) |
| 8 | 2017-07-29 09:41:00 | LVLT | Level 3 Comunication  |  | `3df8999b-4ddc-4eea-bc10-d0c9949e3170` | [VIC](https://www.valueinvestorsclub.com/idea/LEVEL_3_COMMUNICATIONS_INC/3863570505) |
| 9 | 2005-12-20 17:25:00 | NXST | NEXSTAR BROADCASTING GROUP  |  | `7b8c3ad5-3249-4756-901a-9d267e0a8a4b` | [VIC](https://www.valueinvestorsclub.com/idea/Nexstar_Broadcasting/5237264040) |
| 10 | 2011-12-14 12:58:00 | NXST | NEXSTAR BROADCASTING GROUP  |  | `52de43f8-b373-4daa-bbf9-6655b52da336` | [VIC](https://www.valueinvestorsclub.com/idea/NEXSTAR_BROADCASTING_GROUP/2624763498) |

## 작업 규칙

- raw SQL flag는 보존하고 실제 VIC 방향/security는 별도 검증한다.
- 동일 회사라도 게시일이 다르면 별도 canonical idea 파일로 분리한다.
- 각 Idea는 회사/산업/돈의 흐름을 설명한 뒤 C1/C2/... 개별 thesis로 분해한다.
- 각 Claim마다 당시 근거, 숨은 가정, 사전 반증조건, 실제 결과, 판정을 기록한다.
- 목표가 IRR보다 실제 게시가격→실제 후속가격/exit 기준 수익률과 IRR을 우선한다.
- Business / valuation / catalyst / timing / security-selection을 별도 판정한다.
