import sys
input = sys.stdin.readline
n = int(input())
total = 1
count = 1
start, end = 1, 1

while end != n:
    if total < n:
        end += 1
        total = total + end
    elif total > n:
        total = total - start
        start += 1
    else:
        count += 1
        end += 1
        total = total + end
print(count)