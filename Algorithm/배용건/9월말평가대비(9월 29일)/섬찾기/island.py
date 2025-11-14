import sys
from collections import deque
sys.stdin = open('input.txt','r')

dxy = [[1,0],[0,1],[-1,0],[0,-1],[1,1],[-1,-1],[1,-1],[-1,1]]


# 땅은 1
# 물은 0
# 델타가 결합됐기 때문에 
# bfs의 매개변수는 좌표값을 활용해야한다
# 그리고 또 방문하지 않게 visited 를 써준다


def bfs(i, j, visited):
    global result
    q = deque()
    q.append((i, j))

    visited[i][j] = 1

    while q:
        x, y = q.popleft()

        for dx, dy in dxy:
            nx, ny = dx + x, dy + y

            if 0 <= nx < N and 0 <= ny < M:
                if island[nx][ny] == 1 and visited[nx][ny] == -1:
                    visited[nx][ny] = 1
                    q.append((nx,ny))
    result += 1



N, M = map(int, input().split())
island = [list(map(int, input().strip())) for _ in range(N)]
visited = [[-1] * M for _ in range(N)]
result = 0


for i in range(N):
    for j in range(M):
        if island[i][j] == 1 and visited[i][j] == -1:
            bfs(i, j, visited)

print(result) 
