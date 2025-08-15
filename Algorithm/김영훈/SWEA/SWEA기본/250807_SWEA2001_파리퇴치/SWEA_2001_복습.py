Test = int(input())
for test in range(1, Test+1):
    print(Test, test, "TTTTTT")
    N, M = map(int,input().split())
    
    
    flies_list = [list(map(int, input().split())) for _ in range(N)]
    Max_num = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            num = 0

            for k in range(M):
                for l in range(M):
                    num+= flies_list[i+k][j+l]
                
            Max_num = max(Max_num, num)
    print(Max_num)