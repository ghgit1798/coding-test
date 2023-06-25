n, m = map(int, input().split())
array = list(map(int, input().split()))
array = sorted(array)
start, end = 0, max(array)
answer, total = 0, 1e9

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
