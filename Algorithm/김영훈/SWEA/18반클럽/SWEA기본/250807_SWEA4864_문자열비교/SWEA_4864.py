Test = int(input())

for test in range(1, Test+1):
    N = input()
    M = input()
    A = 0

    if(N in M):
        A = 1
    else:
        pass
    print(f"#{test} {A}")
    

    # for m in range(len(M)):
        
    #     print(m, cnt, '첫 번째 m, cnt')
    #     if(M[m] == N[0]):
    #         print(m, N[0], '두번 째 m')
    #         if(M[m] == N[cnt]):
    #             print('2번if')
    #             cnt += 1
    #         else:
    #             pass
    #     else:
    # if(cnt == len(N)):
    #     B = 1
    # print(B)