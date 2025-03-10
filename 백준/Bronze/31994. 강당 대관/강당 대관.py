d = {s: int(n) for s, n in (input().split() for _ in range(7))}
print(max(d, key=d.get))