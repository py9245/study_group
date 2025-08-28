from collections import deque
T = int(input())
for test_case in range(1,T+1):
    n,m = map(int,input().split())
    dq = deque(map(int,input().split()))

    dq.rotate(-m)
    print(f'#{test_case} {dq[0]}')