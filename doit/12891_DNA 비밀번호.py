checkList = [0]*4
myList = [0]*4
checkSecret = 0

def myadd(c):
    global checkList, myList, checkSecret
    if c == 'A':
        myList[0] += 1
        if myList[0] == checkList[0]:
            checkSecret += 1
    elif c == 'C':
        myList[1] += 1
        if myList[1] == checkList[1]:
            checkSecret += 1
    elif c == 'G':
        myList[2] += 1
        if myList[2] == checkList[2]:
            checkSecret += 1
    elif c == 'T':
        myList[3] += 1
        if myList[3] == checkList[3]:
            checkSecret += 1

def myremove(c):
    global checkList, myList, checkSecret
    if c == 'A':
        if myList[0] == checkList[0]:
            checkSecret -= 1
        myList[0] -= 1
    elif c == 'C':
        if myList[1] == checkList[1]:
            checkSecret -= 1
        myList[1] -= 1
    elif c == 'G':
        if myList[2] == checkList[2]:
            checkSecret -= 1
        myList[2] -= 1
    elif c == 'T':
        if myList[3] == checkList[3]:
            checkSecret -= 1
        myList[3] -= 1

S, P = map(int, input().split())
Result = 0
A = list(input())
checkList = list(map(int, input().split()))


for i in range(4):
    if checkList[i] == 0:
        checkSecret += 1

for i in range(P):
    myadd(A[i])

if checkSecret == 4:
    Result += 1

for i in range(P, S):
    j = i - P
    myadd(A[i])
    myremove(A[j])
    if checkSecret == 4:
        Result += 1

print(Result)


"""즉석 코딩 풀이

s,p = map(int, input().split())
pList = list(map(str, input()))
pCheck = list(map(int, input().split()))
myCount = [0]*4
answer = 0

for i in range(p):
    if pList[i] == 'A':
        myCount[0] += 1
    elif pList[i] == 'C':
        myCount[1] += 1
    elif pList[i] == 'G':
        myCount[2] += 1
    elif pList[i] == 'T':
        myCount[3] += 1

if myCount[0] >= pCheck[0] and \
    myCount[1] >= pCheck[1] and \
    myCount[2] >= pCheck[2] and \
    myCount[3] >= pCheck[3]:
    answer += 1

for i in range(p, s):
    t = i-p
    if pList[i] == 'A':
        myCount[0] += 1
    elif pList[i] == 'C':
        myCount[1] += 1
    elif pList[i] == 'G':
        myCount[2] += 1
    elif pList[i] == 'T':
        myCount[3] += 1

    if pList[t] == 'A':
        myCount[0] -= 1
    elif pList[t] == 'C':
        myCount[1] -= 1
    elif pList[t] == 'G':
        myCount[2] -= 1
    elif pList[t] == 'T':
        myCount[3] -= 1

    if myCount[0] >= pCheck[0] and \
        myCount[1] >= pCheck[1] and \
        myCount[2] >= pCheck[2] and \
        myCount[3] >= pCheck[3]:
        answer += 1

print(answer)
"""