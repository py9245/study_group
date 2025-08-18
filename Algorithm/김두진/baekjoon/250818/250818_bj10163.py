# 백준 색종이 10163번 문제
N = int(input()) # 색종이 장수
arr = [[0] * 1001 for _ in range(1001)] # 색종이가 놓이는 평면은 가로 최대 1001칸,세로 최대 1001칸

for i in range(1,N+1):
    x, y, w, h = map(int,input().split()) # x,y는 가장 왼쪽 아래, w,h는 너비와 높이
    