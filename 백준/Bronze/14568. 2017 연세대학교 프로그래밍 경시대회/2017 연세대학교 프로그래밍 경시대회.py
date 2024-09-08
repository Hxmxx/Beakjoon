n = int(input())
a, b, c = 0, 0, 0
cnt = 0

for i in range(1, n-1):
    for j in range(1, i-1):
        m = n - i - j
        if m > 0 and i >= j + 2 and m % 2 == 0 :
            cnt += 1


print(cnt)