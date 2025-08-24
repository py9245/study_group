t = int(input())
for TC in range(1,t+1):
    n = int(input())
    arr= list(map(int,input().split()))
 
    total =0
    maxp=0
    for i in range(n-1,-1,-1):
        if arr[i] > maxp:
            maxp = arr[i]
        else:
            total = total + maxp - arr[i]
    print(f"#{TC} {total}")