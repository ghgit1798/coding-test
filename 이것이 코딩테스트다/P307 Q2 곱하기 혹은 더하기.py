s = list(map(int, input()))

total = 0

for i in range(len(s)):
    if i == 0:
        total = s[i]
    else:
        if total > 1 and s[i] > 1:
            total = total * s[i]
        else:
            total = total + s[i]

print(total)