T = int( input())
for test_case in range(1, T +1):
    n,m = map(int, input().split())
    wi = sorted(list(map(int,input().split())))
    ti = sorted(list(map(int,input().split())))
    cnt = 0

    while ti and wi:
        if ti[-1] >= wi[-1]:
            cnt += wi.pop()
            ti.pop()
        else :
            wi.pop()

    print(f'#{test_case} {cnt}')