n, m = map(int, input().split())
array = []
for i in range(n):
    array.append(int(input()))

d = [10001] * (m+1)

d[0] = 0
for i in range(n):
    for j in range(array[i], m+1):
        if d[j-array[i]] != 10001:
            d[j] = min(d[j], d[j-array[i]]+1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])

# 0629 복습 답안
n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]
arr = sorted(arr)
dp = [99999]*(10001)
for coin in arr:
    dp[coin] = 1

for i in range(1, m+1):
    for coin in arr:
        if i - coin >= 0 and dp[i-coin] != 99999:
            dp[i] = min(dp[i], dp[i-coin]+1)

if dp[m] != 99999:
    print(dp[m])
else:
    print(-1)
