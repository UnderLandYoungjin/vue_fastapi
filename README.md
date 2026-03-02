https://cafe.naver.com/f-e/cafes/30977017/menus/25?viewType=L
<img width="1405" height="688" alt="image" src="https://github.com/user-attachments/assets/aaa6d6eb-e159-4de1-ad25-95b7ad02da0f" />

---


<img width="1080" height="1988" alt="image" src="https://github.com/user-attachments/assets/05f9868d-db44-4495-8e50-03b80bb0f280" />
https://cafe.naver.com/f-e/cafes/30977017/articles/690?boardtype=C&referrerAllArticles=true&page=9

---


https://cafe.naver.com/f-e/cafes/30977017/articles/692?boardtype=I&userDisplay=20&menuid=25&referrerAllArticles=false&page=2

<img width="1229" height="841" alt="image" src="https://github.com/user-attachments/assets/c8a26cba-c44e-49d4-929a-b3ed872efb55" />
<img width="1343" height="843" alt="image" src="https://github.com/user-attachments/assets/5107384a-f075-4619-a0c1-3c40a8eb14ed" />
<img width="1268" height="903" alt="image" src="https://github.com/user-attachments/assets/6847e23a-b89c-4381-a93d-2179faef4e44" />


---
---
---

---


# 📌 산업 시스템을 프로그래밍으로 구현하기

> **강의 대상:** AI소프트웨어융합과 비학위 과정  
> **기준일:** 2026년 3월 2일  
> **목표:** 실제 산업 현장에서 사용하는 시스템의 구조와 작동 원리를 프로그래밍으로 직접 구현해 본다

---

## 🎯 이 수업이 말하는 것

> **"이 수업은 버튼 만드는 연습이 아니다."**  
> 여러분이 만드는 것은 글로벌 기업이 수백억 원을 들여 구축한 산업 시스템의 **축소판(Prototype)** 이다.

코딩을 배우는 이유는 단순히 코드를 짜는 능력이 아닙니다.  
**"현실 문제를 시스템으로 해결하는 사람"** 이 되는 것이 목표입니다.

---

## 🗺️ 수업 전체 구조

```
산업 시스템 이해
     ↓
글로벌 상용 솔루션 분석
     ↓
핵심 기능 추출
     ↓
학생 수준 프로젝트로 변환
     ↓
실제 구현 + GitHub 포트폴리오화
```

---

# 1️⃣ 스마트 팩토리 · MES 시스템

## 📌 산업 현황

제조업의 디지털화(Industry 4.0)와 함께, 현대 제조 시스템은 **MES(Manufacturing Execution System)** 로 진화했습니다.

| 기존 방식 | MES 방식 |
|----------|---------|
| 엑셀로 수동 집계 | 실시간 자동 수집 |
| 불량 발생 후 대응 | 예지보전으로 사전 차단 |
| 부서별 데이터 분리 | ERP 완전 통합 |
| 월말 생산 보고 | 실시간 OEE 모니터링 |

### 🔑 핵심 기능 (End-to-End MES)

- **생산계획 수립** – 주문 기반 생산 일정 자동 산출
- **작업지시 발행** – 라인별 작업 내용 전달
- **설비 상태 모니터링** – PLC 데이터 실시간 수집
- **불량 데이터 수집** – 불량 유형·수량·원인 기록
- **OEE 실시간 계산** – 가동률 × 성능률 × 양품률
- **재고 자동 반영** – 생산 완료 즉시 재고 업데이트
- **ERP 연동** – SAP, Oracle 등과 데이터 동기화
- **설비 예지보전** – 이상 패턴 사전 감지

> **OEE(Overall Equipment Effectiveness)** = 가동률 × 성능률 × 양품률  
> 세계 평균 OEE ≈ 60%, 우수 기업 ≈ 85% 이상

---

## 🌍 글로벌 솔루션 사례

### 🔹 Siemens – Opcenter / Teamcenter

| 항목 | 내용 |
|------|------|
| 주요 기능 | 설비 데이터 실시간 수집, 생산 추적(Traceability), 품질 데이터 자동 저장, 디지털 트윈 연계, ERP 완전 연동 |
| 적용 산업 | 자동차, 반도체, 글로벌 대형 제조 |
| 기술 스택 | OPC-UA, MindSphere IoT, SQL DB |

### 🔹 Rockwell Automation – FactoryTalk

| 항목 | 내용 |
|------|------|
| 주요 기능 | PLC 통합, 생산량 실시간 집계, 설비 이상 감지, 품질 이력 관리 |
| 특징 | Allen-Bradley PLC와 완전 통합, 북미 제조업 표준 플랫폼 |

