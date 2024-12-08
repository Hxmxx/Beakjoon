s = input()
n = int(input())
cnt = 0
#print(s[0:5])

for _ in range(n):
    p = input()
    if s[0:5] == p[0:5] :
        cnt+=1
    else :
        continue

print(cnt)