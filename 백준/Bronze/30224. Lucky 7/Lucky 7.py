n = input()

if '7' not in n and int(n) % 7 : print(0)
elif '7' not in n and int(n) % 7 == 0 : print(1)
elif '7' in n and int(n) % 7 : print(2)
elif '7' in n and int(n) % 7 == 0 : print(3)