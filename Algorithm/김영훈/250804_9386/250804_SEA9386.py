T = int(input())

for test in (1, T+1): # test
    N = int(input()) # 수열 길이
    num = [] # 수열 받을 빈 리스트
    num.append(input()) #리스트에 수열 추가 [00110011]
    cnt = 0 # 1 카운트
    max_cnt = 0 # 1 카운트 최대값

    for n in num: 
        print(n, "d")
        # if(num[n] == 0):
        #     # print("0번")
        #     continue
        # elif(num[n] == 1):
        #     cnt += 1
        #     # print("elif문")
        #     if(num[n+1]==0):
        #         print("cnt 초기화")
        #         max_cnt = max(max_cnt , cnt)
        #         cnt = 0

    # print(max_cnt)


# num.pop()




    # data = [00,11,00,11]
    # for index in data:
    #     if(1 in index): #index = data 안에 각 요소들 ex) 00 or 11 or 00 or 11

    #         cnt = len(index)
    #         max_cnt = max(max_cnt, cnt)