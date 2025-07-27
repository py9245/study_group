T = int(input())

for t in range(1, T + 1):
    A, B = map(int, input().split())
    C = [0]
    D = 0
    E = 0    
    for n in range(1, 11): #패턴 만듦
        C.append((A**n)%10)
        if((A**n)%10 == 0):
            E = 10
            break
        elif(C.count(C[n]) > 1):
            del C[0], C[-1]
            D = (B-1)%len(C)
            break
    if(E == 10):
        print(E)
    else:
        print(C[D])
        

'''
시간 줄이기 위해 공부하다가 pow(A, B, 10) 을 알게 되었습니다.
(A의 B제곱을 10으로 나눈 나머지를 구하는 함수)

문제 풀이는
(A의 B제곱) 마다 패턴을 갖는다는 힌트를 얻고 풀었습니다..

'''