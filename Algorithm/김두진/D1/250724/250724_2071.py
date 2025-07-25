T = int(input())

for test_case in range(1, T + 1):
    N = list(map(int,input().split()))
    avg = sum(N) / len(N)
    answer = round(avg)
    
    print(f'#{test_case} {answer}')