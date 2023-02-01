import sys
input = sys.stdin.readline

n = int(input())
L = list(map(int, input().split()))
L.sort()
answer = 0

for k in range(n):

    find = L[k]
    i, j = 0, n-1
    while i < j:
        if L[i]+L[j] == find:
            if i != k and j != k:
                answer += 1
                break
            elif i == k:
                i += 1
            elif j == k:
                j -= 1
        elif L[i]+L[j] < find:
            i += 1
        else:
            j -= 1

print(answer)