data = input()
count0 = 0
count1 = 1

if data[0] == '1':
    count0 += 1
else:
    count1 += 0

for i in range(len(data) - 1):
    if data[i] != data[i+1]:
        # 다음 수에서 1로 바뀌는 경우
        if data[i+1] == '1':
            count0 += 1
        # 다음 수에서 0으로 바뀌는 경우
        else:
            count1 += 1

print(min(count0, count1))


# 0710 답안
import copy

s = list(map(int, input()))
x = copy.deepcopy(s)

a, b = 0, 0
zero_cnt = 0
one_cnt = 0
count_flag = True

for i in range(len(s)):
    # 0으로 바꾸기
    if s[i] == 1 and count_flag:
        s[i] = 0
        zero_cnt += 1
        count_flag = False
    elif s[i] == 1 and not count_flag:
        s[i] = 0
    elif s[i] == 0 and not count_flag:
        count_flag = True
    else:
        pass


count_flag = True

for i in range(len(x)):
    # 1로 바꾸기
    if x[i] == 0 and count_flag:
        x[i] = 1
        one_cnt += 1
        count_flag = False
    elif x[i] == 0 and not count_flag:
        x[i] = 1
    elif x[i] == 1 and not count_flag:
        count_flag = True
    else:
        pass


if one_cnt > zero_cnt:
    print(zero_cnt)
else:
    print(one_cnt)

print(s)
print(x)
print(zero_cnt, one_cnt)


