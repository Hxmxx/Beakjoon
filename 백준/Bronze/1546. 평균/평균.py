#자기 점수 중에 최댓값을 골랐다. 이 값을 M이라고 한다. 그리고 나서 모든 점수를 점수/M*100으로 고쳤다.

n = int(input())
d = list(map(int, input().split()))

avg_list = []
m = max(d)

for i in d :
    avg_list.append(i/m*100)

res = sum(avg_list)/n
print(res)