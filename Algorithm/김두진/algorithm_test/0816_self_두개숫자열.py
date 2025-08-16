T = int(input())
for test_case in range(1,T+1):
    n, m = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    max_sum = float('-inf') # 음수 중 최대 작은 수
    
    if n < m : 
        for i in range(m - n + 1):
            total = 0
            for j in range(n):
                total += a[j] * b[i+j]
            max_sum = max(max_sum,total)
    else:
        for i in range(n - m + 1):
            total = 0
            for j in range(m):
                total += b[j] * a[i+j]
            max_sum = max(max_sum,total)
print(f'#{test_case} {max_sum}')