---

## 🎓 학생 프로젝트: **Mini MES 시스템**

### 📋 구현 기능 목록

| 기능 | 설명 | 난이도 |
|------|------|--------|
| 작업지시 등록 화면 | 제품명, 목표수량, 담당라인 입력 | ⭐⭐ |
| 생산 실적 입력 | 시간대별 생산량 수기 입력 | ⭐⭐ |
| 불량률 자동 계산 | `불량수 / 총생산수 × 100` | ⭐⭐ |
| OEE 계산 모듈 | 가동시간, 성능률, 양품률 입력 → 자동 산출 | ⭐⭐⭐ |
| 설비 상태 모니터링 | 가동/정지/고장 상태 표시 (색상 구분) | ⭐⭐⭐ |
| 일일 생산 리포트 출력 | 날짜별 집계 → PDF 또는 Excel 출력 | ⭐⭐⭐ |

### 💡 핵심 코드 예시 (Python)

```python
class ProductionLine:
    def __init__(self, line_id, target_qty):
        self.line_id = line_id
        self.target_qty = target_qty
        self.produced_qty = 0
        self.defect_qty = 0
        self.downtime_min = 0  # 정지 시간(분)

    def add_production(self, qty, defects=0):
        self.produced_qty += qty
        self.defect_qty += defects

    def defect_rate(self):
        if self.produced_qty == 0:
            return 0.0
        return round(self.defect_qty / self.produced_qty * 100, 2)

    def oee(self, shift_min=480):
        """
        OEE = 가동률 × 성능률 × 양품률
        shift_min: 근무시간(분), 기본 8시간=480분
        """
        availability = (shift_min - self.downtime_min) / shift_min
        performance = self.produced_qty / self.target_qty if self.target_qty > 0 else 0
        quality = 1 - (self.defect_qty / self.produced_qty) if self.produced_qty > 0 else 0
        return round(availability * performance * quality * 100, 2)


# 사용 예시
line1 = ProductionLine(line_id="A-01", target_qty=500)
line1.add_production(qty=430, defects=12)
line1.downtime_min = 30

print(f"불량률: {line1.defect_rate()}%")
print(f"OEE: {line1.oee()}%")
```

### 🚀 확장 트랙 (심화)

- Modbus TCP 시뮬레이터 연동 → PLC 데이터 수신
- OpenCV/MediaPipe → Vision 검사 결과 자동 DB 저장
- 시계열 데이터 → Matplotlib 실시간 그래프
- SQLite / PostgreSQL → 생산 이력 데이터베이스

---

# 2️⃣ 금융 · 핀테크 시스템

## 📌 산업 현황

현대 금융 시스템은 단순 계좌 관리를 넘어 **Real-Time Risk & Transaction Intelligence** 수준으로 발전했습니다.

| 전통 금융 | 핀테크 |
|---------|--------|
| 점포 방문 처리 | 초당 수천 건 자동 처리 |
| 사람이 이상 거래 감지 | AI 기반 실시간 사기 탐지 |
| 월말 정산 | 즉시 자동 정산 |
| 직관적 신용 평가 | 머신러닝 신용 모델 |

### 🔑 핵심 기능

- 실시간 거래 처리 및 원장 반영
- 이상거래 탐지 (FDS: Fraud Detection System)
- AI 신용 평가 모델
- 리스크 분석 및 포트폴리오 시뮬레이션
- 자동 회계 분개 처리

---

## 🌍 글로벌 솔루션 사례

### 🔹 FIS Global

| 항목 | 내용 |
|------|------|
| 규모 | 초당 수천 건 금융 거래 처리 |
| 주요 기능 | AI 기반 사기 탐지, 리스크 점수 자동 산출, 멀티채널 결제 통합 |

### 🔹 카카오페이

| 항목 | 내용 |
|------|------|
| 특징 | 간편결제 + 신용 분석 + 자동 정산 원스톱 처리 |
| 기술 | MSA(마이크로서비스), Kafka 실시간 이벤트 처리 |

---

## 🎓 학생 프로젝트: **소상공인 손익 분석 시스템**

### 📋 구현 기능 목록

| 기능 | 설명 | 난이도 |
|------|------|--------|
| 매출 입력 | 일별/월별 매출 등록 | ⭐⭐ |
| 비용 구조 입력 | 고정비·변동비 분류 입력 | ⭐⭐ |
| 손익 자동 계산 | 매출 - 비용 = 순이익 자동 산출 | ⭐⭐ |
| 월별 그래프 출력 | Matplotlib / Chart.js 시각화 | ⭐⭐⭐ |
| 현금 흐름 예측 | 이동평균 기반 다음 달 예측 | ⭐⭐⭐⭐ |

