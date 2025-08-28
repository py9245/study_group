t = int(input())
 
for T in range(1,t+1):
    N = int(input())
    lst = list(map(int,input().split()))
    lst.reverse()
    mx = lst[0]
    total = 0
    
    for i in range(1,len(lst)):
        if mx <= lst[i]:
            mx = lst[i]
        else:
            total += mx - lst[i]
 
 
    print(f'#{T} {total}')