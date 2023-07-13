from collections import deque


def solution(s):
    answer = len(s)
    mid = len(s) // 2

    for i in range(1, mid + 1):
        cnt = 1
        temp = ""
        prev = s[:i]
        for j in range(i, len(s), i):
            now = s[j:j + i]

            if prev == now:
                cnt += 1
            else:
                temp += str(cnt) + prev if cnt >= 2 else prev
                prev = now
                cnt = 1

        temp += str(cnt) + prev if cnt >= 2 else prev

        if len(temp) < answer:
            answer = len(temp)
    return answer