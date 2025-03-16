d = {
    '0' : 4,
    '1' : 2
}

while True:
    house = 2
    n = input()
    if n == '0' :
        break
    else:
        for i in n:
            if i in d:
                house += d[i]
            else:
                house += 3
        house += len(n) - 1
        print(house)
