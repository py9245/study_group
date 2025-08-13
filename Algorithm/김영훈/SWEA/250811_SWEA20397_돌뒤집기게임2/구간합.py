Test = int(input())

for test in range(1, Test+1):
    N, M = map(int, input().split())
    Ai = list(map(int, input().split()))
    max_num = 0
    Min_num = float('inf')
    # print(Max_num, " 맥스 테스트케이스")
    for i in range(N-M+1):
        num = 0
        for j in range(M):
            num+=Ai[i+j]
        # print(num1, "넘버")
        Max_num = max(Max_num, num)
        Min_num = min(Min_num, num)
        # print(Max_num,'    ', Min_num)
    print(f"#{test} {Max_num-Min_num}")