t = int(input())

for T in range(1,t+1):
    N = int(input())

    lst = list(map(int,input().split()))  # 받아온 값을  하나씩 나눠서 리스트에 저장

    lst.reverse() # 받아온 리스트를 반대로 정렬 ex) 3 4 6 일 때, 6 5 3

    mx = lst[0] # 최고치라는 값을 임시 반대로 정렬 된 리스트의 0번째 인덱스로 지정.
    total = 0   # 최대이익 0으로 초기화
    for i in range(1,len(lst)): # 첫번째부터 리스트 길이까지 반복
        if mx <= lst[i]: # 만약, mx 최고치가 lst[i]번째랑 비교하여 작거나 같으면    -->  8번 줄과 같이 3 4 6 일 때, mx 는 6으로 지정. 
            mx = lst[i]  # mx를 list[i] 로 변경

        else: # 아닐 시, total에 mx에서 lst[i] 값을 빼면서 총 합치기.  
            total += mx - lst[i]   # --> total += 6 - lst[i] -->  lst[1]일 때는 ,  --> total += 6 - 4 ---> total = 2 가 저장됨. 이렇게 반복하여, 최대 수익을 찾아냄

    print(f'#{T} {total}')

    # 정말 1시간동안 앉아서 생각 해봤지만, 아직 미숙하여 정답자분들의 코드를 보고 해석하면서 문제에 대한 키포인트를 얻어 , 풀게 됐습니다. 스터디를 통해 혼자서도 풀 수 있게 노력해보겠습니다.
    # 코드에 대해서는 완벽하게 이해 했습니다.
