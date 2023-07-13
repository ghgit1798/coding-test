def solution(s):
    answer = len(s)
    mid = len(s) // 2

    for step in range(1, mid + 1):
        cnt = 1
        temp = ""
        prev = s[:step]
        for j in range(step, len(s), step):
            now = s[j:j + step]

            if prev == now:
                cnt += 1
            else:
                temp += str(cnt) + prev if cnt >= 2 else prev
                prev = now
                cnt = 1

        temp += str(cnt) + prev if cnt >= 2 else prev
        answer = min(answer, len(temp))
    return answer