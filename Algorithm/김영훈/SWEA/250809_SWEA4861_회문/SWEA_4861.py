Test = int(input())
for test in range(1 , Test+1):
    N, M = map(int, input().split())
    str_List = [list(map(str, input().split())) for _ in range(N)]
    for i in range(N-M+1):
        for j in range(N-M+1):
            LR_str = ''
            L_str = ''
            R_str = ''
            for k in range(M//2): # m//2 만큼 양쪽에서 가운데까지 이동
                if((j+k) < (M+j-1-k) and str_List[i][j+k] == str_List[i][M+j-1-k]): 
                    #  왼쪽 < 오른쪽 이고 각 인덱스의 문자가 같으면
                    # if(str_List[i][j+k] == str_List[i][M+j-1-k]): 
                    L_str += str_List[i][j+k]
                    R_str += str_List[i][M+j-1-k]
                    print(L_str, R_str, "L, R str 임")
                
                elif(str_List[i][j+k] != str_List[i][M+j-1-k]): # 다르면
                    break
            # if(L_str == R_str): # 왼쪽 오른쪽 같으면
            LR_str = L_str+R_str
            print(LR_str)
