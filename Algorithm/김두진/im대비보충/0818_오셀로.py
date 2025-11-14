# 영훈햄과 오셀로 풀기 시작.
# 08/18(월) 시작 시각 : 20:30 
# swea-> IM대비 문제 오셀로
t = int(input())
for test_case in range(1,t+1):
    # 델타 탐색 위치 지정
    dxy = [[0,1],[0,-1],[1,0],[-1,0],[-1,-1],[-1,1],[1,-1],[1,1]]
    # 보드의 한변 길이 N , 돌을 놓는 쵯수 M
    N , M = map(int,input().split()) 
    # 0으로 채워진 배열을 N만큼 오셀로판을 만듬
    arr = [list([0] * N) for _ in range(N)]
    mid = N // 2
    arr[mid][mid] = 2
    arr[mid-1][mid-1] = 2
    arr[mid-1][mid] = 1
    arr[mid][mid-1] = 1
    for a in range(M):
        # 입력 받아오기 이 때, c에 들어오는 1, 2 는 흑돌과 백돌을 의미함
        x = x - 1
        y = y - 1
        x, y, c = map(int,input().split())
        arr[x][y] = c
        
        
    print(arr)
