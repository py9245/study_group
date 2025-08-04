T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    list_A = map(int,input().split('0'))
    data = list_A
    for index in data :
        if index(1 in data):
            index = max(index[0,1])
print(f'#{index}')
    # max_num = list_A[0]
    # for list_B in list_A:
    #     if list_B > max_num:
    #         max_num = sum(list_B)
    # print(f'#{test_case} {max_num}')