T = int(input())
for test_case in range(1,T+1):
    sdok = [list(map(int,input().split())) for _ in range(9)]
    # cnt = 1
    # for i in range(9):
    #     for j in range(9):
    #         num = 0
    #         if sum(sdok[i][0:9]) != 45 and sum(sdok[0:9][j]) != 45:
    #             cnt = 0
    #             break
    #         if i % 3 == 0 and j % 3 == 0:
    #             for k in range(i, i+3):
    #                 for l in range(j, j+3):
    #                     num += sdok[k][l]

    #             else:
    #                 if num != 45:
    #                     cnt = 0
    #                     break
    
    #     if cnt == 0:
    #         break
    # print(f"#{test_case} {cnt}")

    