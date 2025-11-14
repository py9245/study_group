import sys
import heapq
sys.stdin = open('input1.txt','r')






def dijkstra(graph, start, goal):
    N = len(graph)
    dist = [float('inf')] * N
    dist[start] = 0
    heap = [(0, start)]

    while heap:
        cur_dist, n = heapq.heappop(heap)

        if cur_dist > dist[n]:
            continue
        
        for e, w in graph[n]:
            new_dist = cur_dist + w

            if new_dist < dist[e]:
                dist[e] = new_dist
                heapq.heappush(heap, (new_dist, e))

    if dist[goal] == float('inf'):
        return 'impossible'
    else:
        return dist[goal]



T = int(input())
for tc in range(1, T + 1):
    N, E = map(int, input().split()) 
    graph = [[] for _ in range(N)]
    for _ in range(E):
        a, b, e = map(int, input().split())

        graph[a].append((b, e))
        
    ans = dijkstra(graph, 0, N-1)

    print(f"#{tc} {ans}")
    

