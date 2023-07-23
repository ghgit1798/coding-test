import sys
from collections import deque
input = sys.stdin.readline

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
INF = int(1e9)

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

distance = [INF]*(n+1)
distance[x] = 0

q = deque()
q.append(x)
while q:
    now = q.popleft()
    # 현재 도시에서 이동할 수 있는 모든 도시를 확인
    for next_node in graph[now]:
        # 아직 방문하지 않은 도시라면
        if distance[next_node] == INF:
            # 최단 거리 갱신
            distance[next_node] = distance[now]+1
            q.append(next_node)

check = False
for i in range(1, n+1):
    if distance[i] == k:
        print(i)
        check = True

if check == False:
    print(-1)



