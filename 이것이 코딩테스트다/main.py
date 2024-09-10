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