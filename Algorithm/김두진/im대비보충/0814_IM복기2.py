T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    A = list(map(int,input().split()))
    B = list(map(int, input().split()))

    current = A[:]
    cnt = 0

    for i in range(N):
        if current[i] != B[i]:
            for j in range(i,N):
                current[j] = 1 - current[j]
            cnt += 1
    print(f'#{test_case} {cnt}')