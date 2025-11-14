import sys
from collections import deque
sys.stdin = open('input.txt','r')

dxy = [(1,0),(0,1),(-1,0),(0,-1),(1,1),(-1,-1),(-1,1),(1,-1)]

def bfs(i, j):
    q = deque([(i, j)])

    visited[i][j] = True

    while q:
        x, y = q.popleft()
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy

            if 0 <= nx < N and 0 <= ny < M :
                if visited[nx][ny] == False and island[nx][ny] != '0':
                    visited[nx][ny] = True
                    virus.append(island[nx][ny])
                    q.append((nx,ny))

N, M = 8, 8
island = [list(input().split()) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

max_virus = 0
min_virus = float('inf')
virus = []
for i in range(N):
    for j in range(M):
        if visited[i][j] == False and island[i][j] != '0':
            virus = []
            bfs(i, j)
            max_virus = max(max_virus, len(virus))
            min_virus = min(min_virus, len(virus))
            
print(f"1. {max_virus - min_virus} 2. {set(virus)} {len(virus)}")