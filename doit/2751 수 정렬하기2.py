import sys
import random
input = sys.stdin.readline

n = int(input())
myList = [int(input()) for _ in range(n)]
random.shuffle(myList)

def quick_sort(A, start, end):
    if start >= end:
        return
    pivot = start
    left = start+1
    right = end

    while left <= right:
        while left <= end and A[left] <= A[pivot]:
            left += 1
        while right > start and A[right] >= A[pivot]:
            right -= 1
        if left >= right:
            A[pivot], A[right] = A[right], A[pivot]
        else:
            A[left], A[right] = A[right], A[left]

    quick_sort(A, start, right-1)
    quick_sort(A, right+1, end)

quick_sort(myList, 0, len(myList)-1)

for a in myList:
    print(a)