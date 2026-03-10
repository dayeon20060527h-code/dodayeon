import sys

# 입력된 모든 값을 공백/줄바꿈 기준으로 분리
data = sys.stdin.read().split()

# 첫 번째 값: N, 두 번째 값: M
n = int(data[0])
m = int(data[1])

# 세 번째 값부터 끝까지: 떡의 높이들
heights = list(map(int, data[2:]))

# 이진 탐색 범위 설정
start = 0
end = max(heights)

result = 0

# 이진 탐색 (Binary Search) 수행
while start <= end:
    mid = (start + end) // 2
    
    # 절단기 높이(mid)로 잘랐을 때 가져갈 수 있는 떡의 길이 합 계산
    total = 0
    for h in heights:
        if h > mid:
            total += (h - mid)
            
    # 가져갈 떡의 길이가 충분한 경우: 
    # 더 높게 자를 수 있는지 확인하기 위해 결과를 기록하고 오른쪽 탐색
    if total >= m:
        result = mid
        start = mid + 1
    # 길이가 부족한 경우: 더 많이 가져가야 하므로 낮게 잘라야 함 (왼쪽 탐색)
    else:
        end = mid - 1

print(result)