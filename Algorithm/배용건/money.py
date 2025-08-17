# SWEA 1970 - divmod 없이 풀이 (input() 사용)

denoms = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

T = int(input().strip())
for tc in range(1, T + 1):
    n = int(input().strip())
    counts = []
    for d in denoms:
        q = n // d     # 몫
        n = n % d      # 나머지로 금액 갱신
        counts.append(q)

    print(f"#{tc}")
    print(*counts)