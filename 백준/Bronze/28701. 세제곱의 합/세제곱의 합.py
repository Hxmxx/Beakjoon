sum = 0
sum1 = 0
sum2 = 0
n = int(input())
for i in range(1, n+1):
    sum+=i
    sum1+=i
for i in range(1, n+1):
    sum2+=i**3

print(sum)
print(sum1**2)
print(sum2)