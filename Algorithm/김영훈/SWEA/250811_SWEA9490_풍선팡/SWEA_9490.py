test = int(input())
dxy = [[-1, 0], [1, 0], [0, -1], [0, 1]]  # 상, 하, 좌, 우

for t in range(1, test+1):
    hang, yeol = map(int, input().split())
    ballon = [list(map(int, input().split())) for _ in range(hang)]
    max_num = 0
    for hang_i in range(hang):
        for yeol_j in range(yeol):
            num = ballon[hang_i][yeol_j]

            for jump in range(1, ballon[hang_i][yeol_j]+1):  # 풍선 값 만큼 이동하는거


                for up_down, left_right in dxy[0:2]:  #
                    nx = hang_i+up_down*jump  #0 + -1
                    # print(ballon[hang_i][yeol_j])
                    if 0 <= nx < hang:
                        num += ballon[nx][yeol_j]
                        # print(ballon[nx+(1*jump)][yeol_j], hang_i, yeol_j, nx+(1*jump), '위치에 있는 값, 현재위치, 이동위치, 열')



                for up_down, left_right in dxy[2:]:
                    ny = yeol_j + left_right*jump
                    if 0 <= ny < yeol:
                        num += ballon[hang_i][ny]
                        # print(ballon[hang_i][ny+(1*jump)], hang_i, yeol_j, ny+(1*jump), '위치에 있는 값, 현재위치, 현재위치, 행')

            # print(num, 'num+', ballon[hang_i][yeol_j])
            max_num = max(max_num, num)
    print(max_num, 'max num')


# *ballon[hang_i][yeol_j]