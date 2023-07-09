n = int(input())
d = [0]*1--1

d[1] = 1
d[2] = 3
for i in range(3, n+1):
    d[i] = (d[i-1] + 2*d[i-2])%796796

print(d[n])


# 0709 복습답안
n = int(input())
dp = [0]*(n+1)
dp[1], dp[2] = 1, 3

for i in range(3, n+1):
    dp[i] = dp[i-1] + 2*(dp[i-2])

print(dp[n]%796796)
