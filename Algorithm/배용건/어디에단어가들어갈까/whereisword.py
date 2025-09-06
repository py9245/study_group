T = int(input())
 
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(N)]
    result  = 0
 
    for i in range(N):
        empty_cnt = 0
        for j in range(N):
            if puzzle[i][j] == 1:
                empty_cnt += 1
            elif puzzle[i][j] == 0:
                if empty_cnt == K:
                    result += 1
                empty_cnt = 0
        if empty_cnt == K:
            result += 1
     
    for j in range(N):
        empty_cnt = 0
        for i in range(N):
            if puzzle[i][j] == 1:
                empty_cnt += 1
            elif puzzle[i][j] == 0:
                if empty_cnt == K:
                    result += 1
                empty_cnt = 0
        if empty_cnt == K:
            result += 1
    print(f'#{tc} {result}')