import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
nums = list(map(int, input().split()))

nums.sort()

cnt = 0
sum = 0
i, j = 0,0

while i < n:
    if sum == m:
        cnt += 1
        sum += nums[j]
        j += 1
    elif sum > m:
        sum -= nums[i]
        i += 1
    else:
        sum += nums[j]
        j += 1

print(cnt)