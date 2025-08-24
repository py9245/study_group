# 3시20 ~ 3시 35
test = int(input())

for t in range(1, test+1):
    n = int(input())
    bef = list(map(int, input().split()))
    aft = list(map(int, input().split()))
    cnt = 0

    for i in range(n):
        if aft[i] != bef[i]:
            cnt += 1
            for j in range(i, n):
                if bef[j] == 1:
                    bef[j] = 0
                elif bef[j] == 0:
                    bef[j] = 1
    print(f"#{t} {cnt}")