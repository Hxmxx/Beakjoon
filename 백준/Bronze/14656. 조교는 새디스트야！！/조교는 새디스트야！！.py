n = int(input())
d = list(map(int, input().split()))
cnt = 0

for i in range(1, n+1) :
    if i != d[i-1] :
        cnt+=1
    else :
        continue

print(cnt)