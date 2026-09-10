# Adaptec / Emulex — 2004-06-15 VIC Pair Trade

> **Security audit:** raw SQL은 Short지만 실제 아이디어는 **Long Adaptec (ADPT) / Short Emulex (ELX)** pair trade.
> **Research as-of:** 2026-09-10.

## 0. Idea Snapshot

| 항목 | 내용 |
|---|---|
| 게시일 / 작성자 | 2004-06-15 / hbomb5 |
| 실제 포지션 | **Long ADPT / Short ELX** |
| 핵심 산업 thesis | iSCSI / storage-over-IP 성장, Fibre Channel HBA economics 압박 |
| ADPT EV | 약 **$445m** |
| ADPT unlevered FCF | 약 **$47m** |
| ADPT EV/FCF | 약 **9.4x** |
| ADPT value | **$7.90/share** |
| 실제 ADPT FY05→FY07 revenue | **$402.5m → $255.2m** |
| FY05~06 operating losses | 합계 약 **$188.4m** |
| 최종 판정 | **ADPT Long leg 실패 / 기술방향 일부 맞아도 value capture 실패 / exact pair IRR 미복원** |

> **결론:** 이 아이디어는 “iSCSI가 성장한다”는 기술 방향과 “그 성장을 누가 경제적 가치로 가져가는가”를 연결한 pair였다. 문제는 Adaptec이 그 수혜를 충분히 포착하지 못했다는 점이다. 후속 실적에서 revenue와 gross margin이 크게 악화됐다. 기술트렌드를 맞히는 것과 수혜기업을 맞히는 것은 별개의 문제다.

---

## 1. Pair의 산업논리

당시 enterprise storage connectivity에는:
- Fibre Channel
- SCSI
- Ethernet/IP
- emerging iSCSI

가 경쟁.

원문은 iSCSI shipments가 2004 초 약 **40% QoQ** 성장하는 등 storage-over-IP가 빠르게 침투한다고 봤다.

### Long ADPT
Adaptec은:
- storage controller know-how
- channel/OEM relationships
- iSCSI products
- 큰 net cash

를 가지고 있어 저평가된 수혜주라고 봄.

### Short ELX
Emulex는 Fibre Channel HBA economics 의존도가 높아:
- iSCSI substitution
- pricing pressure
- high margins normalization

에 취약하다고 판단.

---

## 2. ADPT valuation

원문 FY04 기준:
- market cap ~$845m
- cash + marketable securities ~$663m
- debt ~$264m
- EV ~$445m
- EBITDA ~$65m
- unlevered FCF ~$47m

따라서:
**EV/FCF ~9.4x**.

writer value:
- $0.43 FCF/share × 10x = $4.30
- net cash ~$3.60/share
- 합계 **$7.90/share**

즉 technology upside 없이도 cheap하다는 구조.

---

## 3. Hidden Assumptions

1. iSCSI growth가 ADPT product share로 연결.
2. ADPT legacy revenue decline보다 new products가 빠르게 성장.
3. cash가 value-destructive R&D/M&A로 소진되지 않음.
4. ELX의 FC economics는 실제로 압박.
5. pair beta/industry exposure가 충분히 hedge됨.

가장 중요한 1·2가 실패했다.

---

## 4. 실제 Adaptec outcome

후속 공식 proxy에 따르면:
- net revenue **$402.5m FY05 → $255.2m FY07**
- gross margin 약 **40% → 32%**
- FY05~FY06 operating losses 합계 약 **$188.4m**

즉 iSCSI라는 end-market narrative와 별개로 Adaptec 자체의:
- product execution
- competitive positioning
- operating leverage

가 무너졌다.

---

## 5. Claim Map

### C1. storage-over-IP / iSCSI grows — **방향상 성공**
기술 흐름 자체는 맞음.

### C2. ADPT captures that growth — **강한 실패**
legacy decline과 execution 문제를 상쇄 못함.

### C3. cheap cash-adjusted valuation protects Long — **실패**
cash는 operating deterioration을 막지 못함.

### C4. ELX is the better Short hedge — **별도 역사복원 필요**
exact pair return은 ELX leg까지 함께 복원해야 함.

---

## 6. Pair trade의 핵심 오류

**technology winner ≠ stock winner**.

새 기술이 커져도 value capture는:
- IP ownership
- distribution
- OEM qualification
- cost structure
- switching costs
- competitive intensity

에 따라 달라진다.

또 Long과 Short가 같은 산업이면 pair가 market-neutral처럼 보여도 **company-specific execution risk는 hedge되지 않는다.**

---

## 7. 재사용 체크리스트

1. 테마를 맞힌 뒤 value-capture chain을 그린다.
2. 신기술 revenue가 legacy cannibalization보다 큰지 본다.
3. cash-rich tech value trap은 burn rate를 본다.
4. pair trade는 Long/Short 각 leg의 독립 thesis를 저장한다.
5. exact pair IRR은 두 leg의 entry/exit/borrow를 모두 복원한다.
6. “cheap + right theme”를 moat로 착각하지 않는다.

### 한 문장 교훈
> **기술의 방향을 맞히는 것보다 그 기술에서 누가 돈을 버는지를 맞히는 것이 훨씬 어렵다. 테마가 맞아도 수혜기업 선택이 틀리면 투자논지는 실패한다.**

## 8. Sources

1. VIC original / uploaded SQL, 2004-06-15.
2. Adaptec activist proxy / historical operating data: https://www.sec.gov/Archives/edgar/data/709804/000119380507002221/e602548_prec14a-adaptec.htm
