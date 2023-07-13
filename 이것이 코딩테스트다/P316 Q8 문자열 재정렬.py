alpha = []
n = 0

data = list(map(str, input()))

for d in data:
    if d.isalpha():
        alpha.append(d)
    else:
        n = n+int(d)

alpha.sort()
alpha = "".join(alpha) + str(n)
print(alpha)