dxy = [[0,1],[0,-1],[1,0],[-1,0]]

def find_set(x):
    if x != p_list[x]:
        p_list[x] = find_set(p_list[x])
    return p_list[x]

def union(x,y):
    px = find_set(x)
    py = find_set(y)
    if px != py:
        p_list[py] = px


N = int(input())
p_list = list(range(N+1))
arr = [list(map(int,input().split())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]
result = []
t = 1

# while t <= 100:
    