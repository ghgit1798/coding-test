from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
dx = [0,0,-1,1]
dy = [1,-1,0,0]
cnt = 0

def bfs(graph, x, y):
    global cnt
    queue = deque()
    queue.append([x, y])
    visited[x][y] = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=m:
                continue
            if not visited[nx][ny] and graph[nx][ny]==0:
                queue.append([nx, ny])
                visited[nx][ny] = 1

for i in range(n):
    for j in range(m):
        if not visited[i][j] and graph[i][j]==0:
            bfs(graph, i, j)
            cnt += 1

print(cnt)