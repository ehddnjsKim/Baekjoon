def calculate(a, b):
    print(a + b)   # 덧셈
    print(a - b)   # 뺄셈
    print(a * b)   # 곱셈
    print(a // b)  # 정수 나눗셈 (몫)
    print(a % b)   # 나머지

a, b = map(int, input().split())
calculate(a, b)
