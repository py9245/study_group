t = int(input())
for TC in range(1,t+1):
    n = int(input())
    arr= list(map(int,input().split()))
 
    total =0
    maxp=0
    for i in range(n-1,-1,-1):  # 끝에서 부터 돌려야한다
        if arr[i] > maxp:  # 인풋리스트를 순회하면서 maxp 보다 큰게 있다면 그값을 maxp로 할당한다
            maxp = arr[i]
        else:
            total = total + maxp - arr[i]  # 큰게 없다면 total 에 maxp - arr[i]  값을 갱신해준다
    print(f"#{TC} {total}")