import sys
from bisect import bisect_left
from collections import defaultdict

input = sys.stdin.readline

n, m = map(int, input().split())
reservations = defaultdict(list) 

result = [] 
for _ in range(m):
    k, s, e = map(int, input().split())
    
    current_reservations = reservations[k]
    
    idx = bisect_left(current_reservations, (s, 0))
    
    if idx > 0 and current_reservations[idx - 1][1] > s:
        result.append("NO")
    else:
        result.append("YES")
        current_reservations.insert(idx, (s, e))

sys.stdout.write("\n".join(result) + "\n")
