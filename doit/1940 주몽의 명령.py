import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
L = list(map(int, input().split()))
L = sorted(L, reverse=False)
s_idx, e_idx = 0, n-1
answer = 0

while s_idx < e_idx:
    total = L[s_idx]+L[e_idx]
    if total < m:
        s_idx += 1
    elif total > m:
        e_idx -= 1
    else:
        answer += 1
        e_idx -= 1

print(answer)