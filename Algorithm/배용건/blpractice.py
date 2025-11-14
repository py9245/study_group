T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    bl_list = [list(map(int, input().split())) for _ in range(N)]
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    max_num = 0

    for i in range(N):
        for j in range(M):
            num = bl_list[i][j]
            for k in range(4):
                ni = i + dx[k]
                nj = j + dy[k]
                if 0 <= ni < N and 0 <= nj < M:
                    num = bl_list[ni][nj]
                else:
                    break
            max_num = max(num, max_num)
    print(f"#{tc} {max_num}")