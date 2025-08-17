# T = int(input())
# for test_case in range(1,T+1):
#     n = int(input())
#     arr = list(map(int,input().split()))
#     count = 1

#     for i in range(n-1):
#         if arr[i] < arr[i+1]:
#             count += 1
#         else:
#             count = 1
        
#     print("이거다",count)
# -------------------------------------------------------
T = int(input())
for test_case in range(1, T+1):
    n = int(input())
    arr = list(map(int, input().split()))
    
    max_len = 1
    cur_len = 1

    for i in range(n-1):
        if arr[i] < arr[i+1]:
            cur_len += 1
            max_len = max(max_len, cur_len)
        else:
            cur_len = 1
    
    print(f"#{test_case} {max_len}")
