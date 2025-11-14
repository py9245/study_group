T = int(input().strip())
for tc in range(1, T + 1):
    N = int(input().strip())
    jobs = [tuple(map(int, input().split())) for _ in range(N)]

    jobs.sort(key=lambda x: (x[1], x[0]))  # 끝나는 시간, 그다음 시작 시간

    count = 0
    last_end = -1
    for s, e in jobs:
        if s >= last_end:      # 겹치지 않으면 채택
            count += 1
            last_end = e
# 리스트 형태가 아닌 튜플형태로 묶어서 받기
