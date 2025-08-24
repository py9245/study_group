for test in range(10):
    Test = int(input())

    num_list = []
    for ran in range(100): # 100으로 바꿔야됨
        num_list.append(list(map(int, input().split()))) 
    # print(num_list)
   
    
    yeok = 0 # 역대각선
    jung = 0 # 정대각선
    max_num = 0 # 최댓값
    for i in range(100): # 100으로 바꿔야됨
        hang = 0 # 행
        yeol = 0 # 열
        yeok += num_list[i][len(num_list)-1-i]
        for j in range(100): # 100으로 바꿔야됨
            hang += num_list[i][j]
            yeol += num_list[j][i]
            if (i == j):
                jung += num_list[i][j]
                
            # print(f"i = {i}, j = {j}")
        max_num = max(hang, jung, yeol, yeok, max_num)
    # print(f"행 : {hang} 정 : {jung} 열 : {yeol} 역 : {yeok} 맥넘 : {max_num}")

    print(f"#{Test} {max_num}")