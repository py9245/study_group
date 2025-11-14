import sys
import heapq
sys.stdin = open('.txt','r')


def dijkstra(graph, start, goal):
    # graph: 인접 리스트, graph[u] = [(v, w), ...]
    N = len(graph) - 1          # 정점이 0..N 이라면 길이는 N+1
    dist = [float('inf')] * (N + 1)
    dist[start] = 0    # dist = [0, inf, inf, inf, inf, inf]

    # (현재까지의 거리, 노드)
    heap = [(0, start)]

    while heap:
        cur_dist, u = heapq.heappop(heap)
        # 이미 더 좋은 거리로 방문된 이력이 있으면 스킵
        if cur_dist > dist[u]:
            continue

        # 목표 지점에 도달했고, 현재 팝된 거리가 최솟값이면 조기 종료(선택)
        if u == goal:
            return cur_dist

        for v, w in graph[u]:
            nd = cur_dist + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(heap, (nd, v))

    return dist[goal]

T = int(input())
for tc in range(1, T + 1):
    N, E = map(int, input().split())
    
    graph = [[] for _ in range(N + 1)]
    for _ in range(E):
        u, v, w = map(int, input().split())
        # 방향 그래프라 가정
        graph[u].append((v, w)) 
        # 양방향일 경우 u 와 v 의 자리를 바꿔서 하나 더 추가한다

    ans = dijkstra(graph, start=0, goal=N)
    print(f"#{tc} {ans}")