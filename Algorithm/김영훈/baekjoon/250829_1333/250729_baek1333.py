N, L, D = map(int, input().split()) #곡 수
# L = int(input()) #노래 길이
# D = int(input()) #전화벨 울리는 주기
sum = L+5
A=D
for n in range(1, N+1):
    
    if(L<=A<L+5):
        print(n, "if")
        break
    elif (L+5<A):
        L += sum
        print(n, "elif")
        
    while(A<L):
        A+=D
        print(A, n, "while")
    print(n)
print(A)
    # if(D<L and n == N):
    #     D=D*2
'''
새로운 반례가 계속 생기는 거 같아서 아직 푸는 중입니다.

더 풀기 전에 오늘 실습 진행완료하고 이어서 하려합니다.
'''