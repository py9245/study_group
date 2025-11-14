T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    min_num = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    money = [0] * 8
    
    for i in range(len(min_num)):
        if N // min_num[i] > 0  :
            money[i] = N // min_num[i]
            N = N % min_num[i]
    print(f"#{tc}")
    print(*money)