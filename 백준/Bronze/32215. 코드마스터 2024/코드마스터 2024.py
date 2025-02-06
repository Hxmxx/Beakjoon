# 입력 받기
n, m, k = map(int, input().split())

# 도훈이의 설치 횟수
dohun_install = k * m

# 차형준 선생님의 설치 횟수
teacher_install = m

# 총 설치 횟수
total_install = dohun_install + teacher_install

# 결과 출력
print(total_install)
