import sys
sys.stdin = open("1209_input.txt", "r")

for t in range(1, 11):
    test = int(input())
    lrm = 0
    rlm = 0
    max_num = 0
    box = [list(map(int, input().split())) for _ in range(100)]

    for i in range(100):
        ym = 0
        hm = sum(box[i][0:])
        lrm += box[i][i]
        rlm += box[i][99-i]
        for j in range(100):
            ym += box[j][i]

        max_num = max(max_num, hm, ym)
    max_num = max(max_num, lrm, rlm)
    print(max_num)