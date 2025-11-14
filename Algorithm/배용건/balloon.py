import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test in range(1,T+1):
    N, M = map(int, input().split())
    matrix = []
    for _ in range(N):
        matrix.append(list(map(int, input().split()))) # 2차원 리스트 만들기


    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1] # dx,dy 는 방향
    dirt_max = 0
    for i in range(N):
        for j in range(M):
            dirt_sum = 0

            for k in range(4):
                ni = i + dx[k]
                nj = j + dy[k]
                if 0 <= ni < N and 0 <= nj < M:
                    dirt_sum += matrix[ni][nj]
            dirt_sum += matrix[i][j]
            if dirt_sum > dirt_max:
                dirt_max = dirt_sum

    print(f'#{test} {dirt_max}')