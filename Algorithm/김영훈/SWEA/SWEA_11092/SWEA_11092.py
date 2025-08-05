Test = int(input())
for test in range(1, Test+1):
    X = int(input()) # 제외
    num_list = list(map(int,input().split()))
    max_num = max(num_list) # 리스트 내 최대값
    min_num = min(num_list) # 리스트 내 최소값
    
    for mi in range(len(num_list)): # 리스트 내 최소값 인덱스 찾기
        if(num_list[mi] == min_num):
            min_idx = mi
            break

    for ma in range(len(num_list)-1,-1,-1): # 리스트 내 최대값 인덱스 찾기
        if(num_list[ma] == max_num):
            max_idx = ma
            break
  
  
    print(f"#{test} {abs(min_idx-max_idx)}")   

    """min_idx = num_list.index(min_num)
    for ma in range(len(num_list)-1,-1,-1):
        if(num_list[ma] == max_num):
            max_idx = ma
            break
    print(f"#{test} {abs(min_idx-max_idx)}")
"""