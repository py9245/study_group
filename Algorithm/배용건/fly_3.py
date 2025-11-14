import sys
sys.stdin = open("in1.txt", "r")

T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())
    fly_list = [list(map(int, input().split())) for _ in range(N)]
    dx = [-1,1,0,0]
    dy = [0,0,-1,1] # 십자가 델타 탐색 좌표 설정
    di = [-1,1,-1,1]
    dj = [-1,-1,1,1] # 엑스자 델타 탐색 좌표 설정
    max_kill = 0 #죽인 최댓값 변수
    for i in range(N): # 행기준 순회
        for j in range(N): # 열기준 순회
            kill = fly_list[i][j] # kill 변수에 리스트 좌표값 할당
            for k in range(4): # 방향 4개 순회
                for dist in range(1,M): # 1~M 전까지 기준으로 순회 (길이) 중심값포함 M이기때문에
                    ni = i + dx[k] * dist
                    nj = j + dy[k] * dist
                    if 0 <= ni < N and 0 <= nj < N:
                        kill += fly_list[ni][nj]
                    else :
                        break # 엘스 잊지말고 브레이크 걸기

            kill_2 = fly_list[i][j]
            for k in range(4):
                for dist in range(1,M):
                    nii = i + di[k] * dist
                    njj = j + dj[k] * dist
                    if 0 <= nii < N and 0 <= njj < N:
                        kill_2 += fly_list[nii][njj]
                    else :
                        break
            max_kill = max(max_kill,kill,kill_2) # max_kill 변수값까지 총 3 변수를 비교해줘야 함
    print(f"#{tc} {max_kill}")

T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())
    fly_list = [list(map(int, input().split())) for _ in range(N)]
    dx = [-1,1,0,0]
    dy = [0,0,-1,1] # 델타탐색 십자 기준 좌표
    di = [-1,1,-1,1]
    dj = [-1,-1,1,1] # 델타탐색 엑스자 기준 좌표
    kill_max = 0 #파리 최대 죽인수
    for i in range(N):
        for j in range(N):
            ten_kill = fly_list[i][j] # 십자로 죽인 파리수
            for k in range(4): # 4방향 순회
                for dist in range(1,M): # 중심값 포함 기준 M (길이)
                    ni = i + dx[k] * dist
                    nj = j + dy[k] * dist
                    if 0 <= ni < N and 0 <= nj < N: # N x N 배열 범위 설정
                        ten_kill += fly_list[ni][nj]
                    else :
                        break

            x_kill = fly_list[i][j] # x자 죽인 파리수
            for k in range(4):
                for dist in range(1,M):
                    nii = i + di[k] * dist
                    njj = j + dj[k] * dist
                    if 0 <= nii < N and 0 <= njj < N:
                        x_kill += fly_list[nii][njj]
                    else :
                        break
            kill_max = max(kill_max,x_kill,ten_kill)
    print(f"#{tc} {kill_max}")


