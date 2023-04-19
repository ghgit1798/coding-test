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
