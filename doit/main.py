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