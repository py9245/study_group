dy = [-1, 1, 0, 0] # 상 하 좌 우
dx = [0, 0, -1, 1]

def get_score(y, x): # score 계산해서 그 결과를 달라
    score = arr[y][x] # 초기화 - 현재좌표

    for i in range(4): # 방향이 4방향이라서 (상, 하, 좌, 우)
        ny, nx = y, x # 현재 위치
        while True:
            ny += dy[i]
            nx += dx[i]
            if 0 <= ny < N and 0 <= nx < N: score += arr[ny][nx] # 점수계산
            else: break # 범위벗어나면 break

    return score


T = int(input())


for tc in range(1, T + 1):
    N = int(input()) # NxN 행렬
    arr = [list(map(int, input().split())) for _ in range(N)] # 2차원 배열
    result = float('-inf')  # 최대값 초기화 (음의 무한대)

    for y in range(N): # 행순회
        for x in range(N):
            # 함수호출하면서 최대값 갱신
            # 함수 왜 만들까?? ---> 디버깅 때문에!!
            temp = get_score(y, x)
            result = max(result, temp)

    print(f'#{tc} {result}') # 최대값 출력

# ---------------------------------------------------------------

dy = [-1, 1, 0, 0] # 상 하 좌 우
dx = [0, 0, -1, 1]

def get_score(y, x): # score 계산해서 그 결과를 달라
    score = arr[y][x] # 초기화 - 현재좌표

    for i in range(4): # 방향이 4방향이라서 (상, 하, 좌, 우)
        ny, nx = y, x # 현재 위치
        while True:
            ny += dy[i]
            nx += dx[i]
            if 0 <= ny < N and 0 <= nx < N: score += arr[ny][nx] # 점수계산
            else: break # 범위벗어나면 break

    return score


T = int(input())


for tc in range(1, T + 1):
    N = int(input()) # NxN 행렬
    arr = [list(map(int, input().split())) for _ in range(N)] # 2차원 배열
    result = float('-inf')  # 최대값 초기화 (음의 무한대)

    for y in range(N): # 행순회
        for x in range(N):
            # 함수호출하면서 최대값 갱신
            # 함수 왜 만들까?? ---> 디버깅 때문에!!
            temp = get_score(y, x)
            result = max(result, temp)

    print(f'#{tc} {result}') # 최대값 출력
