Test = int(input())

for test in range(1, Test+1):
    num_list = []
    for ran in range(5):
        num_list.append(list(map(int, input().split())))
    # print(num_list)
   
    
    yeok = 0
    jung = 0
    max_num = 0
    max_num2 = 0
    cnt = 1
    for i in range(5):
        hang = 0
        yeol = 0
        yeok += num_list[i][len(num_list)-1-i]
        for j in range(5):
            hang += num_list[i][j]
            yeol += num_list[j][i]
            if (i == j):
                jung += num_list[i][j]
                
            print(f"i = {i}, j = {j}")
        max_num = max(hang, jung, yeol, yeok, max_num)
    print(f"행 : {hang} 정 : {jung} 열 : {yeol} 역 : {yeok} 맥넘 : {max_num}")

    print(max_num)
    # for j in range(3):
    #     for i in range(3):
    #         yeol = num_list[i][j]