# 사용자로부터 n 입력받기
n = int(input())

# 메모이제이션을 위한 리스트 초기화 (n이 90까지 가능하므로 넉넉하게 91개 생성)
memo = [0] * 91

# 기본값 설정
memo[1] = 1

# 2부터 n까지 차례대로 계산하며 리스트에 저장
for i in range(2, n + 1):
    memo[i] = memo[i-1] + memo[i-2]

# 결과 출력
print(memo[n])