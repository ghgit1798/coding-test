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
parent = [0] * (n+1)

for i in range(n+1):
    parent[i] = i

for _ in range(m):
    op, a, b = map(int, input().split())

    if op == 0:
        union_parent(parent, a, b)
    if op == 1:
        a = find_parent(parent, a)
        b = find_parent(parent, b)
        if a == b:
            print("YES")
        else:
            print("NO")

# 0707 복습답안

n, m = map(int, input().split())
parent = [0]*(n+1)

for i in range(1, n+1):
    parent[i] = i

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

for _ in range(m):
    x, a, b = map(int, input().split())
    if x == 0:
        union_parent(parent, a, b)
    if x == 1:
        aa = find_parent(parent, a)
        bb = find_parent(parent, b)
        if aa == bb:
            print("YES")
        else:
            print("NO")

# 0709 복습 답안
import sys
input = sys.stdin.readline

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

for i in range(1, n+1):
    parent[i] = i

for _ in range(m):
    op, a, b = map(int, input().split())
    if op == 0: # 팀 합치기
        union_parent(parent, a, b)
    if op == 1: # 같은 팀 확인
        if find_parent(parent, a) == find_parent(parent, b):
            print("YES")
        else:
            print("NO")
