# n = int(input())
# x, y = 1, 1
# plans = input().split()
#
# dx = [0,0,-1,1]
# dy = [-1,1,0,0]
# move_types = ['L','R','U','D']
#
# for plan in plans:
#     for i in range(len(move_types)):
#         if plan == move_types[i]:
#             nx = x + dx[i]
#             ny = y + dy[i]
#     if nx < 1 or ny < 1 or nx > n or ny > n:
#         continue
#     x, y = nx, ny
#
# print(x, y)

n = int(input())
dir = list(input().split())
dx = [0, 0, 1, -1] # R, L, D, U
dy = [1, -1, 0, 0]
x, y = 0, 0

for d in dir:
    if d == 'D':
        nx = x + dx[2]
        ny = y + dy[2]
    elif d == 'U':
        nx = x + dx[3]
        ny = y + dy[3]
    elif d == 'R':
        nx = x + dx[0]
        ny = y + dy[0]
    elif d == 'L':
        nx = x + dx[1]
        ny = y + dy[1]
    # if (x < n and x >= 0) and (y < n and y >= 0):
    if nx < 0 or ny < 0 or nx >= n or ny >= n:
        continue
    x, y = nx, ny

print(x+1, y+1)

# 0612 복습답안
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
