# 델타 탐색 (풍선팡)

T = int(input())
for tc in range(1,T+1):
    N , M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    max_value = 0

    for i in range(N):
        for j in range(M):

            num = matrix[i][j]

            for k_num in range(4):
                for k in range(1,matrix[i][j]+1):

                    ni = i + dx[k_num] * k
                    nj = j + dy[k_num] * k

                    if 0 <= ni < N and 0 <= nj < M:
                        num += matrix[i][j]
                    else:
                        break
            if num > max_value:
                max_value = num
    print(f"#{tc} {max_value}")




    #두번째 연습

    T = int(input())
    for tc in range(1,T+1):
        N , M = map(int, input().split())
        matrix = [list(map(int, input().split())) for _ in range(N)]

        dx = [-1,1,0,0]
        dy = [0,0,-1,1]

        max_value = 0

        for i in range(N):
            for j in range(M):

                num = matrix[i][j]
                for kk in range(4):
                    for k in range(1,matrix[i][j]+1):
                        ni = i + dx[kk] * k
                        nj = j + dy[kk] * k
                        if 0 <= ni < N and 0 <= nj < M:
                            num += matrix[ni][nj]
                if num > max_value:
                    max_value = num
        print(f"#{tc} {max_value}")



# 3번째 연습
T = int(input())
for tc in range(1,T+1):
    N , M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    max_value = 0
    for i in range(N):
        for j in range(M):

            num = matrix[i][j]
            for kk in range(4):
                for k in range(1,matrix[i][j]+1):
                    x = i + dx[kk] * k
                    y = j + dy[kk] * k
                    if 0 <= x < N and 0 <= y < N:
                        num += matrix[x][y]
            if num > max_value:
                max_value = num
    print(f"#{tc} {max_value}")



