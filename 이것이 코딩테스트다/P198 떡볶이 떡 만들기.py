n, m = map(int, input().split())
array = list(map(int, input().split()))

# 정답인 높이 h는 최소 0에서부터 최대 max(array)까지이다.
start, end = 0, max(array)
answer = 0
while start <= end:
    mid = (start+end) // 2
    sum = 0
    for num in array:
        if mid < num:
            sum = sum + (num-mid)
    if sum >= m:
        answer = mid
        start = mid + 1
    else:
        end = mid - 1

print(answer)


# 0626 복습답안
n, m = map(int, input().split())
array = list(map(int, input().split()))
start, end = 0, max(array)
answer = 0

while start <= end:
    mid = (start+end)//2
    target = 0
    for num in array:
        if num > mid:
            target += (num - mid)

    if target < m: # target이 더 작으면, 높이를 줄여야함
        end = mid - 1
    elif target > m: # target이 더 크면, 높이를 키워야함
        start = mid + 1
        answer = mid
    else:
        answer = mid
        break

print(answer)

# 0709 복습답안
n, m = map(int, input().split())
array = list(map(int, input().split()))

h = 0
start, end = 0, max(array)

while start <= end:
    total = 0
    mid = (start+end)//2
    for num in array:
        if num > mid:
            total = total + (num - mid)

    if total > m:
        start = mid + 1
        h = mid
    elif total < m:
        end = mid - 1
    else:
        h = mid
        break

print(h)
