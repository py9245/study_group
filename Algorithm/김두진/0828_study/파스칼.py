t = int(input())
for test_case in range(1,t+1):
    # n = int(input())
    # arr = [[0]*n for _ in range(n)]
    # arr[0][0] = 1

    # for i in range(1,n):
    #     for j in range(0,i+1):
    #         if 0 <= i-1 < n and 0 <= j-1 < n:
    #             arr[i][j] += arr[i-1][j-1]
    #         if 0 <= i-1 < n and 0 <= j < n:
    #             arr[i][j] += arr[i-1][j]
    
    # print(f'#{test_case}')
    # for i in range(0,n):
    #     for j in range(0, n):
    #         if arr[i][j] > 0:
    #             print(arr[i][j], end = " ")
    #     print()
    # ----------------------------------------------
    n = int(input())
    arr = [[0]*n for _ in range(n)]
    arr[0][0] =1

    for i in range(1,n):
        for j in range(0,i+1):
            if 0 <= i-1 < n and 0 <= j-1 < n:
                arr[i][j] += arr[i-1][j-1]
            if 0 <= i-1 < n and 0 <= j < n :
                arr[i][j] += arr[i-1][j]
    
    print(f'#{test_case}')
    for i in range(0,n):
        for j in range(0,n):
            if arr[i][j] > 0:
                print(arr[i][j], end = " ")
        print()
