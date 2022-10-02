from collections import deque
N, L = map(int, input().split())
mydeque = deque()
now = list(map(int, input().split()))

for i in range(N):
    while mydeque and mydeque[-1][1] > now[i]:
        mydeque.pop()
    mydeque.append((i, now[i]))
    if mydeque[0][0] <= i-L:
        mydeque.popleft()
    print(mydeque[0][1], end=' ')