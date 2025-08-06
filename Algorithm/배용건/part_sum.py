T = int(input())

for i in range(1, T + 1):
    N , M = map(int, input().split())
    N_list = list[int, input().split()]
    min_num = 10000
    max_num = 0
    count = 0
    for j in N_list: #아직 for 문 범위 지정이 익숙치 않은것 같다
        count += 1
        
        min_num = sum(j)
    for j in N_list:
        count += 1
        max_num = sum(j)

    print(f'#{i} {max_num - min_num}')

# 원래 의도는 입력 리스트 값을 N_list 로 받아오면
# for문을 통해 리스트의 (0,M+1) 순회시켜 
# 그 리스트의 합을 최소값
# 비슷한 방법으로 최댓값 구하고 
# 진행하고 싶었는데 아쉽다
