test = int(input())
dx = [-1, 1, 0, 0,-1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, 1, -1]
for t in range(1, test+1):
    n, m = map(int, input().split())
    box = [[0]*n for _ in range(n)]
    mid = n//2 - 1
    middd = mid + 1
    box[mid][mid] = 2  # 백돌
    box[mid][middd] = 1  # 흑돌
    box[middd][mid] = 1
    box[middd][middd] = 2    
    white = 0
    black = 0
    # print(box)
    for i in range(m):  # 돌 놓는 횟수 12번
        
        yeol, hang, rock = map(int, input().split())  # 양 옆, 위 아래
        y = yeol -1  # y = 좌 우
        h = hang-1  # h = 상 하
        box[h][y] = rock

        for j in range(8):  # 십자 돌 확인
            for a in range(1, n):  # 같은 거 있는 지 확인 a = 시작점부터 끝 점 길이까지 범위
                                    # 자기 자신 바로 만나버리면 실행하니까 1부터 시작
                hx = h + dx[j]*a  # hx = 상하 + 방향
                yy = y + dy[j]*a  # yy = 좌우 + 방향
                if 0 <= hx < n and 0 <= yy < n:                  
                    if rock == box[hx][yy]:  # 탐색했는데 같으면
                        for b in range(a-1 , 0, -1):
                            rx = h + dx[j]*b
                            ry = y + dy[j]*b
                            box[rx][ry] = rock
                        
                        break  # 범위까지 바꿨으면 다음 방향
                    elif not box[hx][yy]:  # 비었으면
                        break
        # print(box)        
    
    for color in box:
        white += color.count(2)
        black += color.count(1)
        # print(color)
    print(f"#{t} {black} {white}")