n = int(input())
array1 = list(map(int, input().split()))
m = int(input())
array2 = list(map(int, input().split()))

def bs_search(array, target, start, end):
    if start > end:
        return None
    mid = (start+end)//2
    if target == array[mid]:
        return mid
    elif target < array[mid]:
        return bs_search(array, target, start, mid-1)
    else:
        return bs_search(array, target, mid+1, end)

array1.sort()

for num in array2:
    if bs_search(array1, num, 0, n):
        print("yes", end=' ')
    else:
        print("no", end=' ')


# 답안2
# n = int(input())
# array1 = list(map(int, input().split()))
# m = int(input())
# array2 = list(map(int, input().split()))
#
# def binary_search(array, target, start, end):
#     while start <= end:
#         mid = (start+end)//2
#         if target == array[mid]:
#             return mid
#         elif target < array[mid]:
#             end = mid-1
#         else:
#             start = mid+1
#     return None
#
# array1.sort()
# for i in array2:
#     result = binary_search(array1, i, 0, n-1)
#     if result != None:
#         print('yes', end=' ')
#     else:
#         print('no', end=' ')

# # 답안3 : 계수정렬
# n = int(input())
# array = [0] * 1000001
#
# for i in input().split():
#     array[int(i)] = 1
#
# m = int(input())
# x = list(map(int, input().split()))
#
# for i in x:
#     if array[i] == 1:
#         print('yes', end=' ')
#     else:
#         print('no', end=' ')
#

# 답안3: 집합set 이용하기
# n = int(input())
# array = set(map(int, input().split()))
# 
# m = int(input())
# x = list(map(int, input().split()))
# 
# for i in x:
#     if i in array:
#         print('yes', end=' ')
#     else:
#         print('no', end=' ')
# 

# 0626 복습답안
def bs_search(array, target, start, end):
    while start <= end:
        mid = (start+end)//2
        if array[mid] < target:
            start = mid + 1
        elif array[mid] > target:
            end = mid - 1
        else:
            return mid
    return None

n = int(input())
array = list(map(int, input().split()))
m = int(input())
x = list(map(int, input().split()))
array = sorted(array)

for target in x:
    result = bs_search(array, target, 0, n-1)
    if result == None:
        print("no", end=' ')
    else:
        print("yes", end=' ')

