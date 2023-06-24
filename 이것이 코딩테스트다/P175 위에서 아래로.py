n = int(input())

nums = [int(input()) for _ in range(n)]
count = [0]*(max(nums)+1)

for num in nums:
    count[num] += 1

for i in range(len(count)-1, -1, -1):
    if count[i]:
        print(i, end=' ')

# 답안 2
# n = int(input())
# array = []
# for i in range(n):
#     array.append(int(input()))
#
# # 파이썬 기본 정렬 라이브러리를 이용하게 정렬 수행
# array = sorted(array, reverse=True)
#
# # 정렬이 수행된 결과를 출력
# for i in array:
#     print(i, end = ' ')

# 0625 복습답안
n = int(input())
nums = [int(input()) for _ in range(n)]
cnt = [0]*100001

def count_sort(nums):
    for num in nums:
        cnt[num] += 1

count_sort(nums)

for i in range(100000, 0, -1):
    if cnt[i]>0:
        print(i, end=' ')
