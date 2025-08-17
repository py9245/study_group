# 델타탐색 , 상하좌우만, 
# 현재 있는 곳에서 더 낮은 고도의 칸으로만 이동
# 특성상 , 이동할 수 있는 낮은 고도의 칸은 최대 한개.
# 더 이상 이동할 수 없을 때까지 이동
# 첫번째 지도 크기 N
# 두번째 시작지점 좌표, 공백으로 입력
# N개의 줄에 걸쳐 고도 정보를 공백으로 입력

# T = int(input())
# dxy = [[1,0],[-1,0],[0,1],[0,-1]]
# for test_case in range(1,T+1):
#     N= int(input())
#     start_r, start_c = map(int,input().split())
#     arr = [list(map(int,input().split())) for _ in range(N)]
#     total_count = 1

#     current = arr[start_r][start_c]
#     for i in range(N):
#         for j in range(N):

#             for dx,dy in dxy:
#                 ni = start_r + dx
#                 nj = start_c + dy
#                 if 0 <= ni < N and 0 <= nj < N:
#                     if arr[ni][nj] < arr[start_r][start_c]:
#                         current = arr[ni][nj]
#                         total_count += 1
#             break
#     print(f'#{test_case} {total_count}')



# ------------------------------------------------------------
T = int(input())
dxy = [[1,0],[-1,0],[0,1],[0,-1]]
for test_case in range(1,T+1):
    N= int(input())
    start_r, start_c = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    total_count = 1

    x, y = start_r, start_c
    while True:
        current_num = arr[x][y]
        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < N:
                next_num = arr[nx][ny]
                if next_num < current_num:
                    x, y = nx, ny
                    total_count += 1
                    break
        else:
            break
    print(f'#{test_case} {total_count}')
