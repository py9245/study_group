import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    n_list = list(map(int, input().split()))
    m_list = list(map(int, input().split()))
    
    max_num = 0
    if n > m:
        n, m = m, n
        n_list, m_list = m_list, n_list

    
    for i in range(m - n + 1):
        sum_num = 0
        for j in range(i, i + n):
            sum_num += m_list[j] * n_list[j - i]
        max_num = max(sum_num, max_num)
    print(f"#{tc} {max_num}")