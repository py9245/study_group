# 9시 18분 시작
#48분 
# 12:51분 정답보기
# 12:59분 다시 시작
# 1:16분
# import sys
# sys.stdin = open("4828_input.txt", "r")

test = int(input())

for t in range(1, test+1):
    k, n, m = map(int,input().split())
    bus_st = set(map(int, input().split()))
    charge = [0]*(n+1)
    cnt = 0
    for c in bus_st:
        charge[c] = c
    i = 0
    while i+k < n:
        nc = i + k
        
        while nc > i and nc not in bus_st:
            nc-=1
        if nc == i:
            cnt = 0
            break
        i = nc
        # print(i, 'dijasoidjasoi')
        cnt += 1
    print(f"#{t} {cnt}")
        



