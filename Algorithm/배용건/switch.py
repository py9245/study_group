T = int(input())
for tc in range(1, T+1):
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    count = 0
    # 현재 상태를 복사해서 작업
    curr = A[:]

    for i in range(N):
        if curr[i] != B[i]:      # 다르면 i번째 스위치 조작
            count += 1
            # i번부터 끝까지 토글
            for j in range(i, N):
                curr[j] = 1 - curr[j]   # 0->1, 1->0

    print(f"#{tc} {count}")