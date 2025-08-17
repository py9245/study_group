test = int(input())

for t in range(1, test+1):
    num = int(input())
    cnt = 1

    
    se = []
    for n in range(num):
        s, e = map(int, input().split())
        se.append([s,e])
    se.sort(key=lambda x: x[1])  # 리스트에 넣고 2열 기준 오름차순정렬
    a = se[0][1]

    
    for i in range(num):
        new_time = []
        if a <= se[i][0]:  # 종료시간 <= 시작시간
            # print(a, se[i], se[i][0], '| 종료시간, 시작시간, 종료시간')
            new_time.append(se[i][1]) # 종료시간
            a = min(new_time)
            # print(a, '초기화된 종료시간')
            cnt += 1


    print(f"#{t} {cnt}")
