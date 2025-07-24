T = int(input())

for test_case in range(1, T + 1):
    
    lst = list(map(int, input().split()))
    sum = 0
    for i in range(len(lst)):
        
        if lst[i] % 2 == 1 :
            sum += lst[i]
        else:
            pass
    print(f"#{test_case} {sum}")