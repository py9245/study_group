import heapq
import sys
sys.stdin = open('.txt','r')



def prim(start, N, graph):
    visited = [False] * (N + 1)
    heap = [(0, start)]
    # visited, heap 세팅은 기본 세팅 
    # 그다음은 필요한 변수를 세팅해줘야한다

    total = 0  # 비용 전체를 합쳐줄 변수
    cnt = 0  # 정점들을 연결할때마다 세기

    while heap:
        cost, u = heapq.heappop(heap)

        if visited[u]: # 이미 포함된 정점이면 스킵
            continue

        visited[u] = True
        total += cost
        cnt += 1

        for v, w in graph[u]:
            if not visited[v]:
                heapq.heappush(heap, (w, v))

        if cnt == N:
            return total  # 전체 비용을
    return -1  # -1을 






T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    for _ in range(M):
        x, y, cost = map(int, input().split())
        graph[x].append((y, cost))
        graph[y].append((x, cost))
    result = prim(1, N, graph)
    print(f"#{tc} {result}")