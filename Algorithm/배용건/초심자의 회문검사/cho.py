T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    num = []
    for i in range(N):
        row = [1] * (i+1)
        for j in range(1,i):
            row[j] = num[i-1][j-1] + num[i-1][j]
        num.append(row)
    print(f"#{tc}")
    for row in num:
        print(" ".join(map(str, row)))