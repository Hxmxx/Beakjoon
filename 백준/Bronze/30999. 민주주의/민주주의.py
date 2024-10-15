n, m = map(int, input().split())
li = []

for i in range(n):
    # 각 행의 값을 리스트로 저장
    li.append(list(input()))

out = 0  # 'O'가 더 많은 행의 수

for i in range(n):
    Ocnt = 0
    Xcnt = 0
    for j in range(m):
        if li[i][j] == 'O':  # li의 i번째 행에서 값을 비교
            Ocnt += 1
        else:
            Xcnt += 1
    if Ocnt > Xcnt:
        out += 1

print(out)
