T = int(input())
for tc in range(1, T+1):
    N = int(input())
    carrots = list(map(int, input().split()))
    carrots.sort()

    # 같은 크기끼리 그룹으로 묶기
    groups = []
    cnt = 1
    for i in range(1, N):
        if carrots[i] == carrots[i-1]:
            cnt += 1
        else:
            groups.append(cnt)
            cnt = 1
    groups.append(cnt)  # 마지막 그룹 추가

    G = len(groups)

    # 그룹 누적합
    prefix = [0]*(G+1)
    for i in range(G):
        prefix[i+1] = prefix[i] + groups[i]

    ans = float('inf')

    # 경계 i, j 고르기 (i < j)
    for i in range(1, G-1):
        for j in range(i+1, G):
            small = prefix[i]
            mid = prefix[j] - prefix[i]
            big = prefix[G] - prefix[j]

            # 비어있으면 안 됨
            if small == 0 or mid == 0 or big == 0:
                continue
            # N//2 초과 불가
            if small > N//2 or mid > N//2 or big > N//2:
                continue

            diff = max(small, mid, big) - min(small, mid, big)
            ans = min(ans, diff)

    if ans == float('inf'):
        ans = -1

    print(f"#{tc} {ans}")
