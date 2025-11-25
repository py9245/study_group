import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    n_list = list(map(int, input().split())) # 컨테이너 들
    m_list = list(map(int, input().split())) # 트럭 들
    visited = [False] * n
    n_list.sort(reverse=True)
    m_list.sort(reverse=True)

    sum_num = 0

    for i in range(m):
        for j in range(n):
            if not visited[j] and m_list[i] >= n_list[j]:
                visited[j] = True
                sum_num += n_list[j]
                break
    print(f"#{tc} {sum_num}")        
