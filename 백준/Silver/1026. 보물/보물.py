n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

s = [0 for i in range(n)]
a = sorted(a, reverse=True)
b = sorted(b)

for i in range(n):
    s[i] = a[i] * b[i]

print(sum(s))