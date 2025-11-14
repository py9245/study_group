T = int(input())

for tc in range (1, T+1):
    n, m = map(int, input().split())
    board = [list(map(int, input().split()))for _ in range(n)]
    ans_list = [[0] * (n+1) for _ in range (n+1)]
    for i in range (1, n+1):
        for j in range (1, n+1):
            x, y = i-1, j-1
            ans_list[i][j] = board[x][y] + ans_list[i-1][j] + ans_list[i][j-1] - ans_list[i-1][j-1]
    
    max_num = 0
    for i in range (m, n+1):
        for j in range (m, n+1):
            ans = ans_list[i][j] -ans_list[i-m][j] - ans_list[i][j-m] + ans_list[i-m][j-m]
            if ans > max_num:
                max_num = ans
                
    print (f"#{tc} {max_num}")
                