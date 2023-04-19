k = input()
x, y = int(k[1])-1, k[0]
cnt = 0

dx = ['a','b','c','d','e','f','g','h']
for i in range(len(dx)):
    if y == dx[i]:
        y = i
        break

steps = [(2,-1), (2,1), (-2,-1), (-2,1), (1,2), (1,-2), (-1,2), (-1,-2)]

for a, b in steps:
    nx = int(x) + a
    ny = int(y) + b
    if nx < 0 or ny < 0 or nx >= 8 or ny >= 8:
        continue
    cnt += 1

print(cnt)

