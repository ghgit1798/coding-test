# 답안1
n, m, k = map(int, input().split())
num = list(map(int, input().split()))
answer = 0

num = sorted(num)
first = num[-1]
second = num[-2]

for i in range(1, m+1):
    if i % (k+1) == 0:
        answer = answer + second
    else:
        answer = answer + first

print(answer)

# 답안2
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

# 답안3
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


# 0612 복습답안
n, m, k = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort(reverse=True)
n1 = nums[0]
n2 = nums[1]
div = m // (k+1)
res = m % (k+1)
answer = (n1*k+n2)*div + (n1*res)

print(answer)