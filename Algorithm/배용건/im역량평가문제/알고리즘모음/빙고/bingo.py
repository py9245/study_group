import sys
sys.stdin = open('.txt', 'r')
from pprint import pprint
# UD = ((-1, 0), (1, 0))  # 위아래
# LR = ((0, 1), (0, -1))  # 좌우
# LC = ((-1, -1), (1, 1))  # 왼대
# RC = ((-1, 1), (1, -1))  # 오대

def find(box, i, idx):
    global bingo
    if sum(box[i][0:]) == 0:
        bingo += 1
    if sum([box[k][idx] for k in range(n)]) == 0:
        bingo += 1
    if i == idx:
        if sum([box[k][k] for k in range(n)]) == 0:
            bingo += 1
    if i + idx == 4:
        if sum([box[k][4-k] for k in range(n)]) == 0:
            bingo += 1
    
n = 5
box = [list(map(int, input().split())) for _ in range(n)]
box_size = n
bingo = 0
cnt = 0
while box_size:
    X_num = list(map(int, input().split()))
    idx = 0
    for l in range(5):
        cnt += 1
        for i in range(n):
            if X_num[l] in box[i]:
                idx = box[i].index(X_num[l])
                box[i][idx] = 0
                find(box, i, idx)
                # pprint(box)
                # print("@@@@@@@@@@@@@@")
                if bingo >= 3:
                    break
        if bingo >= 3:
            break
    if bingo >= 3:
        break
    box_size -= 1
print(cnt)