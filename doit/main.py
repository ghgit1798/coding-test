n = int(input())
myList = list(map(int, input().split()))
s = [0]*n

for i in range(1, n):
    Min = myList[i]
    for j in range(i-1, -1, -1):
        if myList[j] > Min:
            myList[j+1] = myList[j]
            myList[j] = Min

s[0] = myList[0]
for i in range(1, n):
    s[i] = s[i-1] + myList[i]

print(sum(s))