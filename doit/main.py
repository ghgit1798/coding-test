import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
A = list(map(int, input().split()))
A.sort()
cnt = 0
i, j = 0,n-1

while i < j:
    if A[i]+A[j] < m:
        i += 1
    elif A[i]+A[j] > m:
        j -= 1
    else:
        cnt += 1
        i += 1
        j -= 1

print(cnt)