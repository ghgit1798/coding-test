n = int(input())
coin = [500, 100, 50, 10]
cnt = 0

print("====start====")

while n != 0:
    for c in coin:
        if n % c == 0:
            cnt += 1
            n = n - n // c

print(cnt)