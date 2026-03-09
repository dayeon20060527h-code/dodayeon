# 크기를 입력받습니다
n = int(input()) 
plans = input().split() 

# 변수 x와 y를 이용해서 시작 위치를 설정합니다.
x, y = 1, 1

# 수평방향으로 이동했을때 Y(열)위치의 변화와 수직방향으로 이동했을 때 x(행)위치의 변화를 list를 이용하여 정의합니다.
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']


for plan in plans:
    # 루프 시작 시점에 nx, ny를 현재 위치(1,1)로 초기화해둡니다.
    # 이렇게 하면 아래 if문에 안 걸리더라도 nx, ny 변수가 존재하지 않는 에러가 안 납니다.
    nx, ny = x, y 
    
    # 이동 후 좌표 구하기
    for i in range(len(move_types)): #i의 범위를 move_types의 길이(0~3)까지로 제한합니다
        if plan == move_types[i]: 
            nx = x + dx[i]
            ny = y + dy[i]
    
    if nx < 1 or ny < 1 or nx > n or ny > n: #좌표 이동 후 처음에 설정한 공간에서 벗어나는지 확인합니다.
        continue
    
    # 변화한 좌표를 처음 설정했던 위치 변수에 입력합니다.
    x, y = nx, ny

# 최종 결과를 출력합니다
print(x, y)