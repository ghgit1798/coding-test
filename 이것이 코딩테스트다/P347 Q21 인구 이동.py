import sys
from collections import deque

input = sys.stdin.readline

n, l, r = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dx, dy = [-1,1,0,0], [0,0,-1,1]
answer = 0
index = 0

def bfs(x, y, index):
    q = deque()
    visited_list = deque()

    q.append([x, y])
    visited_list.append([x, y])
    union[x][y] = index
    total = graph[x][y]

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=n:
                continue
            diff = abs(graph[x][y] - graph[nx][ny])
            if l <= diff <= r and union[nx][ny] == -1:
                total += graph[nx][ny]
                q.append([nx, ny])
                visited_list.append([nx, ny])
                union[nx][ny] = index

    result = total // len(visited_list)

    while visited_list:
        x, y = visited_list.popleft()
        graph[x][y] = result

while True:
    union = [[-1] * n for _ in range(n)]
    index = 0
    for i in range(n):
        for j in range(n):
            if union[i][j] == -1:
                bfs(i, j, index)
                index += 1

    if index == n*n:
        break

    answer += 1

print(answer)

