d = input().split()

if d[1] == 'AND' :
    if d[0] == 'true' and d[2] == 'true' :
        print('true')
    else :
        print('false')
elif d[1] == 'OR' :
    if d[0] == 'true' or d[2] == 'true' :
        print('true')
    else:
        print('false')
    