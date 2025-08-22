# import sys
# sys.stdin = open("1979_input.txt", "r")
# 8시 20분 시작
# 8시 50분 끝(패스)

test = int(input())

for t in range(1, test+1):
    n, m = map(int, input().split())
    box = [list(map(int, input().split())) for _ in range(n)]
    word_cnt = 0

    box2 = list(map(list, zip(*box)))
    # for c_box in [box, box2]:

    for i in range(n):
        cnt = 0
        cnt_2 = 0
        for j in range(n):

            if box[i][j] == 1:
                cnt += 1
            elif box[i][j] == 0:
                if cnt == m:
                    # print(i, j)
                    word_cnt += 1
                    cnt = 0
                cnt = 0

            if j == n-1:
                if cnt == m:
                    # print(i, j)
                    word_cnt += 1
                    cnt = 0
                cnt = 0

            if box2[i][j] == 1:
                cnt_2 += 1
            elif box2[i][j] == 0:
                if cnt_2 == m:
                    # print(i, j)
                    word_cnt += 1
                    cnt_2 = 0
                cnt_2 = 0

            if j == n-1:
                if cnt_2 == m:
                    # print(i, j)
                    word_cnt += 1
                    cnt_2 = 0
                cnt_2 = 0

    print(f"#{t} {word_cnt}")