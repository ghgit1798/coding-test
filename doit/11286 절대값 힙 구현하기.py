import sys
import heapq
input = sys.stdin.readline

n = int(input())
heap = []
data = list(int(input()) for _ in range(n))
for x in data:
    if x != 0:
        heapq.heappush(heap, (abs(x), x))
    elif x == 0 and heap:
        num = heapq.heappop(heap)
        print(num[1])
    elif x == 0 and not heap:
        print(0)

