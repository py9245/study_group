test = int(input())

for t in range(1, test+1):
    n, k = map(int, input().split())
    box = [list(map(int, input().split())) for _ in range(n)]
    num_garo = 0
    num_sero = 0
    word_cnt = 0
    for i in range(n):
        for j in range(n):
            if box[i][j] == 1:
                num_garo += 1
            elif box[i][j] == 0:
                if num_garo == k:
                    word_cnt += 1
                    num_garo = 0
                num_garo = 0
            if box[j][i] == 1:
               num_sero += 1
            elif box[j][i] == 0:
               if num_sero == k:
                   word_cnt += 1
                   num_sero = 0
               num_sero = 0
        if num_garo == k:
            word_cnt += 1
            num = 0
        if num_sero == k:
            word_cnt += 1
            num = 0
        num_garo, num_sero = 0 ,0
    print(f"#{t} {word_cnt}")