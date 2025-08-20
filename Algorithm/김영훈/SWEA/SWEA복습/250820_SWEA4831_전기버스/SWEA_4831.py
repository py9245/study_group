# 9시 18분 시작
#48분 정답보기
test = int(input())

for t in range(1, test+1):
    k, n, m = map(int,input().split())
    bus_st = list(map(int, input().split()))
    charge = [0]*(n+1)
    cnt = 0
    for c in bus_st:
        charge[c] = c

    # for i in range(len(charge)):
    #     if charge[i+k] != 0:
    #         cnt += 1
    #     elif charge[:i+k] != 0:
    #         cnt += 1
    i = 0
    while True:
        # if i+k <= n:
        if n-m+1<= i:
            break
        if charge[i+k] != 0:
            cnt += 1
            i = k
        elif charge[i+k] == 0:
            for j in range(i+k, i, -1):
                if j != 0:
                    i = j
                    cnt += 1
        print(cnt)
        



