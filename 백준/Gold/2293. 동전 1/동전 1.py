# dp를 이용하여 해결한다

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

dp = [0 for _ in range(k+1)]
dp[0] = 1
for i in range(n):
    for j in range(1, k+1):
        if coins[i] <= j:
            dp[j] += dp[j-coins[i]]


print(dp[-1])