n, m = map(int, input().split())
coins = [int(input()) for _ in range(n)]
dp = [10001]*(m+1)

dp[0] = 0
# d[m]이 0이면 만들 수 없는 수. d[m]의 최소값을 구하는 것이 목표.
for i in range(n):
    for j in range(coins[i], m+1):
        if dp[j-coins[i]] != 10001: # (i-k)원을 만드는 방법이 존재하는 경우
            dp[j] = min(dp[j], dp[j-coins[i]]+1)

if dp[m] == 10001:
    print(-1)
else:
    print(dp[m])


