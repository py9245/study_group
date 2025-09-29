"""
2차원 격자 A는 바이러스 0은 청정
A끼리 모여있는 군집 중에 가장 큰 군집 찾고 총 개수 계산
A가 없으면 0 출력
bfs 랑 델타하고 할 때마다 +1
종료 마지막 칸
visited 랑 0이면 continue
"""
from collections import deque
T = int(input())
dxy = [(-1, 0), (1, 0), (0, -1), (0, 1), (1, 1), (1, -1), (-1, -1), (-1, 1)]


def cnt_virus(x, y, cell_map):
    global max_virus, sum_virus
    queue = deque()
    queue.append((x, y))

    while queue:
        queue.pop()
        sum_virus += 1  # 함수가 실행될 때마다 sum 에 1 추가
        Nij[x][y] = '0'  # 한버 확인했으니 0으로 바꾸기 = visited
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N:  # 범위가 격자 안일 때
                if cell_map[nx][ny] == '0':  # 0이라면 pass
                    continue
                if cell_map[nx][ny] == 'A':  # A 이면 그 부분에서 다시 함수 실행
                    cnt_virus(nx, ny, Nij)
        max_virus = max(max_virus, sum_virus)  # max_virus 와 sum_virus 를 비교해서 최대값 갱신


for tc in range(1, T + 1):
    N = int(input())
    Nij = [list(map(str, input().split())) for _ in range(N)]
    max_virus = 0  # 군집의 최대 수를 저장할 변수
    sum_virus = 0  # 각 군집의 수를 더하는 변수

    for i in range(N):
        for j in range(N):
            if Nij[i][j] == '0':  # 델타탐색을 하면서 0이면 pass
                continue
            cnt_virus(i, j, Nij)  # 아닌 경우엔 함수 실행
            sum_virus = 0  # 함수가 끝난 후 sum 초기화
    print(f'#{tc} {max_virus}')
