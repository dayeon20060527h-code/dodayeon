# N과 K 입력 받기
n, k = map(int, input().split())

# 배열 A 입력 받기
a = list(map(int, input().split()))

# 배열 B 입력 받기
b = list(map(int, input().split()))

# 1. A는 오름차순 (작은 게 앞으로)
a.sort()
# 2. B는 내림차순 (큰 게 앞으로)
b.sort(reverse=True)

# 최대 K번 비교하며 교체
for i in range(k):
    # A의 원소가 B의 원소보다 작을 때만 교체
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        # A가 더 크거나 같으면 더 이상 이득이 없으므로 중단
        break

# 최종 합계 출력
print(sum(a))