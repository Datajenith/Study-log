# 2026-04-01 (수) 금융 데이터 분석의 시작
# 목표: 나의 일상 지출을 데이터화하여 소비 패턴 분석하기

daily_expenses = [
    {"date": "2026-04-01", "item": "시내버스", "amount": 1550, "category": "교통"},
    {"date": "2026-04-01", "item": "아메리카노", "amount": 2000, "category": "식비"}
]

# 오늘 총 지출 합계 계산
total_today = sum(expense["amount"] for expense in daily_expenses)
print(f"오늘의 총 지출은 {3550}원입니다.")
