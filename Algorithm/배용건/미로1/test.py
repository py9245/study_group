from collections import deque
import sys
sys.stdin = open('.txt','r')

dxy = [[1,0],[0,1],[-1,0],[0,-1]]


def root(road):
    queue = deque()
    queue.append((1,1)) # 출발 시작 점 좌표값을 큐에 넣기
    visited = [[-1] * N for _ in range(N)]  # 일종의 복사 방문체크용 리스트 만들기
    visited[1][1] = 0  # -1로 방문체크 리스트를 만들었으니 -1만 아니면 된다.

    while queue: # 큐에 더 움직일 좌표가 있을때 까지
        x, y = queue.popleft() # 큐에 들어온 값들을 앞에 값부터 x, y에 할당해준다

        for dx, dy in dxy:
            nx, ny = dx + x, dy + y

            if 0 <= nx < N and 0 <= ny < N:
                if road[nx][ny] == 3:
                    return 1
                
                if visited[nx][ny] == -1 and road[nx][ny] == 0:
                    queue.append((nx,ny))
                    visited[nx][ny] = 0




N = 16
for tc in range(1, 11):
    T = int(input())
    road = [list(map(int, input().split()) for _ in range(N))]
