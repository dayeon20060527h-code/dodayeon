INF = int(1e9)
N, M = map(int, input().split())

# 2차원 배열 초기화
graph = [[INF] * (N + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    graph[i][i] = 0

# 도로 정보 입력
for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

X, K = map(int, input().split())

# 플로이드-워셜 핵심 로직
for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

# 최종 결과 계산
distance = graph[1][X] + graph[X][K]

if distance >= INF:
    print("-1")
else:
    print(distance)