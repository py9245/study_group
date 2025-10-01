import sys
sys.stdin = open('input.txt', 'r')

dxy1 = [(1, 0)]
dxy2 = [(0, 1)]
dxy3 = [(-1, 0)]
dxy4 = [(0, -1)]

T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [[False] * n for _ in range(n)]
    


    for i in range(n):
        for j in range(n):
            if arr[i][j] == 2:
                x, y = i, j
                for dx, dy in dxy1:

                    for dist in range(n):
                        nx, ny = x + dx + dist, y + dy



                        if 0 <= nx < n and 0 <= ny < n:
                            if arr[nx][ny] == 1:
                                break
                            if arr[nx][ny] == 0 and visited[nx][ny] == False:
                                visited[nx][ny] = True
                                arr[nx][ny] = 3
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 2:
                x, y = i, j
                for dx, dy in dxy2:

                    for dist in range(n):
                        nx, ny = x + dx, y + dy + dist
                        if 0 <= nx < n and 0 <= ny < n:
                            if arr[nx][ny] == 1:
                                break
                            if arr[nx][ny] == 0 and visited[nx][ny] == False:
                                visited[nx][ny] = True
                                arr[nx][ny] = 3

    for i in range(n):
        for j in range(n):
            if arr[i][j] == 2:
                x, y = i, j
                for dx, dy in dxy3:


                    for dist in range(n):
                        nx, ny = x + dx - dist, y + dy
                        if 0 <= nx < n and 0 <= ny < n:
                            if arr[nx][ny] == 1:
                                break
                            if arr[nx][ny] == 0 and visited[nx][ny] == False:
                                visited[nx][ny] = True
                                arr[nx][ny] = 3
    # 4방향에서 dist를 한코드에 가져갈려면? 

    for i in range(n):
        for j in range(n):
            if arr[i][j] == 2:
                x, y = i, j
                for dx, dy in dxy4:

                    for dist in range(n):
                        nx, ny = x + dx, y + dy - dist
                        if 0 <= nx < n and 0 <= ny < n:
                            if arr[nx][ny] == 1 :
                                break
                            if arr[nx][ny] == 0 and visited[nx][ny] == False:
                                visited[nx][ny] = True
                                arr[nx][ny] = 3
    
    # 합칠려면 어떻게 해야할까 
    cnt = 0
    
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 0:
                cnt += 1

    print(f"#{tc} {cnt}")
