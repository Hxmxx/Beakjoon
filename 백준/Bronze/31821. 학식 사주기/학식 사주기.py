#n = int(input())
d = [int(input()) for _ in range(int(input()))]
sum1 = 0

for _ in range(int(input())):
    sum1 += d[int(input())-1]

print(sum1)