import sys

from collections import deque

sys.stdin = open("input.txt", "r")

dxy = [(0, 1), (1, 0), (-1, 0), (0, -1)]
T = 10
N = 100

for _ in range(1, T + 1):
    tc = int(input())
    board = [list(map(int, input())) for _ in range(N)]
    # 출발지점, 목표지점 찾는데 N ** 2 연산
    sx, sy = 0, 0
    ex, ey = 0, 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == 2:
                sx, sy = i, j
            if board[i][j] == 3:
                ex, ey = i, j
            if sx and sy and ex and ey:
                break

    q = deque()
    visited = [[False] * N for _ in range(N)]
    visited[sx][sy] = True
    q.append((sx, sy))

    while q:
        x, y = q.popleft()

        if (x, y) == (ex, ey):
            print(f"#{tc} 1")
            break

        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if not(0 <= nx < N and 0 <= ny < N) or board[nx][ny] == 1 or visited[nx][ny]:
                continue

            visited[nx][ny] = True
            q.append((nx, ny))

    else:
        print(f"#{tc} 0")


