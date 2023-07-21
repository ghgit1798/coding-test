from itertools import permutations

def solution(n, weak, dist):
    length = len(weak)
    for i in range(length):
        weak.append(weak[i]+n)
    candidates = list(permutations(dist, len(dist)))

    answer = len(dist) + 1
    # 첫번째부터 length-1까지 시작점 테스트
    for start in range(length):
        for candidate in candidates:
            count = 1
            position = weak[start] + candidate[count-1]
            for i in range(start, start+length):
                if position < weak[i]:
                    count += 1
                    if count > len(dist):
                        break
                    position = weak[i] + candidate[count-1]
            answer = min(answer, count)

    if answer > len(dist):
        return -1
    return answer
