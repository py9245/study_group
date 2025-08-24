test = int(input())

for t in range(1, test+1):
    n = int(input())
    farm_box = [list(map(int, input())) for _ in range(n)]
    down_num = 0
    up_num = 0
    sum_num = 0

    for i in range(n):
        if 0 <= n//2+i < n and 0 <= 0+i < n and 0 <= n-1-i:
            down_num += sum(farm_box[n//2+i][0+i:n-i])
            # print(down_num,i, 'ddddddddddddddd')
            up_num += sum(farm_box[n//2-i][0+i:n-i])
            # print(up_num, 'ukghjujkfgh')
    sum_num = down_num + up_num -sum(farm_box[n//2][0:])
    print(f"#{t} {sum_num}")
        
        
    #     for j in range(n-i):
            

    #             down_num=(farm_box[n//2+i][i+j])
    #             
    #             up_num+=(farm_box[n//2-i][i+j])
    #             # )
    # print(sum(farm_box[n//2][0:]))
    # sum_num = down_num + up_num -sum(farm_box[n//2][0:])
    # print(sum_num)