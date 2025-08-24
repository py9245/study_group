# 3:20분 시작
test = int(input())

for t in range(1, test+1):
    num = int(input())
    num_li = input()
    max_cnt = 0
    cnt = 0
    for n in num_li:
        if n == '0':
            cnt = 0
        elif n == '1':
            cnt += 1
        max_cnt = max(max_cnt, cnt)
    print(f"#{t} {max_cnt}")