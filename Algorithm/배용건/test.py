#구간합 구하기

T = int(input())
for tc in range(1,T+1):
    N , M = map(int, input().split())
    num = list(map(int, input().split()))
    first_sum = sum(num[0:M])
    max_num = first_sum
    min_num = first_sum
    for i in range(1,N - M + 1):
        sum_num = 0
        for j in range(M):
            sum_num += num[i+j]
        if sum_num > max_num:
            max_num = sum_num
        if sum_num < min_num:
            min_num = sum_num
    print(f"#{tc} {max_num - min_num}")

    # 2번째 연습

T = int(input())
for tc in range(1,T+1):
    N , M = map(int, input().split())
    num = list(map(int, input().split()))
    first_sum = sum(num[0:M])
    max_num = first_sum
    min_num = first_sum
    for i in range(1,N - M +1):
        sum_num = 0
        for j in range(M):
            sum_num += num[i+j]
        if sum_num > max_num:
            max_num = sum_num
        if sum_num < min_num:
            min_num = sum_num
    print(f"#{tc} {max_num - min_num}")



# 파리 퇴치
T = int(input())
for tc in range(1,T+1):
    N , M = map(int, input().split())
    fly_list = [list(map(int, input().split())) for _ in range(N)]
    kill_num = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            num = 0
            for m in range(M):
                for n in range(M):
                    num += fly_list[i+m][j+n]
            if num > kill_num:
                kill_num = num
    print(f"#{tc} {kill_num}")
        