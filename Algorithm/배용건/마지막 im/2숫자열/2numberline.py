import sys
sys.stdin = open('input.txt','r')

T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    n_list = list(map(int, input().split()))
    m_list = list(map(int, input().split()))

    sum_list = 0

    if n > m :
        n, m = m, n
        n_list, m_list = m_list, n_list

    for i in range(m-n+1):
        sum_value = 0
        for j in range(n):
            sum_value += m_list[i+j] * n_list[j]
        sum_list = max(sum_list,sum_value)
    print(f"#{tc} {sum_list}")