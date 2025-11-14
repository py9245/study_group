dx = [1, 0, 0]
dy = [0, -1, 1]

def ladder(x, y):

    visited = [[0] * N for _ in range(N)]  # 방문여부를 확인할 수 있도록 한다.
    visited[x][y] = 1

    while x != 99:
        for k in range(3):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < N and 0 <= ny < N and matrix[nx][ny] and not visited[nx][ny]:
                # 범위 안에 들어와야 다음 좌표로 이동

                x, y = nx, ny
                visited[nx][ny] = 1
    return matrix[x][y] == 2



T = 10
for tc in range(1, T + 1):
    N = 100
    a = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    result = -1

    # 출발점이 1인 지점에서 ladder() 함수를 실행한다
    for j in range(N):
        if matrix[0][j] == 1:  # i 고정이고 j 열 기준 1인 곳은 사다리가 놓여 있으므로 , 사다리타기 시작!
            if ladder(0, j):  # 마지막에 도달한 장소가 2인 경우에는 True, 2가 아니면 False
                #  여기에 들어왔다는건 올바른 시작점을 찾았다는 것 => 시작점은 j
                result = j
                break


    print(f"#{tc} {result}")