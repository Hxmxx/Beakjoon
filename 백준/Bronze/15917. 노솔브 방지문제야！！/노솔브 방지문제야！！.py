import sys
import math
input = sys.stdin.readline

a = [2**i for i in range(32)]

for i in range(int(input())):
    if math.log2(int(input())).is_integer():
        print(1)
    else :
        print(0)