import sys
input = sys.stdin.readline

n = int(input())
myList = list(map(int, input().split()))
answer = [0]*n
stack = []

for i in range(n):
    if not stack:
        stack.append(i)
    elif myList[stack[-1]] < myList[i]:
        while stack and myList[stack[-1]] < myList[i]:
            j = stack.pop()
            answer[j] = myList[i]
        stack.append(i)
    elif myList[stack[-1]] >= myList[i]:
        stack.append(i)

while stack:
    j = stack.pop()
    answer[j] = -1

print(' '.join(map(str, answer)))