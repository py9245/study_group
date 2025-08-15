Test = int(input()) # 입력 1
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for test in range(1, Test+1):
    yeol, hang = map(int,input().split()) #yeol=3 hang=5 # 입력 2
    #print(yeol, hang)
    balloons = [] # 풍선들 위치 저장소
    # balloon = list(map(int, input().split())) # 입력 3
    for o in range(yeol):
        balloon = list(map(int, input().split()))
        balloons.append(balloon)
    # print(balloons)
    # balloon = [map(int, input().split()) for _ in range(hang)]
    Max_pang = 0 #최대 터진 값
    for i in range(yeol):
        for j in range(hang):
            pang = balloons[i][j] #현재 터진 값
            # print(pang, "현재 위치값")
            for k in range(4):
                if(0<=i+dx[k]<=yeol-1 and 0<=j+dy[k]<=hang-1):
                    # print(balloons[i+dx[k]][j+dy[k]], "조건 후 위치값")
                    pang += balloons[i+dx[k]][j+dy[k]]
            # print(Max_pang, "맥스팡값")
            Max_pang = max(Max_pang, pang)
    print(f"#{test} {Max_pang}")