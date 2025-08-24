test = int(input())


for t in range(1, test+1):
    n = int(input())
    box = list(map(int, input().split()))
    mb = max(box)
    room = [[0]*n for _ in range(mb)]
    max_cnt = 0
    for i in range(n):
        if box[i] != 0:
            for j in range(box[i]):
                room[j][i] = 1

    # print(room)
    # 상자만큼 다 1 채워 넣음

    for k in range(n):
        cnt = 0
        if room[0][k] != 0:  # 상자가 있으면 실행
            for l in range(mb):  # 이 상자의 최대값 확인 다음 높이가 0이면 지금 위치 최대
                if room[l][k] < mb or room[l+1][k] == 0:  # 종료 조건
                    for nx in range(k, n):  # cnt
                        # nxk = k + nx
                        if 0 <= nx < n:
                            print(l, nx, room[l][nx])  # l = 상자 높이, nx = 오른쪽 이동, 값
                            print('======')
                            if room[l][nx] != 0:
                                cnt += 1
                            elif room[l][nx] == 0:
                                max_cnt = max(max_cnt, cnt)
                                cnt = 0
    print(max_cnt)
    #
