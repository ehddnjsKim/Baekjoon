# 입력
A = int(input())  # 첫 번째 세 자리 수
B = input()       # 두 번째 세 자리 수 (문자열로 받아 자릿수 분리)

# 출력
print(A * int(B[2]))        # (3) 일의 자리
print(A * int(B[1]))        # (4) 십의 자리
print(A * int(B[0]))        # (5) 백의 자리
print(A * int(B))           # (6) 전체 곱
