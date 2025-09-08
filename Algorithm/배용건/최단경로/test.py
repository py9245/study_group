# swea 최소이동거리 연습

import sys
import heapq
sys.stdin = open('.txt','r')



def dijkstra(graph, start, goal):
    N = len(graph) - 1  # graph 마지막 정점 번호
    dist = [float('inf')] * N + 1
    dist[start] = 0
    heap = [(0, start)]  # 현재까지의 거리, 정점

    while heap:
        cur_dist, n = heapq.heappop(heap)
        # heap의 최소 가중치와 그 정점을 각 변수에 할당한다

        if cur_dist > dist[n]: 
        # 최소 가중치가 최단거리 기록보다 크다면 continue
            continue

        if n == goal:
            # 정점이 끝까지 갔다면 최소 가중치를 return
            return cur_dist
        
        for e, w in graph[n]:
            # graph의 정점인덱스 값을 e, w 로 순회 시킨다
            new_dist = cur_dist + w
            # new_dist 에 최소 가중치 와 그래프 정점의 가중치를 더한다

            if new_dist < dist[e]: 
                # 이전에 기록된 e 까지의 거리보다 지금 새로찾은 거리가 짧다면
                
                dist[e] = new_dist  # 더 짧기때문에 갱신
                heapq.heappush(heap, (new_dist, e)) 
                # 짧은길이 새로 발견됐으니 다음 탐색후보로 예약
                # 왜? 짧으니까 
    return dist[goal]

T = int(input())
for tc in range(1, T + 1):
    N, E = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    for _ in range(E):
        s, e, w = map(int, input().split())

        graph[s].append((e, w))
    ans = dijkstra(graph, 0, N)
    print(f"#{tc} {ans}")

