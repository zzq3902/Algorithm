# dp[a][b] -> a번째 자리가 b인 경우 계단 수의 개수

N = int(input())
dp = [[1 for _ in range(10)] for _ in range(N+1)]

for i in range(2, N+1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i-1][1]
        elif j == 9:
            dp[i][j] = dp[i-1][8]
        else:
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]

print(sum(dp[N][1:]) % 1000000000)
