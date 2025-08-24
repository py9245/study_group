test = int(input())

for t in range(1, test+1):

    n, k = map(int, input().split())
    teams = list(map(int, input().split()))
    max_cnt = 0
    teams.sort()

    for idx in range(len(teams)):
        cnt = 0
        # print(men)

        for k_num in teams[idx:]:
            if abs(teams[idx] - k_num) <= k:
                cnt += 1
            else:
                break

        max_cnt = max(max_cnt, cnt)
    print(f"#{t} {max_cnt}")

