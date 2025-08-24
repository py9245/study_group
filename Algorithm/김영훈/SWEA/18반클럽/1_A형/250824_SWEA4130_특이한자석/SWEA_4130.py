# 19 : 37 47

import sys
sys.stdin = open('C:\\Users\\user\\Desktop\\git\\algorism\\SWEA\\18반클럽\\1_A형\\250824_SWEA4130_특이한자석\\4130_input.txt', 'r')

test = int(input())
for t in range(1, test+1):
    k = int(input())
    box = [list(map(int, input().split())) for _ in range(4)]
    box.insert(0, 0)
    cnt = 0
    if box[1][0] == 1:
        cnt += 1
    if box[2][0] == 1:
        cnt += 2
    if box[3][0] == 1: 
        cnt += 4
    if box[4][0] == 1:
        cnt += 8
    for i in range(k):
        tire, turn = map(int, input().split())
        for tu in range(8):
            if box[tire][tu] == 1:
                box[tire][tu] = 0
                box[tire][tu+turn] = 1
                

