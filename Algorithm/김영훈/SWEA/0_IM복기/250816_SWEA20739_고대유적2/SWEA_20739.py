# 4:00 ~ 5:00
test = int(input())

for t in range(1, test+1):
    n, m = map(int, input().split())  # n = 상하 ,  m = 좌우
    box = [list(map(int, input().split())) for _ in range(n)]
    yeol_max = 0
    for i in range(n):  # 상하로 이동
        yeol_num = 0  # 좌우 계산

        for j in range(m):  # 좌우 이동
            if box[i][j] == 1:  # 현재 1이면
                yeol_num += 1  # 1카운트
                yeol_max = max(yeol_max, yeol_num)  # 최댓값 갱신

            else:
                yeol_num = 0
        #     elif box[i][j] == 0 or j == m-1:  # 현재값 0 or 박스 끝이면
        #         max_num = max(max_num, yeol_num)  # 최댓값 갱신
        #         yeol_num = 0  # 카운트 초기화
        # if j == m-1:  
        #     max_num = max(max_num, yeol_num)
        #     yeol_num = 0

    hang_max = 0
    for i in range(m):
        hang_num = 0
        for j in range(n):
            if box[j][i] == 1:
                hang_num += 1
                hang_max = max(hang_max, hang_num)

            else:
                hang_num = 0
        #     elif box[j][i] == 0 or j == n-1:
        #         max_num = max(max_num, hang_num)
        #         hang_num = 0
        # if j == n-1:
        #     max_num = max(max_num, hang_num)
        #     hang_num = 0
    result = max(hang_max, yeol_max)
    if(result == 1):
        result = 0
    
    print(f"#{t} {result}")