import sys
sys.stdin = open("sample_input.txt","r")
from itertools import combinations

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    S = [list(map(int, input().split())) for _ in range(N)]

    # 팀 시너지 합 계산: 팀 안의 (i, j) 모든 쌍에 대해 S[i][j] + S[j][i] 더하기
    def synergy(team):
        total = 0
        team = list(team)
        for x in range(len(team)):
            for y in range(x + 1, len(team)):
                i, j = team[x], team[y]
                total += S[i][j] + S[j][i]
        return total

    best = 10**9

    # 0번을 A팀에 고정하고, 나머지 중에서 N//2 - 1 명을 뽑아 A팀 완성
    for rest in combinations(range(1, N), N // 2 - 1):
        A = (0,) + rest
        B = tuple(i for i in range(N) if i not in A)

        diff = abs(synergy(A) - synergy(B))
        if diff < best:
            best = diff

    print(f"#{tc} {best}")
