# 두 자연수를 입력받아 공백 기준으로 분리
a, b = input().split()

# 문자열을 정수로 변환
a = int(a)
b = int(b)

# 각 연산 결과 출력
print(a + b)   # 덧셈
print(a - b)   # 뺄셈
print(a * b)   # 곱셈
print(a // b)  # 나눗셈 (몫)
print(a % b)   # 나머지
