import statistics

T = int(input())
for test_case in range(1, T+1):
    data = [] # 빈 리스트 생성
    while len(data) < 1000:
        data.extend(map(int,input().split())) # data리스트에 1000개 점수 입력받기
        
    count = [0] * 101 # 점수는 0~100까지이므로 101개 크기의 리스트 생성
    
    for score in data :
        count[score] += 1 # 점수에 해당하는 인덱스에 1씩 추가
     
    max_count = max(count)  # 가장 많이 나온 점수의 개수
    
    mode_value = max(i for i,c in enumerate(count) if c == max_count) # 최빈값 찾기.  - enumerate로 인덱스와 값을 가져오고, max_count와 같은 값을 가진 인덱스 중 최대값을 찾음
    
    print(f'#{test_case} {mode_value}') # 테스트케이스와 함께 최빈값 출력 