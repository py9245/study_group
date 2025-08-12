T = int(input())
for test_case in range(1,T+1):
    # 스위치를 언제 바꿀까? 
    # 현재상태와 B의 상태가 다를 때 바꾸면 된다. -> 그리디
    N = int(input())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))

    
    cnt = 0

    for i in range(N):
        if A[i] != B[i]: # 현재 상태와 B의 상태가 다르다면
            for j in range(1, N): # i부터 끝까지 바꾼다.
                A[j] = 1 - A[j]
            cnt += 1

    print(f'#{test_case} {cnt}')