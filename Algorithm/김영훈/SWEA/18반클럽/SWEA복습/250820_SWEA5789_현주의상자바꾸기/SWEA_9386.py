test = int(input())

for t in range(1, test+1):
    n, q = map(int, input().split())
    box = [0]*n
    for i in range(1, q+1):
        l, r = map(int, input().split())
        # box[l-1:r] = i
        for j in range(l-1, r):
            box[j] = i


    box = ' '.join(map(str, box))

    print(f"#{t} {box}")