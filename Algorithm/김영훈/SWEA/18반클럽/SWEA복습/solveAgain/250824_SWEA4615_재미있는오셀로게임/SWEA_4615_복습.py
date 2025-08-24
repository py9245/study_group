test = int(input())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for t in range(1, test+1):
    n, m = map(int, input().split())
    box = [[0]*n for _ in range(n)]
    bs = n//2
    box[bs][bs] = 2  # 백
    box[bs-1][bs-1] = 2  # 백
    box[bs][bs-1] = 1  # 흑
    box[bs-1][bs] = 1  # 흑

    for i in range(m):  # 돌 놓는 횟수
        y, h, rock = map(int, input().split())
        h = h-1
        y = y-1
        box[h][y] = rock
        # print(rock)
        for j in range(8):  # 8방향 탐색
            for k in range(1, n):  # 각 방향 직진으로 같은 돌 찾음
                nx = h + dx[j]*k
                ny = y + dy[j]*k
                if 0 <= nx < n and 0 <= ny < n:
                    if box[h][y] == box[nx][ny]:
                        for r in range(k):
                            
                            rx = h +dx[j]*r
                            ry = y +dx[j]*r
                            print(r,'@@@@@@@@@@@')
                            # print(box[rx][ry], '바뀌기 전', rx, ry)
                            # box[rx][ry] = rock
                            # print(rx,'rx', ry, 'ry', nx, ny)
                            # print(box[rx][ry], '바뀐 후')
                            if r + 1 == k:
                                break
                    elif box[h][y] != box[nx][ny]:
                        continue
                    elif not box[nx][ny]:
                        break
                print(k,'##############')
    
    # black_st = list(b.count(1) for b in range(box))
    # white_st = list(b.count(2) for b in range(box))
    # for b in box:
    print(box)
    # print(black_st, white_st)