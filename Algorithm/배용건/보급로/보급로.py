from collections import deque
import sys
sys.stdin = open('.txt','r')

dxy = [[1,0],[0,1],[-1,0],[0,-1]]

def root(road):
    queue = deque()
    queue.append((0,0)) # 시작점 넣기

    visited = [[-1] * N for _ in range(N)]
    visited[0][0] = 0

    while queue :
        x, y = queue.popleft()
        for dx, dy in dxy:
            nx, ny = dx + x, dy + y

            if 0 <= nx < N and 0 <= ny < N :
                if road[nx][ny] == road[N-1][N-1]:
                    break

                if visited[nx][ny] == -1 and road[nx][ny] == 0:
                    road_sum += road[nx][ny]
                
                if road[nx][ny] == 1 :


        



T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    road = [list(map(int, input().strip())) for _ in range(N)]
    road_sum = 0
    min_road_sum = 100
    min_road_sum = min(min_road_sum,road_sum)