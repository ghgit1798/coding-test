import sys
input = sys.stdin.readline

N = int(input())
A = []

for i in range(N):
    A.append((int(input()), i))

Max = 0
sorted_A = sorted(A)

for i in range(N):
    if Max < sorted_A[i][1] - i:
        Max = sorted_A[i][1] - i

print(Max + 1)

'''
import sys
input = sys.stdin.readline

n = int(input())
myList = [(int(input()), i) for i in range(n)]
mySort = sorted(myList, key=(lambda x: x[0]))
myAnswer = 0

for i in range(n):
    if myAnswer < mySort[i][1]-i:
        myAnswer = mySort[i][1]-i

print(myAnswer+1)

'''