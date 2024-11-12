n = int(input())

for i in range(n):
    a, b = map(float, input().split())
    #a = b * h / 2
    h = a * 2 / b
    print(f'The height of the triangle is {h:.2f} units')