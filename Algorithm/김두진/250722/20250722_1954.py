T = int(input())
di = [0, 1, 0, -1]
dj = [1,0,-1,0]
for test_case in range(1, T + 1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]


    i,j,cnt, dr = 0,0,1,0 # 초기화  dr = 방향 인덱스(0이면 오른쪽)
    arr[i][j] = cnt
    cnt += 1

    while cnt <= N*N: # cnt가 N*N하고 같거나 작을때까지 무한루프 돌리기
        ni, nj = i+di[dr], j+dj[dr] # 하나식 이동하는 로직 16번줄에 할당
        if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 0: # 다음 칸이 갈 수 있는지 확인. 현재 ni,nj가 0이상 N 미만 숫자가 안들어간 칸 arr[ni][nj] == 0 일 때
            i, j = ni, nj   # 현재 위치를 옮기고
            arr[i][j] = cnt # 숫자를 채우고
            cnt += 1        # 숫자를 올림
        else:
            dr = (dr+1) % 4 # 못 가면 방향을 바꿈. dr -> 0-1-2-3 다시 0 반복

    print(f'#{test_case}')
    for lst in arr:
        print(*lst) #언패킹하여 개별 문자들을 출력함