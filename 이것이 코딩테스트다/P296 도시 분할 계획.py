def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())
parent = [0]*(n+1)
dist = []
result = 0

for i in range(n+1):
    parent[i] = i

for _ in range(m):
    a, b, cost = map(int, input().split())
    dist.append((cost, a, b))

dist.sort()
# max_dist = dist[-1][0]
# print(max_dist)

for cost, a, b in dist:
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a != b:
        union_parent(parent, a, b)
        result += cost
        last = cost

print(result-last)