N, L, D = map(int, input().split())
# N = 곡 수
# L = 노래 길이
# D = 전화벨 울리는 주기

sum = L+5                       # 노래 끝나고부터 전화받을 수 있는 시간 범위
A=D                             #  전화벨 울리는 주기
B= L                            # 노래 끝나는 시간 구하기 위해 노래 길이
cnt = 0                         # 
for n in range(1, N+1):
    if(L<=A<L+5):
        # print(n, "if")
        break
    elif (L+5<=A<(N*B)+(N*5)):
        L += sum
        # print(n, "elif")
    while(A<L):
        A+=D
        # print(A, n, "while")
        
    # print(n,"n")
print(A)
'''
통과
'''