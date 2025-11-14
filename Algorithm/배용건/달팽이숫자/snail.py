# 달팽이 숫자
import sys
sys.stdin = open(".txt","r")

T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    arr = [[0] * n for _ in range(n)]
    delta = [(0,1),(1,0),(0,-1),(-1,0)] # 우 하 좌 상
    #현재 위치
    i, j = 0, 0

    # 넣어줄값 , 2부터 시작
    cnt = 2

    #시작점 (0,0)에 1 넣기
    arr[0][0] = 1

    #모든 칸에 (N * N)을 다 채울 때까지 반복
    while cnt <= n * n :
        # 4가지 방향을 정해놓은대로 우 하 좌 상 순서대로 진행
        for di, dj in delta:
            ni, nj = di + i, dj + j
            # 인덱스가 유효하고 0으로 빈 칸이라면
            while 0 <= ni < n and 0 <= nj < n and arr[ni][nj] == 0:
                arr[ni][nj] = cnt
                i, j = ni, nj
                ni += di
                nj += dj
                cnt += 1
    print(f"#{tc}")
    for row in arr:
        print(*row)

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]
    delta = [(0,1),(1,0),(0,-1),(-1,0)]
    i, j = 0, 0
    cnt = 2
    arr[0][0] = 1


    
    while cnt <= N * N :
        for di, dj in delta:
            ni, nj = di + i, dj + j
            while 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 0:
                arr[ni][nj] = cnt
                i, j = ni, nj
                ni += di
                nj += dj
                cnt += 1
    print(f"#{tc}")
    for d in arr:
        print(*d)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]
    delta = [(0,1), (1,0), (0,-1), (-1,0)]
    i, j = 0, 0
    cnt = 2
    arr[0][0] = 1

    while cnt <= N * N :
        for di, dj in delta:
            ni, nj = di + i, dj + j
            while 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 0:
                arr[ni][nj] = cnt
                i, j = ni, nj
                ni += di
                nj += dj
                cnt += 1
    print(f"#{tc}")
    for d in arr:
        print(*d)
