from collections import deque

n, m = map(int, input().split())
maze = [list(map(int, input())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
visited[0][0] = 1
answer = 0

dx = [0,0,-1,1]
dy = [-1,1,0,0]
x, y, = 0, 0

def bfs(x, y):
    queue = deque([])
    queue.append((x, y))
    while queue:
        a, b = queue.popleft()
        for i in range(4):
            nx, ny = a+dx[i], b+dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if not visited[nx][ny] and maze[nx][ny]:
                visited[nx][ny] = visited[a][b] + 1
                queue.append((nx, ny))

bfs(x, y)
print(visited[n-1][m-1])


# from collections import deque
#
# n, m = map(int, input().split())
# graph = []
# for i in range(n):
#     graph.append(list(map(int, input())))
#
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
#
# def bfs(x, y):
#     queue = deque()
#     queue.append((x,y))
#     while queue:
#         x, y = queue.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if nx < 0 or ny < 0 or nx >= n or ny >= m:
#                 continue
#             if graph[nx][ny] == 0:
#                 continue
#             if graph[nx][ny] == 1:
#                 graph[nx][ny] = graph[x][y]
#                 queue.append((nx, ny))
#     return graph[n-1][m-1]
#
# print(bfs(0, 0))

# 0620 복습답안
from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
cnt = 0
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(graph, x, y):
    queue = deque()
    queue.append([x, y])
    visited[x][y] = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if not visited[nx][ny] and graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y]+1
                visited[nx][ny] = 1
                queue.append([nx, ny])

bfs(graph, 0, 0)

print(graph[n-1][m-1])
