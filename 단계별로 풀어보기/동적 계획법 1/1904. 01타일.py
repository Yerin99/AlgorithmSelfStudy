N = int(input())
dp = dict()
dp[1] = 1
dp[2] = 2

if N >= 3:
    for i in range(3, N+1):
        dp[i] = (dp[i-1] + dp[i-2]) % 15746

print(dp[N])
