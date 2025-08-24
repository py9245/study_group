T = 10
for test_case in range(1,T+1):
    n = int(input())
    arr = list(map(int,input().split()))
    total_num = 0
    for i in range(n):
        max_box = max(arr)
        min_box = min(arr)
        a = arr.index(max_box)
        b = arr.index(min_box)
        arr[a] -= 1
        arr[b] += 1
        max_box = max(arr)
        min_box = min(arr)
        total_num = max_box - min_box
        if total_num <= 1:
            break
    
    # print(arr)
    # print(max_box,min_box)
    print(f'#{test_case} {total_num}')
        
        