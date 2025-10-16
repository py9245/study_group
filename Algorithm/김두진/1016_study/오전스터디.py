from collections import deque
dxy = [[0,1],[0,-1],[1,0],[-1,0]]

def bfs():
    cnt = 0
    for i in range(N):
        for j in range(N):
            if temp_visited[i][j]:
                continue
            
            cnt += 1
            queue = deque()
            queue.append((i,j))

            while queue:
                x,y = queue.popleft()
                for dx, dy in dxy:
                    nx, ny = x+dx, y+dy
                    if not(0 <= nx < N and 0 <= ny < N) or temp_visited[nx][ny]:
                        continue
                    queue.append((nx,ny))
                    temp_visited[nx][ny] = True
    return cnt



def rain():
    for i in range(N):
        for j in range(N):
            if arr[i][j] <= t:
                visited[i][j] = True

N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]
result = 0
t = 0

while t <= 100:
    rain()
    temp_visited = [ar[:] for ar in visited]
    result = max(result, bfs())
    t += 1

print(result)