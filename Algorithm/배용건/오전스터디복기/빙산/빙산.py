import sys
sys.stdin = open('.txt','r')


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
melting = [[] * M for _ in range(N)]