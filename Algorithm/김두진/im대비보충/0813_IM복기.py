T = int(input())
dxy = [[0,1],[0,-1],[1,0],[-1,0]] # 델타탐색 방향 코드 

for test_case in range(1,T+1):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]
    count = 0 # 이동한 거리 카운트 
    idx = []    # 시작점 인덱스 저장배열
    start_ar = 0    # 시작점 벨류값 저장소

    # ----시작지점 찾는 코드---------------------
    for i in range(n):
        for j in range(n):
            if arr[i][j] > start_ar:    # 시작점 위치 선정 시작
                start_ar = arr[i][j]    # 현재 위치로 시작점 재할당
                idx = [(i,j)]   # 현재 위치의 인덱스 할당
            elif arr[i][j] == start_ar:     # 현재 위치랑 시작점이 같으면 idx배열에 추가
                idx.append((i,j))
    # ----시작지점 찾는 코드--- 끝---------------------
    # ----방문한 총 칸의 최대 개수 구하는 코드----------
    for x,y in idx: # 인덱스 저장소에서 하나씩 가져옴 
        cnt = 0 # 임시 거리 저장 
        while True:
            cnt += 1    # 시작점부터 1세니까 시작 시 1증가
            num = arr[x][y] # 작은 인덱스를 저장하기 위해 임시로 보관 해둔 변수
            min_num = num   # 현재 값을 min_num에 임시 할당 
            mx, my = -1, -1     # 임시 선언
            for dx, dy in dxy:  # 델타 탐색 시작
                nx,ny = x + dx, y + dy  # 현재 위치 인덱스에 델타 방향 더하기
                if 0 <= nx < n and 0 <= ny < n: # 델타 방향 더한 인덱스의 범위
                    n_num = arr[nx][ny] # 옮긴 위치랑 min_num이랑 비교하기 위해 임시 저장
                    if min_num > n_num: # min_num이 n_num보다 크면 
                        mx,my = nx,ny   # mx,my에 할당
                        min_num = n_num # min_num은 ni,ny 좌표 할당 
            if min_num == num:  # min_num이 현재 위치랑 같다면 반복문 탈출
                break
            else:
                x,y = mx,my # 인접한 것들 중 작은 것이 있다면 , x,y에 할당 
        if cnt > count: # 임시 거리 저장이 count 보다 크다면
            count = cnt     # 총 이동거리에 임시거리 할당
    print(f'#{test_case} {count}')
    # ----방문한 총 칸의 최대 개수 구하는 코드---끝------



    # ------------------------------------------------
    # for i in range(n):
    #     for j in range(n):
    #         max_count = 0
    #         c_count = 1
    #         current = arr[i][j]
    #         for dx,dy in dxy:
    #             ni = i + dx
    #             nj = j + dy
    #             if 0 <= ni < n and 0 <= nj < n :
    #                 current = arr[ni][nj]
    #                 c_count += 1
    #             max_count = max(c_count,max_count)
                        
    #                 # if arr[i][j] > arr[ni][nj] > arr[i+1][j+0]:
    #                 #     current = arr[ni][nj]
    #                 #     c_count += 1
    #                 # max_count = max(c_count,max_count)
            
                
    # print(f'#{test_case} {max_count}')
    # ----------------------------------------------------------------