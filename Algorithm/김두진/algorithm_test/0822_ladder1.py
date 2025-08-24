import sys
sys.stdin = open("C:\\Users\\Administrator\\Desktop\\dujin\study_group\\Algorithm\\김두진\\algorithm_test\\input (4).txt","r")
for test_case in range(1,11):
    T = int(input())
    arr = [list(map(int,input().split())) for _ in range(100)]
    visited = [[False] * 100 for _ in range(100)]
    dxy = [[0,1],[0,-1],[-1,0]]
    for i in range(100):
        if arr[99][i] == 2:
            x,y = (99,i)
            break
        
    visited[x][y] = True
    while x:
        for dx,dy in dxy:
            nx = x+dx
            ny = y+dy
            if 0 <= nx < 100 and 0 <= ny < 100 and not visited[nx][ny] and arr[nx][ny] == 1:
                visited[nx][ny] = True
                x,y = nx,ny
                break
    print(f'#{test_case} {y}')