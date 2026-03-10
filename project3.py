from collections import deque

# N, M 입력받기
n, m = map(int, input().split())

# 미로 정보 입력받기 (2차원 리스트)
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 이동할 네 가지 방향 정의 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque()
    queue.append((x, y))

    # 큐가 빌 때까지 반복
    while queue:
        x, y = queue.popleft()

        # 현재 위치에서 4가지 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 미로 찾기 공간을 벗어난 경우 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            
            # 괴물이 있는 부분(0)은 무시
            if graph[nx][ny] == 0:
                continue

            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1:
                # 이전 노드의 거리 값에 1을 더해 현재 노드에 저장
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    
    # 가장 오른쪽 아래(탈출구)까지의 최단 거리 반환
    return graph[n - 1][m - 1]

# BFS 수행 결과 출력 (시작 위치는 0,0)
print(bfs(0, 0))