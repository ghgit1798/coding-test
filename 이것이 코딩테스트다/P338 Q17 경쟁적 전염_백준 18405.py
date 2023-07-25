from collections import deque

n, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
ts, tx, ty = map(int, input().split())

data = []

for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            data.append([graph[i][j], 0, i, j])

data.sort()
q = deque(data)
dx = [0,0,1,-1]
dy = [1,-1,0,0]

while q:
    virus, s, x, y = q.popleft()
    if s == ts:
        break
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if nx<0 or ny<0 or nx>=n or ny>=n:
            continue
        if graph[nx][ny] == 0:
            graph[nx][ny] = virus
            q.append((virus, s+1, nx, ny))

print(graph[tx-1][ty-1])