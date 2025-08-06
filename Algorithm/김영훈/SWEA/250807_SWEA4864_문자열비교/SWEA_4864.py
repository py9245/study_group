Test = int(input())

for test in range(1, Test+1):
    N = list(input())
    M = list(input())
    cnt = 0
    A = 0
    B = 0

    for m in range(len(M)):
        print(m, cnt, '첫 번째 m, cnt')
        if(M[m] == N[0]):
            print(m, N[0], '두번 째 m')
            if(M[m] == N[cnt]):
                print('2번if')
                A += 1
            else:
                pass
        else:
            cnt += 1
    if(cnt == len(N)):
        B = 1
    print(B)