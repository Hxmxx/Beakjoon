li = [int(input()) for i in range(5)]
sum = 0

for i in li:
    if i <= 40 :
        i = 40
    sum+=int(i)

print(int(sum/5))