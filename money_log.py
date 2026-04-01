# 2026-04-01 지출 데이터
expenses = [
    {"item": "시내버스", "amount": 1550},
    {"item": "아메리카노", "amount": 2000}
]

# 실제로 계산을 수행하는 코드
total = sum(expense["amount"] for expense in expenses)

# 결과 출력
print(f"오늘의 총 지출 합계는 {total}원입니다.")
