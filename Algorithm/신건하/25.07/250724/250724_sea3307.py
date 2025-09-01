t = int(input())

for tc in range (t):
    n = int(input())
    num = list(map(int, input().split()))
    num.insert(0, 0)
    board = [0] * (n +1)
    
    for i in range (1, n+1):
        a = 0
        for j in range (i):
            if num[i] > num[j]:
                a = max(a, board[j])
        board[i] = a + 1
    
    print (f"#{tc+1} {max(board)}")
    print (board)
            