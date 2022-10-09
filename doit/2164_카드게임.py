from collections import deque

n = int(input())
myList = [num for num in range(1, n+1)]
myQueue = deque(myList)
answer = 0

while len(myQueue) != 1:
    a = myQueue.popleft()
    b = myQueue.popleft()
    myQueue.append(b)

print(myQueue.popleft())