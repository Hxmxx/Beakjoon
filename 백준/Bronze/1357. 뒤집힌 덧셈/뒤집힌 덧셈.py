def rev(gap) :
    return int(gap[::-1])
    
x, y = input().split()
print(rev(str(rev(x)+rev(y))))
