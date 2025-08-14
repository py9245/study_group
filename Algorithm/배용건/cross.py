import sys
sys.stdin = open("input (1).txt", "r")


T = int(input())
N = 100
for tc in range(1,T+1):
    matrix = [list(map(int, input().split())) for _ in range(N)]
    max_num = 0
    i_max = []
    j_max = []
    
    for i in range(N):
        i_sum = 0
        for ii in range(N):
            i_sum += matrix[i][ii]
            i_max.append(i_sum)
    # print(max(i_max))
    
    for j in range(N):
        j_sum = 0
        for jj in range(N):
            j_sum += matrix[jj][j]
            j_max.append(j_sum)
    print(max(j_max))
    
    for k in range(N):
        k_sum = 0
        for kk in range(N):
            if k == kk 