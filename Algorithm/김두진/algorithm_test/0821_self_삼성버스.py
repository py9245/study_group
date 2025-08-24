from collections import defaultdict
T = int(input())
for test_case in range(1,T+1):
    # result = [0]*5001

    # n = int(input())
    # for nosun in range(n):
    #     a1,b1 = map(int,input().split())
    #     for j in range(a1,b1+1):
    #         result[j] += 1
    
    # p = int(input())
    # bus_list = []
    # for i in range(p):
    #     a = int(input())
    #     bus_list.append(a)

    # print('#{}'.format(test_case), end=' ')
    # for i in bus_list:
    #     print(result[i], end=' ')
    # print()
    # ------------------------------------------------------------
    # result = [0] * 5001
    # bus = []
    # aa = []
    # n = int(input())
    # for i in range(n):
    #     a1,b1 = map(int,input().split())
    #     for j in range(a1,b1+1):
    #         result[j] += 1
    # p = int(input())
    # for i in range(p):
    #     a = int(input())
    #     bus.append(a)
    
    # for i in range(len(bus)+1):
    #     if result[i] in bus:
    #         aa.append(result[i])
    
    
    # print(f'#{test_case} {" ".join(map(str,aa))}')
    # 실패 
    # ---------------------------------------------------------------
    n = int(input())  # 버스 노선의 개수
    bus_list = [list(map(int, input().split())) for _ in range(n)]
    P = int(input())  
    p_list = [int(input()) for _ in range(P)]

    result = defaultdict(int)
    for i in range(n):
        for stop in set(p_list):
            if bus_list[i][0] <= stop <= bus_list[i][1]:
                result[stop] += 1
    
    