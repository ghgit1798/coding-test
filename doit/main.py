myList = list(map(int, input()))

for i in range(len(myList)):
    Max = i
    for j in range(i+1, len(myList)):
        if myList[Max] < myList[j]:
            Max = j
    myList[Max], myList[i] = myList[i], myList[Max]

print("".join(map(str, myList)))