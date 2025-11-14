
N = 100
M = int(input())
paper = [[False] * N for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    for i in range(N):
        for j in range(N):
            if i == a and j == b:
                for k in range(10):
                    for kk in range(10):
                        paper[i+k][j+kk] = True
cnt = 0                   
for i in range(N):
    for j in range(N):
        if paper[i][j] == True:
            cnt += 1

print(cnt)
