from collections import deque
T = int(input())

for test_case in range(1, T+1):
    N,M = map(int, input().split())
    dq = deque(map(int, input().split()))
    
    for num in range(M):
        front = dq.popleft()
        dq.append(front)
    print(f'#{test_case} {dq[0]}')
    