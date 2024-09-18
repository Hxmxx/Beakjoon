n, m = map(int, input().split())
arr = []

for _ in range(n):
    arr.append(list(input())) 

cnt = -1

for i in range(n-7):
    for j in range(m-7):
        white = 0
        black = 0

        
        for row in range(i, i + 8):
            for col in range(j, j + 8):
                if (row + col) % 2 == 0:  
                    if arr[row][col] != "W":
                        white += 1
                    else:
                        black += 1
                else:  
                    if arr[row][col] != "B":
                        white += 1
                    else:
                        black += 1

        cnt1 = min(white, black)

        if cnt == -1 or cnt > cnt1:
            cnt = cnt1

print(cnt)
