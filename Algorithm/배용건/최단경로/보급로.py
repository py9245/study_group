import heapq
import sys
sys.stdin = open('input2.txt','r')

dxy = [(1,0),(0,1),(-1,0),(0,-1)]

def dijkstra(N, arr):
    dist = [[float('inf')] * N for _ in range(N)]
    dist[0][0] = arr[0][0]  # 초기값이 중요함
    heap = [(arr[0][0],0,0)] # 누적비용, 좌표 x, y

    while heap:
        cur_cost, x, y = heapq.heappop(heap)

        if cur_cost > dist[x][y]:
            continue  # cur_cost는 누적값보다 작아야한다

        for dx, dy in dxy:
            nx, ny = x + dx, y + dy

            if 0 <= nx < N and 0 <= ny < N :
                new_cost = cur_cost + arr[nx][ny]
                # 새로운 비용 = 최소비용 + 다음 이동할 곳의 비용
                if new_cost < dist[nx][ny]: # 새로운 비용 < 현재까지 누적비용
                    dist[nx][ny] = new_cost  # 현재까지 누적비용 = 새로운 비용 
                    heapq.heappush(heap,(new_cost,nx,ny))
    return dist[N-1][N-1] # 도착지점의 값 리턴







T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().strip())) for _ in range(N)]
    
    result = dijkstra(N, arr)
    print(f"#{tc} {result}")