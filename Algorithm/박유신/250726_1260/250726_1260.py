import sys # sys 라는 s내장 함수를 import
from collections import deque # collections 라는 모듈에서 deque 라는 메서드을 가져옴

input = sys.stdin.readline # 인풋을 받아오는데 정확히 모름

N, M, V = map(int, input().split())
gr = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    gr[a].append(b)
    gr[b].append(a)

for g in gr:
    g.sort()

visited = [False] * (N + 1)
dfs_p = []

def dfs(v):
    visited[v] = True
    dfs_p.append(v)
    for nxt in gr[v]:
        if not visited[nxt]:
            dfs(nxt)

dfs(V)

bfs_p = []
visited = [False] * (N + 1)
q = deque([V])
visited[V] = True

while q:
    v = q.popleft()
    bfs_p.append(v)
    for nxt in gr[v]:
        if not visited[nxt]:
            visited[nxt] = True
            q.append(nxt)

print(*dfs_p)
print(*bfs_p)