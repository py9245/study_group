import heapq, math

def dijkstra(graph, start):
    distances = {v: math.inf for v in graph} # 정점들의 이동 가중치값의 초기값을 무한대로 만들어주기
    distances[start] = 0
    min_heap = []
    heapq.heappush(min_heap, [0, start])

    while min_heap:
        current_distance, current_vertex = heapq.heappop(min_heap)

        if distances[current_vertex] < current_distance: continue

        for adjacent, weight in graph[current_vertex]:
            nd = current_distance + weight

            if nd < distances[adjacent]:
                distances[adjacent] = nd
                heapq.heappush(min_heap, [nd, adjacent])



def dijkstra(start, graph, n):
    INF = int(1e9)
    dist = [inf] * (n+1)
    dist[start] = 0
    q = [(0, start)]

    while q:
        d, now = heapq.heappop(q)
        if dist[now] < d:
            continue
        for nxt, w in graph[now]:
            nd = d + w
            if nd < dist[nxt]:
                dist[nxt] = nd
                heapq.heappush(q, (nd, nxt))
    return dist
