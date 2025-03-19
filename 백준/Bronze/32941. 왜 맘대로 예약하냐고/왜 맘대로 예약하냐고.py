T, X = map(int, input().split())
N = int(input())
result = True 

for _ in range(N):
    K = int(input())
    A = list(map(int, input().split()))

    if X not in A:
        result = False

if result:
    print("YES")
else:
    print("NO")
