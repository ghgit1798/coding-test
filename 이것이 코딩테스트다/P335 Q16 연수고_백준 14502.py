import sys, copy
from collections import deque
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dx = [0,0,-1,1]     # 동서남북
dy = [1,-1,0,0]

virus = []
empty = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            virus.append((i, j))
        if graph[i][j] == 0:
            empty.append((i, j))

cases = list(combinations(empty, 3))

# 바이러스 전파한다.
def activate(graph, a, b):
    q = deque()
    q.append((a, b))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = 2
                q.append((nx, ny))

# 빈칸을 카운트한다.
def get_sum(graph):
    cnt = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                cnt += 1
    return cnt

answer = 0
for walls in cases:
    temp = copy.deepcopy(graph)
    for wall in walls:
        ex, ey = wall
        temp[ex][ey] = 1
    for data in virus:
        vx, vy = data
        activate(temp, vx, vy)
    result = get_sum(temp)
    answer = max(answer, result)

print(answer)