T = int(input())
for test_case in range(1,T+1):
    N,K = map(int,input().split())
    arr = list(map(int,input().split()))
    arr.sort()
    max_len = 0
    for i in range(N):
        num_lst = []
        num_lst.append(arr[i])
        for j in range(i+1,N):
            if arr[j] - arr[i] <= K:
                num_lst.append(arr[j])
        max_len = max(len(num_lst),max_len)
    # print(num_lst)
    print(f'#{test_case} {max_len}')