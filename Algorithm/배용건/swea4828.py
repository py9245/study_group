T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    list_A = list(map(int, input().split()))
    max_num = list_A[0]
    min_num = list_A[0]
    for list_B in list_A:
        if list_B > max_num :
            max_num = list_B
        if list_B < min_num :
            min_num = list_B
    print(f'#{test_case} {max_num - min_num}')

