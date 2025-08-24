T = int(input())
A = int(input())
Max = 0
for t in range(1, T+1):
    N = list(map(int, input().split()))
    for n in range(1, 101):
        B = 0
        B = N.count(n)
        Max = max(Max, B)
    print(f"#{t}", Max)

'''
최빈수의 횟수를 구해서 최빈수를 출력해보려 합니다.(1번 결과 17 -> 17번 나온 숫자 찾기)
#1 17 결과 나온 후 N = list(map(int, input().split())) -> EOFError: EOF when reading a line
                                   ~^^^^^
소요 시간 = 50분
----------------------------------------------------------
T = int(input())
A = int(input())
Max = 0
t= 1
for t in range(1, T+1):
    N = list(map(int, input().split()))
    for n in range(1, 101):
        B = N.count(n)
        Max = max(Max, B)
        for d in range(0, len(N)):
            if(N[d]<Max):
                # print(N[d])
                del N[d]
            
    print(f"#{t}", N[0])
----------------------------------------------------------
T = int(input()) #test

for t in range(1, T+1):
    A = input()
    Count_1, Count_2, maxnum = 0
    N = list(map(int,input().split()))
    N.sort()
    
    # Count_2 = 0 #// 최빈수 횟수 맥스
    # while (n < N):
    #     Count_1 += 1
    #     if(N[n] < N[n+1]): # 횟수 초기화,최빈수넣음
    #         Count_2 = max(Count_2, Count_1)
    #         Count_1 = 0 #//현재값 횟수 초기화
    #         maxnum = N[n+1]
    #         elif(Count_2<Count_1):
    #             maxnum = N[n+1]
    
    for n in range(len(N)-1): #//N배열 순회 999 1000
        # if(N(n) == N(n+1))
            Count_1 += 1
        if(N[n] < N[n+1]): # 작으면 실행횟수 초기화,최빈수넣음
            if(Count_2<Count_1)
                Count_2 = max(Count_2, Count_1)
                maxnum = N[n+1]
                Count_1 = 0 #//현재값 횟수 초기화
            else:
                Count_1 = 0 #//현재값 횟수 초기화
    print(f"#{t} {maxnum}")
-----------------------------------------------------------
이 코드 41 부터 시작해야되는데
11
13
12 이렇게 나옴
소요시간 약 1시간 
if(N[d]<Max):
       ~^^^
IndexError: list index out of range
'''