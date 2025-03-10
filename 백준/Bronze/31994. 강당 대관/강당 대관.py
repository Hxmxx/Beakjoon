d = []
max_ = 0
winner = ""

for i in range(7):
    s = input().split()
    d.append(s)
    d[i][1] = int(d[i][1])
    if d[i][1] > max_:
        max_ = d[i][1]
        winner = d[i][0]
    #print(max_, winner)

#print(d)
print(winner)
