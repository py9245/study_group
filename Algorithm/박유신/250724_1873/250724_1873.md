T = int(input())  # 테스트 케이스 개수

for t in range(1, T + 1):  # 각 테스트 케이스 처리
    # 전장 크기 입력
    H, W = map(int, input().split())  # H: 높이, W: 너비

    # 전장 정보를 저장할 2차원 리스트 초기화
    board = [[] * W for _ in range(H)]

    # 탱크가 바라보는 방향 문자와 명령 문자 매핑
    dirs = ["^", "v", ">", "<"]  # 탱크 모양(위, 아래, 오른쪽, 왼쪽)
    dirS = ["U", "D", "R", "L"]  # 명령(U, D, R, L)

    # 각 방향에 대한 이동 벡터
    dir = [(-1, 0), (1, 0), (0, 1), (0, -1)]

    cd = 0          # 탱크의 현재 방향 인덱스(0: 위, 1: 아래, 2: 오른쪽, 3: 왼쪽)
    sx, sy = 0, 0   # 탱크의 현재 좌표

    # 전장 정보 읽기
    for i in range(H):
        for j, s in enumerate(input()):
            board[i].append(s)  # 문자 저장
            if s in dirs:       # 탱크 초기 위치라면
                sx, sy = i, j
                cd = dirs.index(s)

    # 명령 입력
    cnt = int(input())  # 명령 개수(사용하지 않아도 무관)
    move = input()      # 명령 문자열

    # 명령 처리
    for s in move:
        if s == "S":  # 포탄 발사 명령
            shx, shy = sx, sy        # 포탄 시작 위치(탱크 위치)
            dx, dy = dir[cd]         # 현재 방향 벡터
            while True:
                nx, ny = shx + dx, shy + dy  # 다음 칸 위치
                # 전장 내부인지 확인
                if 0 <= nx < H and 0 <= ny < W:
                    ns = board[nx][ny]       # 다음 칸의 문자
                    if ns in ".-":          # 평지 혹은 물(통과 가능)
                        shx, shy = nx, ny    # 포탄 이동
                    elif ns == "*":         # 벽돌(파괴 가능)
                        board[nx][ny] = "."  # 벽돌 파괴
                        break               # 발사 종료
                    else:                    # 강철벽 등 기타 장애물
                        break               # 발사 종료
                else:                         # 전장 밖으로 나가면 종료
                    break
        else:  # 이동 명령(U, D, R, L)
            cd = dirS.index(s)        # 방향 전환
            dx, dy = dir[cd]
            nx, ny = sx + dx, sy + dy # 이동할 칸
            if 0 <= nx < H and 0 <= ny < W:  # 전장 내부라면
                ns = board[nx][ny]
                if ns == ".":               # 이동 가능
                    board[nx][ny] = dirs[cd] # 새로운 위치에 탱크 배치
                    board[sx][sy] = "."     # 기존 위치를 평지로 변경
                    sx, sy = nx, ny          # 좌표 갱신
                else:                         # 이동 불가(벽 등)
                    board[sx][sy] = dirs[cd]  # 위치 고정, 방향만 변경
            else:                              # 전장 밖이면 이동하지 않음
                board[sx][sy] = dirs[cd]

    # 결과 출력
    print(f"#{t}", end=" ")
    for i in board:
        print(''.join(i))