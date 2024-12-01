import sys

input = sys.stdin.readline

n = int(input())
d = [input() for _ in range(n)]

for i in d:
    print(i.lower(), end='')