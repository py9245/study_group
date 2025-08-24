# 10 : 12 ~ 31

test = int(input())
for t in range(1, test+1):
    box = [0]* 5001
    n = int(input())
    bs = [list(map(int, input().split())) for _ in range(n)]
    p = int(input())
    pl = [int(input()) for _ in range(p)]
    cnt = []
    for a, b in bs:
        for j in set(pl):
            if a <= j <= b:
                box[j] += 1

    for k in pl:
        cnt.append(box[k])
    print(f"#{t} {' '.join(map(str, cnt))}")