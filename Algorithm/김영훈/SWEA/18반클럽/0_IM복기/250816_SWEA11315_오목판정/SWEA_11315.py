# 08시 25분 ~ 08시 55분

test = int(input())
dx = [-1, -1, -1, 0, 1, 1, 1, 0]
dy = [-1, 0, 1, 1, 1, 0, -1, -1]

for t in range(1, test+1):
    b = int(input())
    box = [list(map(str, input())) for _ in range(b)]
    max_cnt = 0
    for i in range(b):
        for j in range(b):
            

            for k in range(8):  # 방향 탐색 한칸
                nx = i + dx[k]
                ny = j + dy[k]
                cnt = 0
                if 0 <= nx < b and 0 <= ny < b:  # 탐색 범위 제한
                    for nn in range(b):  # 방향으로 오목 탐색
                        nnx = i + dx[k]*nn  # 내 위치 + 방향*nn
                        nny = j + dy[k]*nn
                        if 0 <= nnx < b and 0 <= nny < b:  # 오목 탐색 범위 제한
                            if box[nnx][nny] == 'o':
                                cnt += 1
                                # print(box[nnx][nny])
                                if cnt == 5:
                                    max_cnt += 1
                                    break
                            else:
                                break

    if max_cnt >= 1:
        print(f"#{t} YES")
    else:
        print(f"#{t} NO")        