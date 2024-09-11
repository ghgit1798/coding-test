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




'''
구현 유형
1. 특정 소수점 자리까지 출력해야 하는 문제
2. 문자열이 입력되었을 때, 한 문자 단위로 끊어서 넣어야 하는 문제
 - 파싱을 해야하는 유형으로 볼 수 있다.
 - 대체로 사소한 조건 설정이 많다. -> 문법도 익숙하지 않아 어려움
ㅁ 유형
 1. 완전탐색, 시뮬레이션 모두 구현 유형이다.
  - 완전탐색 : 모든 경우의 수를 다 계산하는 방법
  - 시뮬레이션 : 문제에서 제시한 알고리즘을 한 단계씩 수행하는 유형
'''

# 240911 P.108 상하좌우
import sys
input = sys.stdin.readline

dx = [0,-1,0,1] # 동북서남
dy = [1,0,-1,0]

n = int(input())
dirs = list(input().split())

x,y = 0,0

for dir in dirs:
    nx, ny = x, y
    if dir == 'R':
        nx = x + dx[0]
        ny = y + dy[0]
    elif dir == 'U':
        nx = x+dx[1]
        ny = y+dy[1]
    elif dir == 'L':
        nx = x+dx[2]
        ny = y+dy[2]
    else:
        nx, ny = x+dx[3],y+dy[3]
    if nx<0 or ny<0 or nx>=n or ny>=n:
        continue
    x, y = nx, ny

print(x+1, y+1)

# 모범답안

n = int(input())
x,y = 1,1
plans = input().split()

dx = [0,0,-1,1]
dy = [-1,1,0,0]
move_types = ['L','R','U','D']

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx<1 or ny<1 or nx>n or ny>n:
        continue
    x,y = nx,ny

print(x,y)


