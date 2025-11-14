N = 100
for tc in range(10):
    t = int(input())
    matrix = [list(map(int,input().split())) for _ in range(N)]
    max_num = 0
    
    for i in range(N): #행 순회
        i_sum = sum(matrix[i]) # 행의 합을 구하고 할당한다
    if i_sum > max_num:
        max_num = i_sum
    
    for j in range(N): #열 순회
        j_sum = 0
        for i in range(N):
            j_sum += matrix[i][j]
    if j_sum > max_num:
        max_num = j_sum
    
    left_line = 0
    right_line = 0
    for i in range(N):
        left_line += matrix[i][i]
        right_line += matrix[i,N-1-i]
    if left_line > max_num:
        max_num = left_line
    if right_line > max_num:
        max_num = right_line
    
    print(f"#{t} {max_num}")



    N = 100
    for tc in range(10):
        t = int(input())
        matrix = [list(map(int, input().split())) for _ in range(N)]
        max_num = 0
        for i in range(N): # 행 순회
            i_sum = sum(matrix[i])
        if i_sum > max_num :
            max_num = i_sum
        
        for j in range(N): # 열 고정 순회
            j_sum = 0
            for i in range(N):
                j_sum += matrix[i][j]
        if j_sum > max_num:
            max_num = j_sum
        
        left_line = 0 # 주대각선
        right_line = 0 # 부대각선
        for i in range(N):
            left_line += matrix[i][i]
            right_line += matrix[i,N-1-i]

        if left_line > max_num:
            max_num = left_line
        if right_line > max_num:
            max_num = right_line
    print(f"#{t} {max_num}")
