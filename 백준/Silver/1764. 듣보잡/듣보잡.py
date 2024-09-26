n, m = map(int, input().split())

cnt = 0
d = []
name = []

for i in range(n + m):
    d.append(input())

d.sort()

for i in range(n + m - 1):
    if d[i] == d[i + 1]:
        cnt += 1
        name.append(d[i])

print(cnt)

for i in range(cnt):
    print(name[i])
