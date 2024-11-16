from math import pi

n = int(input())

for i in range(n):
    a, p1 = map(float, input().split())
    r, p2 = map(float, input().split())
    val1, val2 = (a / p1), (pi * r**2) / p2
    print(["Slice of pizza", "Whole pizza"] [val1 < val2])