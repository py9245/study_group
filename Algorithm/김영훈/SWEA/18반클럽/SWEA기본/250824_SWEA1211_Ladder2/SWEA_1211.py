# 12 : 31 ~ 13 : 40(visited 힌트받고 패스)
import sys
sys.stdin = open('C:\\Users\\user\\Desktop\\코딩폴더 깃허브\\김영훈\\algorithm\\SWEA\\SWEA기본\\250824_SWEA1211_Ladder2\\1211_input.txt', 'r')
dxy = [[0, -1], [0, 1], [-1, 0]]
for t in range(1, 11):
    test = int(input())
    box = [list(map(int, input().split())) for _ in range(100)]
    st = []  # 시작 갯수
    for q in range(100):
        if box[0][q] == 1:
            st.append([99, q])
    min_cnt = float('inf')  # 사다리 타는 횟수
        # 만약 이거보다 크면 컨티뉴

    for h, y in st:
        visited = [[0]*100 for _ in range(100)]
        visited[h][y] = 1
        cnt = 0
        
        while h != 0:
            # print(h, y)
            for dx, dy in dxy:
                hx = h + dx  # 다음 행 이동좌표
                yx = y + dy  # 다음 열 이동좌표
                if 0 <= hx < 100 and 0 <= yx < 100 and box[hx][yx] == 1 and visited[hx][yx] == 0:
                    h = hx  # 행 초기화
                    y = yx  # 열 초기화
                    cnt += 1  
                    visited[hx][yx] = 1  # 방문 횟수 카운트
            # if cnt >= min_cnt:  # 이동횟수가 최소 이동횟수보다 작으면 브레이크
            #     break
        min_cnt = min(min_cnt, cnt)
        if min_cnt == cnt:
            ydx = yx
            # print('==================================')
    print(f"#{t} {ydx}")
        
                    
