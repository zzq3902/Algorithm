# 1. 두 숫자를 입력받는다.
# 2. 각 숫자를 거꾸로 바꾼 후, 비교한다.

a, b = map(int, input().split())

a = 100 * (a % 10) + 10 * ((a // 10) % 10) + a // 100
b = 100 * (b % 10) + 10 * ((b // 10) % 10) + b // 100
print(a if a > b else b)
