T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, input().strip())) for _ in range(N)]
    
    mid = n // 2
    total = 0
    
    for i in range(n):
        # 가운데 기준으로 얼마나 떨어졌는지
        dist = abs(mid - i)
        start = dist
        end = n - dist

        total += sum(arr[i][start:end])
    
    print(f"#{test_case} {total}")