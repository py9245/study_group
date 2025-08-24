test = int(input())

for t in range(1, test+1):
    n = int(input())
    c = list(map(int, input().split()))
    max_cnt = 0
    cnt = 1
    for i in range(n):

        if 0 <= i+1 < n:
            if c[i] < c[i+1]:
                cnt += 1
                # print('증가', cnt)
            elif c[i] >= c[i + 1]:
                cnt = 1
                # print('감소')
        max_cnt = max(max_cnt, cnt)

    print(f"#{t} {max_cnt}")

