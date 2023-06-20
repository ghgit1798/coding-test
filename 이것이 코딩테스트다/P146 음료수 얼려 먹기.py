# 내가 작성한 BFS 답안
from collections import deque

n, m = map(int, input().split())
ices = [list(map(int, input())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
cnt = 0

def bfs(x, y):
    queue = deque([])
    queue.append((x, y))
    visited[x][y] = 1
    while queue:
        a, b = queue.popleft()
        for i in range(4):
            nx, ny = a+dx[i], b+dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if not visited[nx][ny] and ices[nx][ny] == 0:
                visited[nx][ny] = 1
                queue.append((nx, ny))

for i in range(n):
    for j in range(m):
        if not visited[i][j] and ices[i][j] == 0:
            bfs(i, j)
            cnt += 1

print(cnt)


# # DFS 답안
# n,m = map(int, input().split())
#
# graph = []
# for i in range(n):
#     graph.append(list(map(int, input())))
#
# def dfs(x, y):
#     if x <= -1 or x >= n or y <= -1 or y >= m:
#         return False
#     if graph[x][y] == 0:
#         graph[x][y] = 1
#         dfs(x-1, y)
#         dfs(x, y-1)
#         dfs(x+1, y)
#         dfs(x, y+1)
#         return True
#     return False
#
# result = 0
# for i in range(n):
#     for j in range(m):
#         if dfs(i, j) == True:
#             result += 1
#
# print(result)

# 0619 복습 답안

from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
dx = [0,0,-1,1]
dy = [1,-1,0,0]
cnt = 0

def bfs(graph, x, y):
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