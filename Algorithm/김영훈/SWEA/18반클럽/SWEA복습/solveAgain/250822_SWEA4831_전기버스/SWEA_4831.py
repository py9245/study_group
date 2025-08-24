# <<<<<<< HEAD:SWEA/18반클럽/SWEA복습/solveAgain/250822_SWEA4831_전기버스/SWEA_4831.py
# # 17:05 ~ 17 : 50
# import sys
# sys.stdin = open("C:\\Users\\user\\Desktop\\코딩폴더 깃허브\\김영훈\\algorithm\\SWEA\\SWEA복습\\solveAgain\\250822_SWEA4831_전기버스\\4831_input.txt", "r")
# =======
# # # 17:05 ~ 17 : 50
# # import sys
# # sys.stdin = open("C:\\Users\\user\\Desktop\\코딩폴더 깃허브\\김영훈\\algorithm\\SWEA\\SWEA복습\\solveAgain\\250822_SWEA4831_전기버스\\4831_input.txt", "r")
# >>>>>>> c45410519fa408999531e482f06d215f0d5f37db:SWEA/SWEA복습/solveAgain/250822_SWEA4831_전기버스/SWEA_4831.py

test = int(input())

for t in range(1, test+1):
    k, n, m = map(int, input().split())
    num = list(map(int, input().split()))
    box = [0]*(n+1)
    for i in num:
        box[i] = i

    cnt = 0
    i = 0

    while i+k < n:
        nc = i + k
        for j in range(nc, i-1, -1):
            
            if box[j] == j:
                print('asd')
                cnt += 1
                i = j
                break
            
        
    print(cnt)

