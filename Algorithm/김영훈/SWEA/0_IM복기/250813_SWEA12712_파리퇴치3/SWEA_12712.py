test = int(input())
dxy = [[-1, 0], [1, 0], [0, -1], [0, 1]]
dxxyy = [[-1, -1], [-1, 1], [1, 1], [1, -1]]
#
# for dx, dy in dxy:
#     print(dx, 'dx', dy, 'dy')


for t in range(1, test+1):
    size, power = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(size)]
    max_num = 0
    for i in range(size):
        for j in range(size):
            num = board[i][j]
            num2 = board[i][j]

            for dx, dy in dxy:
                for p in range(1, power):
                    if 0 <= i+(dx*p) < size and 0 <= j+(dy*p) < size:
                        num += board[i+(dx*p)][j+(dy*p)]

            for dxx, dyy in dxxyy:
                for p in range(1, power):
                    if 0 <= i+(dxx*p) < size and 0 <= j+(dyy*p) < size:
                        num2 += board[i+dxx*p][j+dyy*p]

            max_num = max(max_num, num, num2)
    print(f"#{t} {max_num}")

    # 와 레전드 20분 걸렸다
    # 수정 10분 걸림



# test = int(input())
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
# dxx = [-1, -1, 1, 1]
# dyy = [-1, 1, 1, -1]
# for t in range(1, test+1):
#     size, power = map(int, input().split())
#     board = [list(map(int, input().split())) for _ in range(size)]
#     max_num = 0
#     for i in range(size):
#         for j in range(size):
#             num = board[i][j]
#             num2 = board[i][j]
#
#             for k in range(4):
#                 for p in range(1, power):
#                     if 0 <= i+(dx[k]*p) < size and 0 <= j+(dy[k]*p) < size:
#                         num += board[i+dx[k]*p][j+dy[k]*p]
#
#             for k in range(4):
#                 for p in range(1, power):
#                     if 0 <= i+(dxx[k]*p) < size and 0 <= j+(dyy[k]*p) <size:
#                         num2 += board[i+dxx[k]*p][j+dyy[k]*p]
#
#             max_num = max(max_num, num, num2)
#     print(f"#{t} {max_num}")
#
#     # 와 레전드 20분 걸렸다