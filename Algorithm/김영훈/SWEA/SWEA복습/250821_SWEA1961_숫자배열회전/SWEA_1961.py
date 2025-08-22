# 11:28분 시작
import sys
sys.stdin = open("1961_input.txt", "r")

test = int(input())

# for t in range(1, test+1):
#     n = int(input())

    # box = [list(input().split()) for _ in range(n)]
    # box_90 = list(map(list, zip(*box[::-1])))
    # box_180 = list(map(list, zip(*box_90[::-1])))
    # box_270 = list(map(list, zip(*box)))[::-1]
    # print(f"#{t}")
    # for i in range(n):
    #     row_90 = ''.join(box_90[i])
    #     row_180 = ''.join(box_180[i])
    #     row_270 = ''.join(box_270[i])
    #     print(row_90, row_180, row_270)


for t in range(1, test+1):
    n = int(input())

    box = [list(input().split()) for _ in range(n)]
    no_box = [[[] for _ in range(n)] for _ in range(n)]
    # no_box[0][0]+= '1'
    # print(no_box)
    box_90 = list(map(list, zip(*box[::-1])))
    box_180 = list(map(list, zip(*box_90[::-1])))
    box_270 = list(map(list, zip(*box)))[::-1]

    # print(box_90)
    # print(box_180)
    # print(box_270)
    for i in range(n):
        for j in range(n):
            if j == 0:
                for k in range(n):
                    no_box[j][i] += box_90[i][k]
                    # print(box_90[j][k])

            elif j == 1:
                for k in range(n):
                    no_box[j][i] += box_180[i][k]
            elif j == 2:
                for k in range(n):
                    no_box[j][i] += box_270[i][k]

    no_box = list(map(list, zip(*no_box)))

    for nb in no_box:
        for n in nb:
            if n == ['9','6','3']:
                print("여기다")
            print(''.join(n), end=" ")
        print()
    # a = ''.join(map(str, no_box))
    # # print(a)
