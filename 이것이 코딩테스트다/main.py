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
