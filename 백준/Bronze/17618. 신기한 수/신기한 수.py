cnt = 0

for n in range(1, int(input())+1):
    s = 0
    temp = n
    while temp:
        s += temp % 10
        temp //= 10
    if n%s == 0:
        cnt += 1

print(cnt)