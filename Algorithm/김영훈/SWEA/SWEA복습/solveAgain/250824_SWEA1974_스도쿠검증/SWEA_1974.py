# 11:40 ~ 12:24
import sys
sys.stdin = open('C:\\Users\\user\\Desktop\\코딩폴더 깃허브\\김영훈\\algorithm\\SWEA\\SWEA복습\\solveAgain\\250824_SWEA1974_스도쿠검증\\1974_input.txt', 'r')
test = int(input())

for t in range(1, test+1):
    box = [list(map(int, input().split())) for _ in range(9)]
    cnt = 1

    for i in range(9):
        bi = [0]*10
        bj = [0]*10
        for j in range(9):
            bij = box[i][j]
            bji = box[j][i]
            bi[bji] += 1
            bj[bij] += 1
            if bi[bji] != 1 or bj[bij] != 1:
                cnt = 0
                # print(bi[bji], )
                break 

            
            if i % 3 == 0 and j % 3 == 0:
                bk = [0]*10
                for k in range(i, i+3):
                    for l in range(j, j+3):
                        bkl = box[k][l]
                        bk[bkl] += 1
                        # print(bkl, k, l,'dksaldkals')
                        if bk[bkl] != 1:
                            
                            cnt = 0
                            break
        if cnt == 0:
            break
    print(f"#{t} {cnt}")

