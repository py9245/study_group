# 13:03 ~ 27-50 다시

test = int(input())
for t in range(1, test+1):
    n, m = map(int, input().split())
    box = [(input()) for _ in range(n)]
    word = ''
    for i in range(n):  # 10
        for j in range(n-m+1): # 10-10+1
            row = box[i][j:j+m]
            row2 = ''.join(box[k][i] for k in range(j, j+m))
            if row == row[::-1]:
                word = row
                break
            # for k in range(j, j+m):
            #     b += box[k][i]
            if row2 == row2[::-1]:
                word = row2
                break
        if word:
            break
    print(f"#{t} {word}")