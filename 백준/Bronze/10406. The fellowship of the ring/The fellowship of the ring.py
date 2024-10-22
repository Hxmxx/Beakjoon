a, b, c = map(int, input().split())
li = list(map(int, input().split()))
cnt = 0

for i in li:
    if i >= a and i <= b :
        cnt += 1
    else :
        continue

print(cnt)