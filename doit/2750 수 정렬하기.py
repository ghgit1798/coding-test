import sys
input = sys.stdin.readline

n = int(input())
myList = [int(input()) for _ in range(n)]

for j in range(n-1):
    for i in range(n-j-1):
        if myList[i] > myList[i+1]:
            myList[i], myList[i+1] = myList[i+1], myList[i]

for a in myList:
    print(a)