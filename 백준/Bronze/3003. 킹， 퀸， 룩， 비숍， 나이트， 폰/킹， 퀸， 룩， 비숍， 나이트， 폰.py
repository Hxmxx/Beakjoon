d = list(map(int, input().split()))
li = [1, 1, 2, 2, 2, 8]

for i in range(len(d)):
    print(li[i]-d[i], end=" ")