Test = int(input())
for test in range(1, Test+1):
    N, M = map(int, input().split())  # N = 글자 길이, M = 교체 수
    num_list = list(map(int, input().split()))
    for m in range(1, M+1):
        idx, cont = map(int, input().split()) # idx = 교체 기준 위치, # cont = 기준 위치로부터 길이
        idx_m = idx-1
        for cnt in range(1, cont+1):  # cont 가 2면
            if 0 <= idx_m + cnt < N and 0 <= idx_m - cnt < N:
                # print(idx_m, num_list[idx_m-cnt], num_list[idx_m+cnt], "위치~~~~")
                if num_list[idx_m+cnt] == num_list[idx_m-cnt]:     # 마주보는 수가 같으면
                    if num_list[idx_m+cnt] == 0:                         # 0이면
                        num_list[idx_m+cnt], num_list[idx_m-cnt] = 1, 1
                        # print(num_list, "0일때")
                    elif num_list[idx_m+cnt] == 1:                       # 1이면
                        num_list[idx_m+cnt], num_list[idx_m-cnt] = 0, 0
                        # print(num_list, "1일때")

                elif num_list[idx_m + cnt] != num_list[idx_m - cnt]:   # 다르면 패스
                    pass
    A = ' '.join(map(str, num_list))
    print(f"#{test} {A}")
