import sys
sys.stdin = open('input.txt', 'r')

# 1 black
# 2 white

dxy = [(1,0), (0,1), (-1,0), (0, -1), (1, 1), (-1, -1), (-1, 1), (1, -1)]

T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())

    arr = [[0] * n for _ in range(n)]
    mid = n // 2
    arr[mid-1][mid] = 1
    arr[mid][mid-1] = 1
    arr[mid-1][mid-1] = 2
    arr[mid][mid] = 2
    

    for _ in range(m):
        y, x, stone = map(int, input().split())
        
        i = x - 1
        j = y - 1
        arr[i][j] = stone

        

        for dx, dy in dxy:
            stone_list = []
            nx, ny = i + dx, j + dy

            while 0 <= nx < n and 0 <= ny < n:
                if arr[nx][ny] == 0:
                    stone_list = []
                    break

                elif arr[nx][ny] == stone:
                    break

                
                stone_list.append((nx, ny))
                nx += dx
                ny += dy
            else:
                stone_list = []

            for fx, fy in stone_list:
                arr[fx][fy] = stone

    black = 0
    white = 0
    for k in range(n):
        for kk in range(n):
            if arr[k][kk] == 1:
                black += 1
            elif arr[k][kk] == 2:
                white += 1
    print(f"#{tc} {black} {white}")