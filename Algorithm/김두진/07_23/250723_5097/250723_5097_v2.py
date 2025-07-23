from collections import deque
T = int(input())

for test_case in range(1, T+1):
    N,M = map(int, input().split())
    dq = deque(map(int, input().split()))

# deque에 대해서 복습하면서 추가로 얻은 정보로 rotate함수를 이용하면 처음에 푼 코드보다 훨씬 빠를거라 생각하여 복습 겸 실행해봤습니다.
# rotate를 사용하여 코드를 작성해보니 더 간략하게 작성이 가능하며 쉬웠습니다.

    dq.rotate(-M) # rotate함수는 () 안에 음수냐,양수냐에 따라 방향이 달라짐. 음수일 경우 맨 앞에 있는 원소가 뒤로 가는 방향
                    #, 양수일 경우 맨 뒤에 있는 원소가 앞으로 가는 방향
    
    print(f'#{test_case} {dq[0]}') # dq에 담겨있는 리스트 중 제일 맨 앞에 원소를 프린트하는 코드.
