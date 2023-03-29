n, m, k = map(int, input().split())
nums = list(map(int, input().split()))
answer = 0

nums = sorted(nums, reverse=True)
cnt = 0
for i in range(m):
    if cnt == k:
        answer += nums[1]
        cnt = 0
    else:
        answer += nums[0]
        cnt += 1

print(answer)

# 답안2
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

count = int(m/(k+1)*k)
count += m % (k+1)

result = 0
result += (count)*first
result += (m-count) * second

print(result)