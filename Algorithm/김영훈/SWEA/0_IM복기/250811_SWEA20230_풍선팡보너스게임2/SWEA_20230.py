test = int(input())
for t in range(1, test+1):
    n = int(input())
    num_box = [list(map(int, input().split())) for _ in range(n)]
    max_num = 0
    for i in range(n):
        for j in range(n):
            num = 0
            num += sum(num_box[k][j] for k in range(0, n))
            num += sum(num_box[i][0:n])
            max_num = max(max_num, (num-num_box[i][j]))

    print(f"#{t} {max_num}")