test = int(input())

for t in range(1, test+1):
    n, m = map(int, input().split())
    num = list(map(int, input().split()))
    max_num = 0
    min_num = float('inf')
    for nu in range(n-m+1):
        m_num = 0

        for mu in range(nu, nu+m):
            m_num += num[mu]

        max_num = max(max_num, m_num)
        min_num = min(min_num, m_num)
        # print(min_num, max_num)

    print(f"#{t} {max_num-min_num}")

# 3
# 10 3
# 1 2 3 4 5 6 7 8 9 10