### 💡 핵심 코드 예시 (Python)

```python
class FinancialAnalyzer:
    def __init__(self):
        self.records = []  # {'month': 'YYYY-MM', 'revenue': 0, 'fixed_cost': 0, 'variable_cost': 0}

    def add_record(self, month, revenue, fixed_cost, variable_cost):
        self.records.append({
            'month': month,
            'revenue': revenue,
            'fixed_cost': fixed_cost,
            'variable_cost': variable_cost
        })

    def net_profit(self, record):
        return record['revenue'] - record['fixed_cost'] - record['variable_cost']

    def profit_margin(self, record):
        if record['revenue'] == 0:
            return 0.0
        return round(self.net_profit(record) / record['revenue'] * 100, 2)

    def summary(self):
        for r in self.records:
            profit = self.net_profit(r)
            margin = self.profit_margin(r)
            status = "흑자✅" if profit >= 0 else "적자❌"
            print(f"[{r['month']}] 매출: {r['revenue']:,}원 | 순이익: {profit:,}원 | 이익률: {margin}% | {status}")

    def moving_average_forecast(self, n=3):
        """최근 n개월 이동평균으로 다음달 매출 예측"""
        revenues = [r['revenue'] for r in self.records[-n:]]
        if len(revenues) < n:
            return None
        forecast = sum(revenues) / n
        print(f"\n📈 다음 달 매출 예측 (최근 {n}개월 이동평균): {forecast:,.0f}원")
        return forecast


# 사용 예시
fa = FinancialAnalyzer()
fa.add_record('2026-01', revenue=5_200_000, fixed_cost=1_500_000, variable_cost=2_100_000)
fa.add_record('2026-02', revenue=4_800_000, fixed_cost=1_500_000, variable_cost=1_900_000)
fa.add_record('2026-03', revenue=5_600_000, fixed_cost=1_500_000, variable_cost=2_300_000)
fa.summary()
fa.moving_average_forecast(n=3)
```

### 🚀 확장 트랙 (심화)

- scikit-learn → 선형회귀 기반 매출 예측 모델
- 카드 수수료 계산 모듈 (업종별 수수료율 적용)
- 세금 자동 계산 (부가세, 소득세 구간 적용)
- Flask/FastAPI → 웹 대시보드로 확장

---

# 3️⃣ 물류 · 스마트 배송 시스템

## 📌 산업 현황

현대 물류 플랫폼은 **AI Logistics Optimization Platform** 수준으로, 단순 택배 관리를 넘어섰습니다.

| 전통 물류 | 스마트 물류 |
|---------|----------|
| 수기 송장 작성 | 자동 송장 생성 + 바코드 발행 |
| 전화 배송 문의 | 실시간 GPS 추적 |
| 배차 담당자 경험 의존 | AI 경로 최적화 |
| 수작업 창고 분류 | 자동 컨베이어 + 자동 분류기 |

### 🔑 핵심 기능

- 실시간 GPS 위치 추적
- 자동 경로 최적화 (TSP: Traveling Salesman Problem)
- 창고 자동 분류 (Zone 별 자동 배정)
- 배송비 자동 계산 (거리 × 중량)
- SLA(서비스 수준 협약) 관리

---

## 🌍 글로벌 솔루션 사례

### 🔹 DHL

| 항목 | 내용 |
|------|------|
| 특징 | 글로벌 220개국 물류 통합, AI 경로 최적화, 드론 배송 파일럿 |

### 🔹 CJ대한통운

| 항목 | 내용 |
|------|------|
| 특징 | 자동 분류 시스템(소터), 실시간 택배 상태 추적, 지역별 통계 대시보드 |

---

## 🎓 학생 프로젝트: **택배 추적 + 배송비 계산 시스템**

### 📋 구현 기능 목록

| 기능 | 설명 | 난이도 |
|------|------|--------|
| 송장 등록 | 발송인, 수신인, 품목, 중량 입력 | ⭐⭐ |
| 상태 변경 로직 | 접수→집화→간선이동→배달중→완료 | ⭐⭐⭐ |
| 배송비 자동 계산 | 거리 + 중량 기반 요금 산출 | ⭐⭐⭐ |
| 지역별 매출 통계 | 발송지/수신지별 건수·금액 집계 | ⭐⭐⭐ |
| 관리자 대시보드 | 전체 현황 테이블 + 상태별 필터 | ⭐⭐⭐ |

### 💡 핵심 코드 예시 (Python)

