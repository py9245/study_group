import sys
from collections import deque
sys.stdin = open('.txt','r')

dxy = [(1,0),(0,1),(-1,0),(0,-1)]

# 그래프의 최대 높이 찾기



def bfs(x, y, rain, visited):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True

    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            # 범위 안에 있고, 방문 안했고, 물에 잠기지 않은 곳만 탐색
            if 0 <= nx < N and 0 <= ny < N:
                if not visited[nx][ny] and graph[nx][ny] > rain:
                    visited[nx][ny] = True
                    queue.append((nx, ny))


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]
rain = 100
max_height = max(map(max, arr))

# 비가 내리지 않을 수도 있으니까 최소값 1 대신 0부터 시작
max_safe = 0
for rain in range(0, max_height + 1):
    visited = [[False] * N for _ in range(N)]
    safe_area = 0

    for i in range(N):
        for j in range(N):
            # 물에 잠기지 않았고, 방문하지 않은 경우
            if not visited[i][j] and arr[i][j] > rain:
                bfs(i, j, rain, visited)
                safe_area += 1  # 한 영역 완성될 때마다 +1

    max_safe = max(max_safe, safe_area)

print(max_safe)