# 동전처럼 생긴 돌의 양면은 각각 흰색과 검은색으로 되어있고, 게임의 규칙은 다음과 같다.
# i번째 돌을 사이에 두고 마주보는 j개의 돌에 대해, 각각 같은 색이면 뒤집고, 다른 색이면 그대로 둔다.
# 주어진 돌을 벗어나는 경우 뒤집기는 중지된다.
# [입력]
# 첫 줄에 게임의 개수 T, 다음 줄부터 게임별로 첫 줄에 돌의 수 N, 뒤집기 횟수 M, 다음 줄에 N개 돌의 초기상태, 이후 M개의 줄에 걸쳐 i, j가 주어진다.
# (1<=T<=50, 3<=N<=20,   1<=M<=10, 1<=i, j<=N)
# [출력]
# #과 게임번호, 빈칸에 이어 빈칸으로 구분된 돌의 상태를 출력한다.

# 예제 입력
# 3
# 5 1
# 0 1 0 1 0
# 2 2
# 5 1
# 0 1 0 0 0
# 2 3
# 10 4
# 0 1 1 0 0 1 0 1 0 1
# 3 2
# 5 3
# 4 4
# 8 4

# 예제 출력
# # 1 1 1 1 1 0
# # 2 1 1 1 0 0
# # 3 1 0 0 0 0 0 1 0 1 0

# 범위체크하고 돌 뒤집기.
# stones[left] = 1 - stones[left]
# stones[right] = 1 - stones[right]

T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    stones = list(map(int,input().split()))

    # 1차원 델타배열(왼쪽, 오른쪽)
    dx = [-1.1]
    
    for _ in range(M): # M 은 뒤집기 횟수
        center , j = map(int,input().split())
        center -= 1 # 인덱스 조정 우리가 아는 인덱스는 0부터이니까.

        for k in range(1, j + 1): # k는 퍼져 나가는 파워
            left = center + dx[0] * k
            right = center + dx[1] * k

            # 범위 체크 (벗어나면 안됨), 왼쪽 돌과 오른쪽돌이 같은 돌이면 뒤집기
            if 0 <= left and right < N and stones[left] == stones[right]:
                stones[left] = 1 - stones[left]
                stones[right] = 1 - stones[right]
    
    print(f'#{tc}', *stones) # *은 언패킹 연산자