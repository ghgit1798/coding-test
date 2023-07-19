from itertools import combinations

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
chicken, house = [], []

for r in range(n):
    for c in range(n):
        if graph[r][c] == 1:        # 일반 집
            house.append((r,c))
        elif graph[r][c] == 2:      # 치킨집
            chicken.append((r,c))

# 모든 치킨집 중에서 m개의 치킨집을 뽑는 조합 계산
candidates = list(combinations(chicken, m))

# 치킨 거리의 합을 계산하는 함수
def get_sum(candidate):
    result = 0
    for hx, hy in house:
        dist = 1e9
        for cx, cy in candidate:
            dist = min(dist, abs(hx-cx)+abs(hy-cy))
        # 가장 가까운 치킨집까지의 거리를 더하기
        result = result + dist
    return result

# 치킨 거리의 합의 최소를 찾아 출력
result = 1e9
for candidate in candidates:
    result = min(result, get_sum(candidate))

print(result)