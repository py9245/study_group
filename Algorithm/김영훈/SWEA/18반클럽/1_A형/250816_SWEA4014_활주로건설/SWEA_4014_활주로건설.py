# import sys
# sys.stdin = open('sample_input.txt', 'r')

test = int(input())

for t in range(1, test+1):
    n, m = map(int, input().split())
    box = [list(map(int, input().split())) for _ in range(n)]
    hwal = 0
    for h in [box, list(zip(*box))]:
        for i in range(n):
            cnt = 1
            for j in range(n-1):

                if h[i][j] - h[i][j+1] == 1:  # down
                    if cnt < 0:
                        break
                    cnt = -(m-1)
                    # down cnt
                
                elif h[i][j] - h[i][j+1] == 0:
                    cnt += 1
                    
                elif h[i][j] - h[i][j+1] == -1:  # up
                    if cnt < m:
                        break
                    cnt = 1
                    #up cnt
                
                else:
                    break
            else:
                if cnt >= 0:
                    hwal += 1
    print(f"#{t} {hwal}")
















# 3 3 3 2 1 1
# 3 3 3 2 2 1
# 3 3 3 3 3 2
# 2 2 3 2 2 2
# 2 2 3 2 2 2
# 2 2 2 2 2 5