import heapq
import sys
sys.stdin = open('input (2).txt','r')

def dijkstra(graph, start, N):
    dist = [float('inf')] * (N + 1)
    dist[start] = 0
    heap = [(0,start)]

    while heap:
        cur_dist, n = heapq.heappop(heap)

        if cur_dist > dist[n]:
            continue

        for e, w in graph[n]:
            new_dist = cur_dist + w

            if new_dist < dist[e]:
                dist[e] = new_dist
                heapq.heappush(heap, (new_dist, e))

    return dist



    



T = int(input())
for tc in range(1, T + 1):
    N, M, X = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    reverse_graph = [[] for _ in range(N + 1)]

    for _ in range(M):
        x, y, c = map(int, input().split())
        graph[x].append((y,c))
        reverse_graph[y].append((x,c))

    from_x = dijkstra(graph, X, N)
    to_x = dijkstra(reverse_graph, X ,N)

    max_time = 0

    for i in range(1, N + 1):
        total = from_x[i] + to_x[i]
        if total < float('inf'):
            max_time = max(max_time, total)
    
    print(f"#{tc} {max_time}")
