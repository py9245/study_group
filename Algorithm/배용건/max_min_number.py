T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    n_list = list(map(int, input().split()))

    min_val = n_list[0] # 최소값 초기 값
    min_index = 1 # 최소값 인덱스 변수
    for i in range(1,N): #최소값 빼고 순회
        if n_list[i] < min_val: 
            min_val = n_list[i]
            min_index = i + 1 # 최소값 정해지면 i 값을 인덱스로 최신화
    
    max_val = n_list[0] # 최대값 초기 값
    max_index = 1 # 최대값 인덱스 변수
    for i in range(N): 
        if n_list[i] > max_val:
            max_val = n_list[i]
            max_index = i + 1 #최대값 정해지면 i 값을 인덱스로 최신화
        elif n_list[i] == max_val:
            max_val = n_list[i]
            max_index = i + 1 #같은 최대값이 나올겨우 최근 i 값으로 인덱스 최신화
    
    ans = abs(max_index - min_index)
    print(f"#{tc} {ans}")