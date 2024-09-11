import sys
input = sys.stdin.readline

num = int(input())
# 11^6 = 1,000,000 : 복잡도
# 24 * 60 * 60 = 24 * 3600 = 86400
answer = 0

for i in range(num+1):
    for j in range(0, 60):
        for k in range(0, 60):
            st = str(i)+str(j)+str(k)
            st = list(st) # 안해도 됨
            if '3' in st:
                answer += 1

print(answer)