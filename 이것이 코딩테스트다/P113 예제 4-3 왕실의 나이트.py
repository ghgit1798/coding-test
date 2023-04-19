# k = input()
# x, y = int(k[1])-1, k[0]
# cnt = 0
#
# dx = ['a','b','c','d','e','f','g','h']
# for i in range(len(dx)):
#     if y == dx[i]:
#         y = i
#         break
#
# steps = [(2,-1), (2,1), (-2,-1), (-2,1), (1,2), (1,-2), (-1,2), (-1,-2)]
#
# for a, b in steps:
#     nx = int(x) + a
#     ny = int(y) + b
#     if nx < 0 or ny < 0 or nx >= 8 or ny >= 8:
#         continue
#     cnt += 1
#
# print(cnt)
#

input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0]) - int(ord('a'))) + 1

# 나이트가 이동할 수 있는 8가지 방향 정의
steps = [(-2,-1), (-1,-2), (1,-2), (2,-1), (2,1), (1,2), (-1, 2), (-2,1)]

# 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
result = 0
for step in steps:
    # 이동하고자 하는 위치 확인
    next_row = row+step[0]
    next_column = column + step[1]
    # 해당 위치로 이동이 가능하다면 카운트 증가
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1

print(result)