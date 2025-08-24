# 20분걸림
test = int(input())

for t in range(1, test + 1):
    num = int(input())
    box = [[0] * 10 for _ in range(10)]
    cnt = 0
    for n in range(num):
        r1, c1, r2, c2, color = map(int, input().split())
        for r in range(r1, r2 + 1):
            for c in range(c1, c2 + 1):
                if color == box[r][c]:
                    pass
                elif color != box[r][c]:
                    box[r][c] += color
    for b in box:
        cnt += b.count(3)
    print(f"#{t} {cnt}")
