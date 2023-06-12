n = int(input())

graph = [[0]*n for _ in range(n)]
dir = list(input().split())
dx = [1,0,-1,0] # 남 동 북 서
dy = [0,1,0,-1] # D R U L
x, y = 0, 0

for mov in dir:
    if mov == 'R':
        nx, ny = x+dx[1], y+dy[1]
    elif mov == 'L':
        nx, ny = x+dx[3], y+dy[3]
    elif mov == 'U':
        nx, ny = x+dx[2], y+dy[2]
    elif mov == 'D':
        nx, ny = x+dx[0], y+dy[0]

    if nx >= n or ny >= n or nx < 0 or ny < 0:
        continue
    else:
        x, y = nx, ny

print(x+1, y+1)
