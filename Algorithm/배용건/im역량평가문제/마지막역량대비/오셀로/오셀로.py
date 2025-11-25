import sys
sys.stdin = open('input.txt', 'r')

dxy = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (-1, 1), (1, -1)]

# black = 1
# white = 2

T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    visited = [[0] * n for _ in range(n)]

    mid = n // 2
    visited[mid][mid] = 2
    visited[mid][mid - 1] = 1
    visited[mid - 1][mid] = 1
    visited[mid - 1][mid - 1] = 2

    for _ in range(m):
        y, x, stone = map(int, input().split())
        i = x - 1
        j = y - 1
        visited[i][j] = stone

        for dx, dy in dxy:
            stone_list = []
            nx = i + dx
            ny = j + dy
            
                
            while 0 <= nx < n and 0 <= ny < n: # 바둑판 범위 안에 있는 동안
                # 종료 버튼
                
                if visited[nx][ny] == 0 :
                    stone_list = []
                    break
                
                # 내 돌을 만나면 종료
                if visited[nx][ny] == stone:
                    break
                
                
                    

                stone_list.append((nx, ny))
                # 그 방향으로 더해주면 그 방향으로 전진
                nx += dx
                ny += dy

            
            else : # 보드 벗어났을때 
                stone_list = []

            for fx, fy in stone_list:
                visited[fx][fy] = stone
    black = 0
    white = 0
    for ii in range(n):
        for jj in range(n):
            if visited[ii][jj] == 1:
                black += 1
            elif visited[ii][jj] == 2:
                white += 1
    print(f"#{tc} {black} {white}")
         
