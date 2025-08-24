import sys
sys.stdin = open("1974_input.txt", "r")

test = int(input())
for t in range(1, test + 1):
    sdok = [list(map(int, input().split())) for _ in range(9)]
    cnt = 1
    for i in range(9):
        box_l = [0]*10
        box_j = [0]*10

        for l in range(9):  # 행이동
            box_l[sdok[i][l]] += 1

        for j in range(9):  # 열이동
            box_j[sdok[j][i]] += 1

        for e in range(1, 10):
            if box_l[e] != 1 or box_j[e] != 1:
                cnt = 0
                break

        for k in range(9):
            if i % 3 == 0 and k % 3 == 0:
                box_k = [0] * 10
                for q in range(i, i+3):
                    for w in range(k, k+3):
                        box_k[sdok[q][w]] += 1
                for r in range(1, 10):
                    if box_k[r] != 1:
                        cnt = 0
                        break

    print(f"#{t} {cnt}")