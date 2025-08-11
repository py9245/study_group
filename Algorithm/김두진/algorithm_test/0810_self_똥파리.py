# 본 문제 풀이는 양심에 손을 얹고 혼자 푸는 과정입니다.
T = int(input())
for test_case in range(1,T+1):
    N,M = map(int,input().split())
    nums = [list(map(int,input().split())) for _ in range(N)]
    total_kill = 0 # 총합적으로 파리잡은 큰 수를 저장할 곳 처음으로 0 초기화

    for i in range(N - M + 1): #파리채의 크기가 m이므로, N으로 하면, 인덱스초과 에러 발생
        for j in range(N - M + 1):
            total = 0   # 각 행과 열을 하나씩 순회하면서, 파리채크기만큼 합산한 결과를 담을 변수 초기화선언
            for m in range(M): # 파리채크기만큼 행 순회
                for n in range(M): # 파리채크기만큼 열 순회
                    total += nums[i + m][j+n] # 순회하면서, m*m 크기의 파리를 잡고 더하여 total에 저장.
            total_kill = max(total_kill,total) # 각 칸을 순회하면서 다 더해줘야하니, total_kill에 max함수를 이용해, total_kill과 total 중에 큰 수를 total_kill에 저장.
    print(f"#{test_case} {total_kill}") # 테스트케이스별로 출력