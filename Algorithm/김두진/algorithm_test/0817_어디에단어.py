T = int(input())
for test_case in range(1,T+1):
    n,k = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(n)]
    total_cnt = 0

    for i in range(n):
        count = 0
        for j in range(n):
            if arr[i][j] == 1 : # 1일 경우 카운트 1증가
                count += 1
            if arr[i][j] == 0 or j == n-1: # 범위지정. 위치가 0 이거나, 범위 끝에 도달했을경우
                if count == k:  # 현재 카운트가 k와 같은지 확인
                    total_cnt += 1  # 맞으면 총합 +1
                count = 0   # 0으로 초기화
    
    for j in range(n):
        count = 0
        for i in range(n):
            if arr[i][j] == 1:
                count += 1
            if arr[i][j] == 0 or i == n -1:
                if count == k :
                    total_cnt += 1
                count = 0

    print(f'#{test_case} {total_cnt}')