V = int(input())  # 심사위원 수 입력
votes = input().strip()  # 투표 결과 입력

# A와 B의 투표 수 세기
count_A = votes.count('A')
count_B = votes.count('B')

# 결과 출력
if count_A > count_B:
    print("A")
elif count_B > count_A:
    print("B")
else:
    print("Tie")