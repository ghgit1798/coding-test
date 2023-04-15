n, k = map(int, input().split())
cnt = 0

while n != 1:
    if n % k == 0:
        n = n / k
        cnt += 1
    else:
        target = (n // k) * k
        cnt += (n - target)
        n = target

print(cnt)