n = int(input())
scary = list(map(int, input().split()))

scary.sort()
cnt = 0
q = []

for i in range(n):
    x = scary[i]
    q.append(x)
    if x <= len(q):
        cnt += 1
        q = []

print(cnt)
