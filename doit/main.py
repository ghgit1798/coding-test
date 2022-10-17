import sys
input = sys.stdin.readline
answer = 0

def merge_sort(arr):
    global answer
    if len(arr) < 2:
        return arr
    mid = len(arr) // 2
    low_arr = merge_sort(arr[:mid])
    high_arr = merge_sort(arr[mid:])

    merged_arr = []
    l = h = 0
    while l < len(low_arr) and h < len(high_arr):
        if low_arr[l][0] < high_arr[h][0]:
            merged_arr.append(low_arr[l])
            l += 1
        else:
            merged_arr.append(high_arr[h])
            h += 1

    merged_arr += low_arr[l:]
    merged_arr += high_arr[h:]
    return merged_arr

n = int(input())
L = list(map(int, input().split()))
L = [(L[i], i) for i in range(n)]
result = merge_sort(L)
