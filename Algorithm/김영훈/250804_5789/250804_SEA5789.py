T = int(input())
for t in range(1, T+1):
    N, Q = map(int, input().split())
    N = [0]*N # N만큼의 리스트 생성
    i = 1 # 지정된 인덱스에 추가할 수
    for q in range(Q): #상자 바꾸는 횟수, i도 증가
        L, R = map(int, input().split()) # 왼쪽, 오른쪽 지정
        for j in range(L-1,R): # 
            N[j] = i # 지정된 인덱스에 i 추가
        i+=1    # i 추가 후 증가
    print(f"#{t}", end = ' ')
    for n in N:
        print(n, end = ' ')
# L, R = input().split()
# print(type(L), L)
# N = int(input())
# N = [0]*5
# print(N[0:])
