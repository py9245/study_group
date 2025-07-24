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
이 코드 41 부터 시작해야되는데
11
13
12 이렇게 나옴
소요시간 약 1시간 
if(N[d]<Max):
       ~^^^
IndexError: list index out of range
'''