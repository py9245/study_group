# 14: 05 ~ 14 : 41
import sys
sys.stdin = open('C:\\Users\\user\\Desktop\\코딩폴더 깃허브\\김영훈\\algorithm\\SWEA\\SWEA복습\\solveAgain\\250824_SWEA5202_화물도크\\5202_input.txt', 'r')

test = int(input())

for t in range(1, test+1):
    n = int(input())
    box = [list(map(int, input().split())) for _ in range(n)]
    box.sort(key = lambda x: x[1])
    # print(box)
    cnt = 1
    b = 0
    max_num = max(box[i][0] for i in range(n))
    # print(max_num)
    while True:
        for i in range(b, n):

            if box[b][1] <= box[i][0]:
                cnt += 1
                b = i
                # print(cnt,'cnt')
                break
        if box[b][1] > max_num:
            break
        # print(b, i, box)
            # if box[b][1] == max(box[b:][1]):
            #     break
        # print(b,'b')
    print(f"#{t} {cnt}")