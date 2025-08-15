import sys
sys.stdin = open("in1.txt", "r")

T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())
    fly_list = [list(map(int, input().split())) for _ in range(N)]
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    di = [-1,1,-1,1]
    dj = [-1,-1,1,1]
    max_kill = 0
    for i in range(N):
        for j in range(N):
            kill = fly_list[i][j]
            for k in range(4):
                for dist in range(1,M):
                    ni = i + dx[k] * dist
                    nj = j + dy[k] * dist
                    if 0 <= ni < N and 0 <= nj < N:
                        kill += fly_list[ni][nj]
                    else :
                        break

            kill_2 = fly_list[i][j]
            for k in range(4):
                for dist in range(1,M):
                    nii = i + di[k] * dist
                    njj = j + dj[k] * dist
                    if 0 <= nii < N and 0 <= njj < N:
                        kill_2 += fly_list[nii][njj]
            max_kill = max(max_kill,kill,kill_2)
    print(f"#{tc} {max_kill}")





