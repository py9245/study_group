n, m, v = map(int, input().split())

board = [[False] * (n+1) for _ in range (n+1)]

for _ in range(m):
    x, y = map(int, input(). split())
    board[x][y] = True
    board[y][x] = True


def sol_dfs(s):
    visited[s] = True
    print (s, end=" ")
    for i in range (1, n+1):
        if board[s][i] and not visited[i]:
            sol_dfs(i)


def sol_bfs(s):
    ans = 0
    q = []
    q.append(s)
    visited[s] = True
    while q:
        ans = q.pop(0)
        print (ans, end=" ")

        for i in range (n+1):
            if not visited[i] and board[ans][i]:
                q.append(i)
                visited[i] = True


visited = [False] * (n+1)
visited[0] = True
sol_dfs(v)
print ()

visited = [False] * (n+1)
visited[0] = True
sol_bfs(v)