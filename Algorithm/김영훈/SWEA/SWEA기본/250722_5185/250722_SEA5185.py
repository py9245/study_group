T = int(input())

for t in range(T):
    N = list(map(str, input().split()))
    A = int(N[1],16)
    B = bin(A)[2:]
    if len(B)<int(N[0])*4:
        print(f'#{t+1}','0',end = B)
        print()
    else:
        print(f'#{t+1}', B)



### 10진수, 2진수 변환 방법을 알게됐습니다.