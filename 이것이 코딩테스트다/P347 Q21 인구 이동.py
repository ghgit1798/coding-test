import sys
from collections import deque

input = sys.stdin.readline

dx, dy = [-1,1,0,0], [0,0,-1,1]

n, l, r = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
# visited_xy = [[0]*n for _ in range(n)]
answer = 0

def bfs(graph, x, y):
    # 방문한 위치(x,y)를 저장하는 곳 필요 : 다 방문한 다음 n등분한 값을 저장해야함.

    q = deque()
    visited_list = deque()
    visited = [[0] * n for _ in range(n)]

    q.append([x, y])
    visited_list.append([x, y])
    visited[x][y] = 1
    total = graph[x][y]

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=n:
                continue
            if visited[nx][ny]:
                continue
            diff = abs(graph[x][y] - graph[nx][ny])
            if l <= diff <= r:
                total += graph[nx][ny]
                visited[nx][ny] = 1
                q.append([nx, ny])
                visited_list.append([nx, ny])

    result = total // len(visited_list)


    while visited_list:
        x, y = visited_list.popleft()
        graph[x][y] = result

for x in range(n):
    for y in range(n):
        check = False
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            diff = abs(graph[x][y] - graph[nx][ny])
            if l <= diff <= r:
                check = True

        if check:
            bfs(graph, x, y)
            answer += 1

print(answer)