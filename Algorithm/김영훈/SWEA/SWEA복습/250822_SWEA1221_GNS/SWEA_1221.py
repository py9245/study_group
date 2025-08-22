# 250822 / 21:18 ~ 21:44
# import sys
# sys.stdin = open('1221_input.txt', 'r')

Pl = {'ZRO' : 0, 'ONE' : 1, 'TWO' : 2, 'THR' : 3, 'FOR' : 4, 'FIV' : 5, 'SIX' : 6, 'SVN' : 7, 'EGT' : 8, 'NIN' : 9}
Pn = {0 : 'ZRO', 1 : 'ONE', 2 : 'TWO', 3 : 'THR', 4 : 'FOR', 5 : 'FIV', 6 : 'SIX', 7 : 'SVN', 8 : 'EGT', 9 : 'NIN'}

test = int(input())
for t in range(1, test + 1):
    n, num = input().split()
    box = list(input().split())
    box_l = []
    box_n = []
    for b in box:
        box_l.append(Pl[b])
    box_l.sort()
    for bs in box_l:
        box_n.append(Pn[bs])

    print(n)
    print(*box_n)
