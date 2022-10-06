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


'''
n = int(input())
ans = [0]*n
A = list(map(int, input().split()))
myStack = []

for i in range(n):
    # 스택이 비어 있지 않고 현재 수열의 스택 top 인덱스가 가리키는 수열보다 큰 경우
    while myStack and A[myStack[-1]] < A[i]:
        ans[myStack.pop()] = A[i] # 정답 리스트에 오큰수를 현재 수열로 저장하기
    myStack.append(i)

while myStack:
    ans[myStack.pop()] = -1

result = ""

print(" ".join(map(str, ans)))
'''