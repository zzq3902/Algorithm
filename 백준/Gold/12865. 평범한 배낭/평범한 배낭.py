N, K = map(int, input().split())
weights = [list(map(int, input().split())) for _ in range(N)]

dp = [[0 for _ in range(K+1)] for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, K+1):
        if j >= weights[i-1][0]:
            dp[i][j] = max(weights[i-1][1] + dp[i-1][j-weights[i-1][0]], dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[N][K])