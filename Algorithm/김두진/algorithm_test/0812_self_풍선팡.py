T = int(input())
for test_case in range(1,T+1):
    n,m = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(n)]
    dxy = [[0,1],[0,-1],[1,0],[-1,0]]
    max_sum = 0

    for i in range(n):
        for j in range(m):
            total_sum = arr[i][j]

            for dx,dy in dxy:
                for step in range(1, arr[i][j]+1):
                    ni = i + dx*step
                    nj = j + dy*step
                    if 0 <= ni < n and 0 <= nj < m:
                        total_sum += arr[ni][nj]
                    max_sum = max(max_sum,total_sum)
    print(f'#{test_case} {max_sum}')