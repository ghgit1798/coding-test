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
