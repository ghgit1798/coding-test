# n, k = map(int, input().split())
# a = list(map(int, input().split()))
# b = list(map(int, input().split()))
#
# for _ in range(k):
#     aMin = min(a)
#     bMax = max(b)
#     if aMin < bMax:
#         a.append(bMax)
#         a.remove(aMin)
#         b.remove(bMax)
#
# print(sum(a))

n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break

print(sum(a))

# 0625 복습답안
n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a = sorted(a)
b = sorted(b, reverse=True)

for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break

print(sum(a))
