T = int(input())
for test_case in range(1,T+1):
    n,m = map(int,input().split())
    pari = [list(map(int,input().split())) for _ in range(n)]
    dxy = [[0,1],[0,-1],[1,0],[-1,0],[1,1],[1,-1],[-1,1],[-1,-1]]
    max_sum = 0
    
    for i in range(n):
        for j in range(n):
            plus_sum = pari[i][j]
            for dx,dy in dxy[:4]:
                for step in range(1,m):
                    ni = i + dx*step
                    nj = j + dy*step
                    if 0 <= ni < n and 0 <= nj < n:
                        plus_sum += pari[ni][nj]
            
            x_sum = pari[i][j]
            for dx,dy in dxy[4:]:
                for step in range(1,m):
                    ni = i + dx*step
                    nj = j + dy*step
                    if 0 <= ni < n and 0 <= nj < n:
                        x_sum += pari[ni][nj]
            max_sum = max(max_sum,plus_sum,x_sum)
    print(f'#{test_case} {max_sum}')