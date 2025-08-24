test = int(input())

for t in range(1, test+1):
    num = int(input())
    mum = input()
    a = list(map(int, mum))
    # max_num = max(a)
    # b = a.count(max_num)
    max_cnt = 0
    cnt = 0
    b = 0
    for i in a:
        cnt = a.count(i)
        max_cnt = max(max_cnt, cnt)
        if max_cnt == cnt:
           b = max(b, i)
    print(f"#{t} {b} {max_cnt}")

# 3
# 5
# 49679
# 5
# 08271
# 10
# 7797946543