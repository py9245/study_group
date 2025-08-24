# 1:56 시작
# + 10
import sys
sys.stdin = open("4861_input.txt", "r")

# 111111111111
# test = int(input())
#
# for t in range(1, test+1):
#     n, m = map(int, input().split())
#     box = [input() for _ in range(n)]
#     # print(box)
#     word = ''

    # print(m//2)
    # for i in range(n):
    #     for j in range(n-m+1):
    #         cnt = 0
    #         cnt2 = 0
    #         for k in range(m//2):
    #             jmk = j+m-k-1
    #             if 0 <= j+k < n and 0 <= jmk < n:
    #                 if j+k < j+m-k-1:
    #                     if box[i][j+k] == box[i][jmk]:
    #                         cnt += 1
    #                     elif box[i][j+k] != box[i][jmk]:
    #                         break
    #         else:
    #             if cnt == m//2:
    #                 for l in range(j, j+m):
    #                     word += box[i][l]
    #
    #         for k in range(m//2):
    #             jmk = j+m-k-1
    #             if 0 <= j+k < n and 0 <= jmk < n:
    #                 if j+k < j+m-k-1:
    #                     if box[j+k][i] == box[jmk][i]:
    #                         cnt2 += 1
    #                     elif box[j+k][i] != box[jmk][i]:
    #                         break
    #         else:
    #             if cnt2 == m//2:
    #                 for l in range(j, j+m):
    #                     word += box[l][i]
    #
    # print(f"#{t} {word}")
 # 222222222222
test = int(input())

for t in range(1, test + 1):
    n, m = map(int, input().split())
    box = [input() for _ in range(n)]
    # print(box)
    word = ''
    word2 = ''
    for i in range(n):
        for j in range(n-m+1):
            row = box[i][j:j+m]
            row2 = ''.join(box[k][i] for k in range(j, j+m))
            if row == row[::-1]:
                word = row
                break
            if row2 == row2[::-1]:
                word = row2
                break
        if word:
            break
    print(f"#{t} {word}")

