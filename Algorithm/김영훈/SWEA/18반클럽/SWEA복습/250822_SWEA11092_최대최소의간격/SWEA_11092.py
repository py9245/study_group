# 22 : 55 ~

test = int(input())

for t in range(1, test+1):
    n = int(input())
    box = list(map(int, input().split()))
    mam = 0
    mim = float('inf')
    for idx, i in enumerate(box):
        if i == max(box):
            mam = idx
    
    for j in range(n-1, -1, -1):
        if box[j] == min(box):
            mim = j
        result = abs(mam-mim)
    print(f"#{t} {result}")