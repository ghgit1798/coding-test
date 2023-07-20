from itertools import combinations

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

house, chicken = [], []
for r in range(n):
    for c in range(n):
        if graph[r][c] == 1:
            house.append((r, c))
        elif graph[r][c] == 2:
            chicken.append((r, c))

candidates = list(combinations(chicken, m))

def get_sum(candidate):
    answer = 0
    for hx, hy in house:
        dist = 1e9
        for cx, cy in candidate:
            dist = min(dist, abs(hx-cx)+abs(hy-cy))
        answer += dist
    return answer

answer = 1e9
for candidate in candidates:
    answer = min(answer, get_sum(candidate))

print(answer)