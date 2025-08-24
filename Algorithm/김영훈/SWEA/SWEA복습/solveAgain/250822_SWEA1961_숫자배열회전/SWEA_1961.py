# 11:26 ~ 11:56
# 회전이 안익숙하네

test = int(input())

for t in range(1, test+1):
    n = int(input())
    box = [list(map(int, input().split())) for t in range(n)]
    box_90 = list(map(list, zip(*box[::-1])))
    box_180 = list(map(list, zip(*box_90[::-1])))
    box_270 = list(map(list, zip(*box)))[::-1]
    print(f"#{t}")
    for i in range(n):
        row_1 = box_90[i]
        row_2 = box_180[i]
        row_3 = box_270[i]
        print(''.join(map(str, row_1)), ''.join(map(str, row_2)), ''.join(map(str, row_3)))