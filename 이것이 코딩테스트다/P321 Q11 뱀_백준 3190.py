from collections import deque

n = int(input())
graph = [[0]*n for _ in range(n)]

k = int(input())
for _ in range(k):
    x, y = map(int, input().split())
    graph[x-1][y-1] = 1

l = int(input())
direction = deque()
for _ in range(l):
    t, c = map(str, input().split())
    direction.append((int(t), c))

dx = [0,1,0,-1] # 동, 남, 서, 북
dy = [1,0,-1,0]
dir = 0

time = 0
x, y = 0, 0
graph[x][y] = 9999
snake = deque()
snake.append((0, 0))

def turn(dir, c):
    if c == 'L':
        dir = (dir + 3) % 4
    if c == 'D':
        dir = (dir + 1) % 4
    return dir

while True:
    time = time + 1

    nx, ny = x+dx[dir], y+dy[dir]
    if nx < 0 or ny < 0 or nx >= n or ny >= n:
        break
    if graph[nx][ny] == 1:
        graph[nx][ny] = 9999
        x, y = nx, ny
        snake.append((nx, ny))
    elif graph[nx][ny] == 0:
        graph[nx][ny] = 9999
        x, y = nx, ny
        snake.append((nx, ny))
        a, b = snake.popleft()
        graph[a][b] = 0
    else:
        # 9999인 경우, 자기 자신과 부딪히고 종료
        break

    if direction and direction[0][0] == time:
        _, c = direction.popleft()
        dir = turn(dir, c)

print(time)