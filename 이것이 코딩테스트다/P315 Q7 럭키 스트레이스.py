k = list(map(int, input()))
mid = len(k)//2
a = sum(k[0:mid])
b = sum(k[mid:len(k)])

if a == b:
    print("LUCKY")
else:
    print("READY")
