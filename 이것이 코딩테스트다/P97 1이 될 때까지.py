n, k = map(int, input().split())
cnt = 0

while n != 1:
    if n % k == 0:
        n = n / k
    else:
        n = n - 1
    cnt += 1

print(cnt)

# 답안 2 : 최적화 > 1을 한 번에 빼기
n, k = map(int, input().split())
cnt = 0

while n != 1:
    if n % k == 0:
        n = n / k
        cnt += 1
    else:   # 나누어 떨어지지 않으면 1을 한 번에 빼기
        target = (n // k) * k
        cnt += (n - target)
        n = target

print(cnt)


# 240911
import sys

input = sys.stdin.readline

answer = 0

n, k = map(int, input().split())

while True:
    if n == 1:
        break
    if n % k == 0:
        n = n//k
    else:
        n = n-1
    answer += 1

print(answer)

# 240911 최적화 답안
import sys

input = sys.stdin.readline

answer = 0

n, k = map(int, input().split())

while True:
    target = (n//k) * k # n = 17, target = 16 || n = 4, target = 4
    answer += (n-target) # answer = 1 || answer = 1
    if n < k: # n = 17 || # n = 4
        break
    n //= k # n = 4 || n = 1
    answer += 1 # answer = 2 || answer = 3

answer += (n-1) # 마지막 남은 수에 대해 1씩 빼기 : 3이면 2빼서 1로 만들기
print(answer)
