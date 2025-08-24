test = int(input())

for t in range(1, test+1):
    n, m = map(int, input().split())
    ai, bj = (list(map(int, input().split())) for _ in range(2))
    max_num = 0
    if n <= m:
        
        for i in range(m-n+1):
            num = 0
            for j in range(n):
                if i+j <= m:
                    num += bj[i+j]*ai[j]
                    # print(bj[i+j]*ai[j], ' dasdasdsadsa')
            max_num = max(max_num, num)


    elif n > m:
        for i in range(n-m+1):
            num = 0
            for j in range(m):
                if i+j <= n:
                    num += bj[j]*ai[i+j]
                    # print(bj[j]*ai[i+j], ' aaaaaaaaaaaaaaai')
            max_num = max(max_num, num)
    
    print(f"#{t} {max_num}")