import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    money = int(input())
    money_list = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    money_cnt = [0] * len(money_list)
    mon = money
    for i in range(len(money_list)):
        if mon >= money_list[i]:
            money_cnt[i] = mon // money_list[i]
            mon = mon % money_list[i]
    print(f"#{tc}")
    print(*money_cnt)