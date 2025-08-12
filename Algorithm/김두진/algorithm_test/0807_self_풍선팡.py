T = int(input())
for test_case in range(1,T+1):
    n,m = list(map(int,input().split()))
    arr = [list(map(int,input().split())) for _ in range(n)]
    dxy = [[0,1],[0,-1],[1,0],[-1,0]]
    total_sum = 0

    for i in range(n):
        for j in range(m):
            this = arr[i][j]

            for dx,dy in dxy:
                ni = i+dx
                nj = j+dy

                if 0 <= ni < n and 0 <= nj < m:
                    this += arr[ni][nj]
            total_sum = max(total_sum,this)
    print(f'#{test_case} {total_sum}')
    