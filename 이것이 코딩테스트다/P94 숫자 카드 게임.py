# 답안1
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
answer = 0

for g in graph:
    answer = max(answer, min(g))

print(answer)

# 답안2
n, m = map(int, input().split())

result = 0
# 한 줄씩 입력받아 확인
for i in range(n):
    data = list(map(int, input().split()))
    # 현재 줄에서 가장 작은 수 찾기
    min_value = min(data)
    # '가장 작은 수'들 중에서 가장 큰 수 찾기
    result = max(result, min_value)

print(result) # 최종 답안 출력

# 0612 복습답안
n, m = map(int, input().split())
answer = 0

for _ in range(n):
    tmp = list(map(int, input().split()))
    minNum = min(tmp)
    answer = max(answer, minNum)

print(answer)


'''
import sys

input = sys.stdin.readline

answer = 0

n, m = map(int, input().split())
graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

for g in graph:
    a = min(g)
    answer = max(answer, a)


print(answer)
'''