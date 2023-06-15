h = int(input())

count = 0
for i in range(h+1):
    for j in range(60):
        for k in range(60):
            # 매 시각 안에 '3'이 포함되어 있다면 카운트 증가
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)


# 0615 복습
n = int(input())
answer = 0

for i in range(n+1):
    for j in range(60):
        for k in range(60):
            res = str(i)+str(j)+str(k)

            if '3' in res:
                answer += 1
print(answer)