```python
from datetime import datetime
from enum import Enum

class DeliveryStatus(Enum):
    REGISTERED   = "접수"
    PICKED_UP    = "집화"
    IN_TRANSIT   = "간선이동"
    OUT_FOR_DEL  = "배달중"
    DELIVERED    = "배달완료"

class Parcel:
    # 기본 요금표 (중량 구간별, 단위: 원)
    WEIGHT_RATE = {1: 3000, 3: 4000, 5: 5000, 10: 7000, 20: 10000}

    def __init__(self, tracking_no, sender, receiver, weight_kg, distance_km):
        self.tracking_no  = tracking_no
        self.sender       = sender
        self.receiver     = receiver
        self.weight_kg    = weight_kg
        self.distance_km  = distance_km
        self.status       = DeliveryStatus.REGISTERED
        self.history      = [(DeliveryStatus.REGISTERED, datetime.now())]

    def update_status(self, new_status: DeliveryStatus):
        self.status = new_status
        self.history.append((new_status, datetime.now()))
        print(f"[{self.tracking_no}] 상태 변경 → {new_status.value}")

    def calc_fee(self):
        """중량 구간 + 거리 할증 계산"""
        base_fee = 3000
        for limit, fee in sorted(self.WEIGHT_RATE.items()):
            if self.weight_kg <= limit:
                base_fee = fee
                break
        else:
            base_fee = self.WEIGHT_RATE[20]

        distance_surcharge = (self.distance_km // 100) * 500  # 100km 초과마다 500원
        return base_fee + distance_surcharge

    def print_info(self):
        print(f"\n📦 송장번호: {self.tracking_no}")
        print(f"   발송인: {self.sender} → 수신인: {self.receiver}")
        print(f"   중량: {self.weight_kg}kg | 거리: {self.distance_km}km")
        print(f"   배송비: {self.calc_fee():,}원")
        print(f"   현재상태: {self.status.value}")


# 사용 예시
p = Parcel("KR20260302001", "김부산", "이서울", weight_kg=2.5, distance_km=450)
p.print_info()
p.update_status(DeliveryStatus.PICKED_UP)
p.update_status(DeliveryStatus.IN_TRANSIT)
p.update_status(DeliveryStatus.OUT_FOR_DEL)
p.update_status(DeliveryStatus.DELIVERED)
```

### 🚀 확장 트랙 (심화)

- Kakao Map / Google Maps API → 실시간 지도 배송 경로 표시
- TSP 알고리즘 → 배송 순서 최적화
- Tkinter / PyQt → GUI 관리자 화면 구현
- REST API (Flask) → 모바일 앱과 연동 구조 체험

---

# 📊 수업 전체 난이도 및 취업 연계성

| 분야 | 프로젝트명 | 난이도 | 취업 연계 분야 | 핵심 기술 |
|------|----------|--------|-------------|----------|
| 스마트팩토리 | Mini MES | ★★★★ | 제조 IT, 스마트팩토리 엔지니어 | OOP, DB, 실시간 처리 |
| 금융·핀테크 | 손익 분석 시스템 | ★★★ | SI, 핀테크 개발자 | 수치 계산, 예측 모델 |
| 물류 | 택배 추적 시스템 | ★★★ | 물류 SI, 플랫폼 개발 | 상태 관리, 알고리즘 |

---

# 🔎 확장 가능 트랙

## 기초 → 심화 로드맵

```
Python 기초 OOP
     ↓
SQLite DB 연동 (데이터 영속성)
     ↓
Flask/FastAPI REST API 구축
     ↓
HTML/JS 프론트엔드 대시보드
     ↓
머신러닝 예측 모델 탑재
     ↓
GitHub 포트폴리오 완성
```

## 융합 프로젝트 아이디어

| 주제 | 융합 기술 |
|------|---------|
| AI 비전 품질검사 + MES | OpenCV + MediaPipe + DB |
| 스마트 재고 관리 | Barcode + DB + 자동 발주 알고리즘 |
| 실시간 배송 대시보드 | GPS API + 지도 시각화 + WebSocket |
| 소상공인 AI 매출 예측 | pandas + scikit-learn + 웹 배포 |

---

# ✅ 수업 마무리 메시지

> **"코드 한 줄이 공장 하나를 움직이고,**  
> **알고리즘 하나가 수천 건의 물류를 최적화한다."**

여러분이 이 수업에서 만드는 시스템은 단순한 실습 과제가 아닙니다.  
실제 산업 시스템의 **핵심 로직을 이해하고 직접 구현한 경험**, 그 자체가 여러분의 가장 강력한 포트폴리오입니다.

---

*© 2026 AI소프트웨어융합과 강의자료 | 부산*
