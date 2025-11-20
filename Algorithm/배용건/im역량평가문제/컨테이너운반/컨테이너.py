# 빈 배열을 만들어 방문처리 하는 방식도 써보기

import sys
sys.stdin = open('input.txt','r')

T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    n_list = list(map(int, input().split()))  # 컨테이너 들
    m_list = list(map(int, input().split()))  # 트럭 들

    n_list.sort(reverse=True)
    m_list.sort(reverse=True)

    visited = [False] * n  # 컨테이너 사용 여부 체크
    cnt = 0

    for i in range(m):
        for j in range(n):
            if not visited[j] and m_list[i] >= n_list[j]:
                visited[j] = True
                cnt += n_list[j]
                break
    print(f"#{tc} {cnt}")