# 3:35 ~ 4:30 (패스)
import sys
sys.stdin = open("C:\\Users\\user\\Desktop\\코딩폴더 깃허브\\김영훈\\algorithm\\SWEA\\SWEA복습\\250823_SWEA1210_Ladder1\\input.txt", "r")
dxy = [[0, -1], [0, 1], [-1, 0]]


for t in range(1, 11):
    T = int(input())
    box = [list(map(int, input().split())) for _ in range(100)]
    s = []
    for i in range(100):
        for j in range(100):
            if box[i][j] == 2:
                s.append([i, j])
                break
    # print(s)
    sh = s[0][0]
    sy = s[0][1]
    # print(sh, sy)
    # =============================================
    st = sh, sy
    # for i in range(100):
    #     for j in range(100):
    cnt =0
    while True:
        box[sh][sy] = 0  # 2의 위치
        cnt += 1
        
        for h, y in dxy:
            shh = sh + h
            shy = sy + y
            # cnt += 1
            if 0 <= shh < 100 and 0 <= shy < 100:
                if box[shh][shy] == 1:
                    sh = shh
                    sy = shy
                    break
        
        if sh == 0:
            break
    # =============================================

    print(f"#{T} {sy}")