
from collections import deque
import sys
sys.stdin = open('input.txt', 'r')


# 방향 정해주기
dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]

# 빙산 녹을때

def nok(A, B):
    global ice, melt


    if years > 0:


        result = [[x - y for x, y in zip(row1, row2)] for row1, row2 in zip(ice, melt)]
        return result
# 군집이 형성될때의 cnt

def bfs(i, j, visited):
    global N, M, years, melt, minus, years

    q = deque([(i, j)])
    visited[i][j] = True

    while q:
        x, y = q.popleft()

        for dx, dy in dxy:
            nx, ny = x + dx, y + dy

            if 0 <= nx < N and 0 <= ny < M:
                if ice[x][y] == 0:
                    continue
                if ice[nx][ny] == 0 and visited[nx][ny] == False:
                    visited[nx][ny] = True
                    melt[x][y] += 1
                    q.append((nx, ny))
    return 1


# 입력 받기

N, M = map(int, input().split())
ice = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
melt = [[0] * M for _ in range(N)]
minus = 0
years = 0

for i in range(N):
    for j in range(M):
        if ice[i][j] != 0 and visited[i][j] == False:

            bfs(i, j, visited)
            years += 1
result_1 = nok(ice, melt)

print(result_1)
