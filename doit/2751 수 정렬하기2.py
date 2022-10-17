import sys
import random
input = sys.stdin.readline

n = int(input())
myList = [int(input()) for _ in range(n)]
random.shuffle(myList)

''' 퀵 정렬 '''
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


''' 병합 정렬
import sys
input = sys.stdin.readline

def merge_sort(arr):
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    low_arr = merge_sort(arr[:mid])
    high_arr = merge_sort(arr[mid:])

    merged_arr = []
    l = h = 0
    while l < len(low_arr) and h < len(high_arr):
        if low_arr[l] < high_arr[h]:
            merged_arr.append(low_arr[l])
            l += 1
        else:
            merged_arr.append(high_arr[h])
            h += 1
    merged_arr += low_arr[l:]
    merged_arr += high_arr[h:]
    return merged_arr

n = int(input())
myList = [int(input()) for _ in range(n)]
myList = merge_sort(myList)

for a in myList:
    print(a)
'''