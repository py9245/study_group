import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

dxy = [[1, 0], [0, 1], [-1, 0], [0, -1]]

def root(road):  # 입력받은 변수활용해서 초기값 함수 만들기

    queue = deque()  # 데쿵으로 감싼 큐를
    queue.append((1, 1))  # 첫 시작값 큐에 넣기

    visited = [[-1] * N for _ in range(N)]  # 방문처리 초기값 변수
    visited[1][1] = 0  # 시작지점을 방문처리한다

    while queue:  # 큐에 값이 있는 동안
        x, y = queue.popleft()    # 앞에 값을 x, y 에 할당해주고

        for dx, dy in dxy:   # 방향
            nx, ny = x + dx, y + dy  # 현재위치에서 더한 방향으로의 위치좌표

            if 0 <= nx < N and 0 <= ny < N:  # 범위
                if road[nx][ny] == 3:  # 도착했다면 1을 리턴하고
                    return 1

                if visited[nx][ny] == -1 and road[nx][ny] == 0:
                    # visited(방문)이 -1이라는건 방문을 아직 안한거
                    # 길이면 방문가능한거
                    queue.append((nx, ny))  # 조건에 맞으면 좌표를 큐에 넣을게
                    visited[nx][ny] = 1  # 방문 처리한거
    return 0




N = 16
for tc in range(1, 11):
    T = int(input())
    road = [list(map(int, input())) for _ in range(N)]

    result = root(road)
    print(f"#{tc} {result}")