n = int(input())
array = list(map(int, input().split()))

d = [0] * 100

d[0] = array[0]
d[1] = max(array[0], array[1])
for i in range(2, n):
    d[i] = max(d[i-1], d[i-2] + array[i])

print(d[n-1])


# 0629 복습 답안
n = int(input())
graph = list(map(int, input().split()))
dp = [0]*(n)
dp[0] = graph[0]
dp[1] = max(graph[0], graph[1])
answer = 0

for i in range(2, n):
    dp[i] = max(dp[i-1], dp[i-2]+graph[i])

print(dp[n-1])