import sys
import itertools
sys.stdin = open(".txt","r")

"""
요리사 문제는 
A 요리와 B 요리의 차를 구해 그 차가 젤 작은 최솟값을 출력하는 문제
[0,1,2,3] 중에 2개를 고르는 조합 (겹치는건 없어야함)
그래서 food_comb_list =>
[0,1],[0,2][0,3],[0,4],[1,2],[1,3],[1,4],[2,3],[2,4],[3,4] 로 조합이 된다

synerge 의 인덱스들을 
즉, N을 순회해서 리스트를 만들어줘야한다



"""
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    synerge = [list(map(int, input().split())) for _ in range(N)]
    half = N // 2 

    num_list = [i for i in range(N)] # num_list에 N 순회한 만큼 넣는다

    res = float('INF') # 최소값 변수에 무한의 최대로 큰값을 초기값으로 잡는다

    food_comb_list = itertools.combinations(num_list, half)
    for a_food_list in food_comb_list:
        

        b_food_list = []
        for x in num_list:
            if x not in a_food_list:
                b_food_list.append(x)
        
        a_synergy_sum = 0
        for i, j in itertools.combinations(a_food_list, 2):
            a_synergy_sum += synerge[i][j] + synerge[j][i]
        
        # a_synergy_list = itertools.combinations(a_food_list, 2)
        # a_food_list = 0
        # for a_synergy in a_synergy_list:
        #     i, j = a_synergy
        #     a_synergy_sum += synerge[i][j] + synerge[j][i]

        b_synergy_sum = 0
        for i, j in itertools.combinations(a_food_list, 2):
            a_synergy_sum += synerge[i][j] + synerge[j][i]
        
        # b_synergy_list = itertools.combinations(b_food_list, 2)
        # b_food_list = 0
        # for b_synergy in b_synergy_list:
        #     i, j = b_synergy
        #     b_synergy_sum += synerge[i][j] + synerge[j][i]

        res = min(res, abs(a_synergy_sum - b_synergy_sum))
    print(f"#{tc} {res}")


# 연습하기
import itertools
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    synerge = [list(map(int, input().split())) for _ in range(N)]
    half = N // 2
    
    num_list = list(range(N)) # synerge 변수들의 갯수 즉 N을 순회한 리스트 만들기
    res = float('inf') #무한대를 초기값으로 최솟값 변수만들기

    food_comb_list = itertools.combinations(num_list, half)
    for a_food in food_comb_list:
        b_food = []
        for x in num_list:
            if x not in a_food:
                b_food.append(x)


        a_synergy_sum = 0
        for i, j in itertools.combinations(a_food, 2):
            a_synergy_sum += synerge[i][j] + synerge[j][i]
        
        b_synergy_sum = 0
        for i, j in itertools.combinations(b_food, 2):
            b_synergy_sum += synerge[i][j] + synerge[j][i]
        

        res = min(res, abs(a_synergy_sum - b_synergy_sum))
    print(f"#{tc} {res}")


# 다시 연습하기 외우지말고 문제를 곱씹으면서 생각하고 풀어보기
import itertools

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    synerge = [list(map(int, input().split())) for _ in range(N)]
    half = N // 2

    res = float('inf')#최솟값 그러므로 가장 큰수를 넣어준다
    num_list = list(range(N))

    food_comb_list = itertools.combinations(num_list, half)
    for a_food in food_comb_list:
        b_food = []
        for x in num_list:
            if x not in a_food:
                b_food.append(x)
        

        a_synerge_sum = 0
        for i, j in itertools.combinations(a_food, 2):
            a_synerge_sum += synerge[i][j] + synerge[j][i]

        b_synerge_sum = 0
        for i, j in itertools.combinations(b_food, 2):
            b_synerge_sum += synerge[i][j] + synerge[j][i]

        res = min(res, abs(a_synerge_sum - b_synerge_sum)) 
    print(f"#{tc} {res}")   




    # 다시 연습해보기


import sys
import itertools
sys.stdin = open(".txt","r")
    
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    synerge = [list(map(int, input().split())) for _ in range(N)]
    res = float("inf")
    half = N // 2

    num_list = list(range(N))

    food_comb_list = itertools.combinations(num_list, half)
    for a_food in food_comb_list:
        b_food = []
        for x in num_list:
            if x not in a_food:
                b_food.append(x)
        
        a_synerge_sum = 0
        for i, j in itertools.combinations(a_food, 2):
            a_synerge_sum += synerge[i][j]+synerge[j][i]

        b_synerge_sum = 0
        for i,j in itertools.combinations(b_food, 2):
            b_synerge_sum += synerge[i][j] + synerge[j][i]

        res = min(res, abs(a_synerge_sum - b_synerge_sum))
    print(f"#{tc} {res}")