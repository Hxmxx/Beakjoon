import sys
input = sys.stdin.read

data = input().split()
n = int(data[0])
d = list(map(int, data[1:n+1]))

d.sort()

sys.stdout.write('\n'.join(map(str, d)) + '\n')
