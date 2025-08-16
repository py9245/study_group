T = int(input())
for test_case in range(1,T+1):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    cnt = 0

    for i in range(n):
        if a[i] != b[i]:
            for j in range(1,n):
                a[j] = 1 - a[j]
            cnt += 1
    print(f'#{test_case} {cnt}')