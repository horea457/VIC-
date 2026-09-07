# Batch 044 — V9 Candidate Index

> Batch 003 V9 규칙 적용: 투자시점별 독립 Idea Unit, claim-level C1/C2/... 검증, 실제 성과와 사후검증 중심.

| # | VIC date | ticker | company | raw flag | idea id | source |
|---:|---|---|---|---|---|---|
| 1 | 2012-08-26 14:11:00 | NXST | NEXSTAR BROADCASTING GROUP  | Short | `71436938-3f4b-4d1d-9825-afe818a2f4d7` | source link missing |
| 2 | 2016-01-29 11:53:00 | NXST | NEXSTAR BROADCASTING GROUP  | Short | `924b250f-5703-4a82-8537-fac2a187abd1` | [VIC](https://www.valueinvestorsclub.com/idea/NEXSTAR_BROADCASTING_GROUP_NXST/2939181073) |
| 3 | 2017-08-12 10:42:00 | NXST | NEXSTAR BROADCASTING GROUP  | Short | `1b8faf06-08ca-4b27-b723-641fee88d15f` | [VIC](https://www.valueinvestorsclub.com/idea/NEXSTAR_MEDIA_GROUP/4879434468) |
| 4 | 2018-04-23 10:55:00 | NXST | NEXSTAR BROADCASTING GROUP  | Short | `dd7f83ea-6590-4028-9742-84d0cdffda86` | [VIC](https://www.valueinvestorsclub.com/idea/NEXSTAR_MEDIA_GROUP/3733286651) |
| 5 | 2020-03-12 19:48:00 | NXST | NEXSTAR BROADCASTING GROUP  | Short | `f91c8f1f-4a84-4eab-ab51-03068d3b0b2b` | [VIC](https://www.valueinvestorsclub.com/idea/NEXSTAR_MEDIA_GROUP/2843489144) |
| 6 | 2021-09-20 21:38:00 | NXST | NEXSTAR BROADCASTING GROUP  | Short | `585159f9-193f-40f6-aafa-3454b889e2fa` | source link missing |
| 7 | 2002-06-04 13:57:00 | PLUS | ePLUS  | Long | `16577e38-4933-4db0-892e-fa5b9fdd7d79` | [VIC](https://www.valueinvestorsclub.com/idea/ePlus_Inc/1076596755) |
| 8 | 2004-12-23 22:17:00 | PLUS | ePLUS  | Long | `09cb4b70-533d-435e-8566-be6203f98c1b` | [VIC](https://www.valueinvestorsclub.com/idea/ePlus/7455315813) |
| 9 | 2007-05-09 16:14:00 | PLUS | ePLUS  | Short | `98c3017f-e2f5-4a57-8e98-ee0ebac34d63` | source link missing |
| 10 | 2007-11-14 13:10:00 | PLUS | ePLUS  | Short | `f04f83bb-ff87-4e97-981c-05be168e60c6` | source link missing |

## 작업 규칙

- raw SQL flag는 보존하고 실제 VIC 방향/security는 별도 검증한다.
- 동일 회사라도 게시일이 다르면 별도 canonical idea 파일로 분리한다.
- 각 Idea는 회사/산업/돈의 흐름을 설명한 뒤 C1/C2/... 개별 thesis로 분해한다.
- 각 Claim마다 당시 근거, 숨은 가정, 사전 반증조건, 실제 결과, 판정을 기록한다.
- 목표가 IRR보다 실제 게시가격→실제 후속가격/exit 기준 수익률과 IRR을 우선한다.
- Business / valuation / catalyst / timing / security-selection을 별도 판정한다.
