n, m = map(int, input().split())
a, b, dir = map(int ,input().split())
a, b = a, b
answer = 0

# 북, 동, 남, 서 : 왼쪽부터 돌아가는 순서는 북 서 남 동 > i+3%4로 연산 : 3, 혹은 i-1로 연산
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
x, y, nx, ny = a, b, 0, 0
ground = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
visited[a][b] = 1

# 왼쪽으로 회전
def turn_left():
    global dir
    dir -= 1
    if dir == -1:
        dir = 3

# 시뮬레이션
cnt = 1
turn_time = 0
while True:
    # 왼쪽으로 회전
    turn_left()
    nx = x + dx[dir]
    ny = y + dy[dir]
    # 회전한 이후에 정면에 가보지 않은 칸이 존재하는 경우 이동
    if visited[nx][ny] == 0 and ground[nx][ny] == 0:
        visited[nx][ny]=1
        x, y = nx, ny
        cnt += 1
        turn_time = 0
        continue
    # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
    else:
        turn_time += 1
    # 네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[dir]
        ny = y - dy[dir]
        # 뒤로 갈 수 있다면 이동하기
        if ground[nx][ny] == 0:
            x, y = nx, ny
        else:
            break
        turn_time = 0

print(cnt)


# 0709 복습답안
n, m = map(int, input().split())
x, y, dir = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
visited[x][y], cnt = 1, 1

dx = [-1, 0, 1, 0] # 북 서 남 동
dy = [0, -1, 0, 1]

turn_time = 0
while True:
    dir = (dir+1)%4
    nx, ny = x + dx[dir], y + dy[dir]
    if visited[nx][ny] == 0 and graph[nx][ny] == 0:
        visited[nx][ny] = 1
        x, y = nx, ny
        cnt += 1
        turn_time = 0
    else:
        turn_time += 1

    if turn_time == 4:
        nx, ny = x - dx[dir], y - dy[dir]
        if graph[nx][ny] == 0:
            x, y = nx, ny
            turn_time = 0
        else:
            break

print(cnt)
