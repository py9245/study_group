import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    n, m, k = map(int, input().split())
    pass_list = list(map(int, input().split()))  # 정답지
    student_list = [list(map(int, input().split())) for _ in range(n)]
    max_cnt = 0

    for i in range(n):
        sum_cnt = 0
        cnt = 0
        counting = 0
        for j in range(m):
            if (j + 1) % k  == 0 and student_list[i][j] == pass_list[j] and counting % (k - 1) == 0:
                cnt = 50
                sum_cnt += cnt
                cnt = 0

                continue
            elif student_list[i][j] == pass_list[j]:
                cnt = 10
                sum_cnt += cnt
                counting += 1


            elif student_list[i][j] != pass_list[j]:
                cnt = 0

        max_cnt = max(sum_cnt, max_cnt)
    print(f"#{tc} {max_cnt}")