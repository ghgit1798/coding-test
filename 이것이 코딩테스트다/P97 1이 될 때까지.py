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
