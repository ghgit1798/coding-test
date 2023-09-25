from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]
dx, dy = [-1,1,0,0], [0,0,-1,1]
answer = 0

def bfs(graph, x, y):
    q = deque()
    q.append([x, y])
    while q:
        x, y = q.popleft()
        graph[x][y] = 2
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if graph[nx][ny] == 0:
                q.append([nx, ny])

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            bfs(graph, i, j)
            answer += 1

print(answer)