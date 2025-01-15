import sys
input =sys.stdin.readline
N , L = map(int,input().split())
ans_li=[]

#2개일 때는 3x+(1+2)  4개일때는 4x+(1+2+3) 5개일때는 5x+(1+2+3+4)   n개일때는 (L*x) + ( (0.5(L-1)) + (((L-1)**2)/2))
# 점화식을 대입해서 자연수 x가 나오지 않으면 L을 1씩 증가시키는 방식으로

while True:

    x= float((N - ( float((L-1)/2) + float(((L-1)**2)/2) ))/L) #첫항 계산
    if x%2 == 0 or x%2 == 1 : #첫항이 정수라면 ( 정답이 맞다면 ) 
        for i in range(L):
            ans_li.append(int(x+i)) 

    if len(ans_li)!=0: # ans_li에 x값이 들어갔다는 얘기는 정답을 출력하면 된다는 얘기
        if -1 in ans_li: #음수가 들어가있으면 -1 출력. x의 범위는 0부터이므로 
            print(-1)
            exit()
        else:
            print(*ans_li)
            exit()
    
    L+=1
    if L ==101: #L이 문제에서 정해준 100까지의 범위를 넘게되면 -1출력
        print(-1)
        exit()