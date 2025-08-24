for t in range(1, 11):  # 10개
    n = int(input())
    box = list(map(int, input().split()))

    for dump in range(n):
        dax = box.index(max(box))
        din = box.index(min(box))
        d_num = max(box) - min(box)
        if d_num > 1:
            box[dax] -= 1
            box[din] += 1
        d_num = max(box) - min(box)
        if d_num <= 1:
            break
    print(f"#{t} {d_num}")