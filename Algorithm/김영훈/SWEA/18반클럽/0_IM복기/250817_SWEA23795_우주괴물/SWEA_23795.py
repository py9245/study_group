# 40분 소요
test = int(input())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for t in range(1, test+1):
    n = int(input())
    box = [list(map(int, input().split())) for _ in range(n)]
    mon = []
    cnt = 0
    for idx, num in enumerate(box):
        if max(num) == 2:
            mon = [idx, num.index(2)]
    # 몬스터 위치 찾음 = mon
    for j in range(4):  # 괴물빔 방향
        for k in range(1,n): # 한방향으로 괴물빔
            mdx = mon[0]+(dx[j]*k) # 상하 한칸 본인 위치 포함
            mdy = mon[1]+(dy[j]*k) # 좌우 한칸
            # print(mdx, mdy, 'mdmdmdmdmd,,,,,,myyy')
            # print(dx[j]*n)
            if 0 <= mdx < n and 0 <= mdy < n: # 범위 제한
                if box[mdx][mdy] != 1:
                    box[mdx][mdy] = 2
                    # print('22222222222222222')
                
                elif box[mdx][mdy] == 1:
                    break
    for c in range(n):
        cnt += box[c].count(0)

    print(f"#{t} {cnt}")
