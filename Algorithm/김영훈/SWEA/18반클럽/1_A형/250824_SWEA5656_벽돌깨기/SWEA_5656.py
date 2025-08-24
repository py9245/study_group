# 15 : 35

from collections import deque
import sys
sys.stdin = open('C:\\Users\\user\\Desktop\\코딩폴더 깃허브\\김영훈\\algorithm\\SWEA\\18반클럽\\1_A형\\250824_SWEA5656_벽돌깨기\\5656_input.txt','r')


T = int(input())

for tc in range(1, T+1):
    n, w, h = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(h)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    min_num = 10**10

    def bomb(x, y, bd):  # 벽돌 숫자만큼 깨지는 함수
        dq = deque()
        dq.append((x, y))  # dq에 튜플로
        while dq:  # dq 있으면:
            bx, by = dq.popleft()  # dq 첫번째꺼부터
            k = bd[bx][by]  # 벽돌의 값
            bd[bx][by] = 0  # 깼으니까 0으로 바꿈
            for ii in range(1, k):  # 값만큼 진행
                for d in range(4):  # 방향
                    nx = bx + (dx[d] * ii)
                    ny = by + (dy[d] * ii)
                    if not (0 <= nx < h and 0 <= ny < w):  # 범위 밖이면
                        continue
                    if bd[nx][ny] > 0:  # 연쇄반응으로 깨질 벽돌도 넣음
                        dq.append((nx, ny))
                        # 일단 처음 깨지기 시작한 벽돌(for문)부터 다 깨고
                        # 다음 while문에서 연쇄반응할 dq 있으면 다시 시작

    def gravity(bd):  # 중력
        for ii in range(w):  # w = 가로
            new_list = []
            for jj in range(h-1, -1, -1):  # h = 세로
                if bd[jj][ii]:  # 열 값이 있으면
                    new_list.append(bd[jj][ii])  # 뉴리스트에 값 넣음
                    bd[jj][ii] = 0  # 그러고 초기화
                if new_list:  # 뉴 리스트 값 있으면
                    for kk in range(len(new_list)):  # 뉴리스트길이만큼 kk
                        bd[h-kk-1][ii] = new_list[kk] 
                        # h(세로)-1(인덱스)-kk(0부터) = 뉴리스트[kk](0번부터)
                        # 맨 왼쪽(ii), 맨 아래(h-kk-1)부터 값 넣음
    
    def dfs(shoot, brick_bd):  # ???
        global min_num  
        
        if shoot == n + 1:  # 공 다 쏘면 벽돌 갯수 카운팅
            ans = 0
            for i in range(h):  # 세로
                for j in range(w):  # 가로
                    if brick_bd[i][j]:  # 값 있으면
                        ans += 1
            min_num = min(min_num, ans)
            return
        
        for i in range(w):
            new_bd = [val[:] for val in brick_bd]
            # brick_bd = box ,  val = 행, new_bd = new_bd = brick_bd
            # 행 바뀔때마다 계속 전체 초기화 ??
            for j in range(h):
                if new_bd[j][i]:
                    bomb(j, i, new_bd)  # 값이 있어서 쏨
                    gravity(new_bd)  # 중력 작용
                    dfs(shoot + 1, new_bd)  
                    break
            else:
                dfs(shoot + 1, new_bd)  # for 정상이면 다시

    dfs(1, board)  # ???

    print(f"#{tc} {min_num}")