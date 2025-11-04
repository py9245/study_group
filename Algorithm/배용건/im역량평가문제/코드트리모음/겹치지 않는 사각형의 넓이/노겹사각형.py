offset = 1000
x1 = [0] * 3
y1 = [0] * 3
x2 = [0] * 3
y2 = [0] * 3


x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())
x1[2], y1[2], x2[2], y2[2] = map(int, input().split())

# Please write your code here.
arr = [[0] * 2001 for _ in range(2001)]



# A 직사각형 구하기

for i in range(x1[0] + offset, x2[0] + offset):
    for j in range(y1[0] + offset, y2[0] + offset):
        arr[i][j] = 1

# B 직사각형 구하기

for i in range(x1[1] + offset, x2[1] + offset):
    for j in range(y1[1] + offset, y2[1] + offset):
        arr[i][j] = 1

# M 사각형

for i in range(x1[2] + offset, x2[2] + offset):
    for j in range(y1[2] + offset, y2[2] + offset):
        arr[i][j] -= 1

# 전체 넓이 구하기
cnt = 0
for i in range(2001):
    for j in range(2001):
        if arr[i][j] == 1:
            cnt += 1

print(cnt)
