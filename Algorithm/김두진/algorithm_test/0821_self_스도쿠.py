T = int(input())
for test_case in range(1,T+1):
    # sdok = [list(map(int,input().split())) for _ in range(9)]
    # # 9 * 9 배열의 스도쿠, 겹치는 숫자가 없을 경우 1 아니면, 0 출력
    # # 3*3배열의 중복 검사, 행과열 검사.
    # result = 1
    # for i in range(9):
    #     cnt_r = [0] * 10
    #     cnt_c = [0] * 10
    #     for j in range(9):
    #         cnt_r[sdok[i][j]] += 1
    #         cnt_c[sdok[j][i]] += 1

    #     for k in range(1,10):
    #         if cnt_r[k] != 1:
    #             result = 0
    #             break
    #         if cnt_c[k] != 1:
    #             result = 0
    #             break
        
    # for i in range(3):
    #     for j in range(3):
    #         cnt_x = [0] * 10
    #         for k in range(3):
    #             for l in range(3):
    #                 cnt_x[sdok[3*i+k][3*j+l]] += 1
            
    #         for k in range(1,10):
    #             if cnt_x[k] != 1:
    #                 reuslt = 0 
    #                 break

    # print(f'#{test_case} {result}')

# ------------------------------------------------
# set으로 풀어보기
    sdok = [list(map(int,input().split())) for _ in range(9)]
    result = 1

    for row in sdok:
        if len(set(row)) != 9:
            result = 0

    for c in range(9):
        col = []
        for r in range(9):
            col.append(sdok[r][c])
        if len(set(col)) != 9:
            result = 0
    
    for i in range(0,9,3):
        for j in range(0,9,3):
            box = []
            for x in range(3):
                for y in range(3):
                    box.append(sdok[i+x][j+y])
            if len(set(box)) != 9:
                result = 0
    print(f'#{test_case} {result}')
    