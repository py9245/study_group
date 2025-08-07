Test = int(input())

for test in range(1, Test+1):
    number, flies_spray = map(int, input().split())
    flies_list = [list(map(int,input().split())) for _ in range(number)]
    max_flies = 0
    for i in range(len(flies_list)):
        for j in range(len(flies_list)):
            flies = 0
            # print(j, "jjjjjjj")
            if(0<=i<=len(flies_list)-flies_spray and 0<=j<=len(flies_list)-flies_spray):
                # print(flies_list[i][j+1])
                # print(j, "jjjjjjj")

                for k in range(flies_spray):
                    for l in range(flies_spray):
                        flies += flies_list[i+k][j+l]
                        # print(flies, flies_spray ,k,l,"파리들, 스프레이 세기")
                
                # flies = flies_list[i][j] + flies_list[i+flies_catch-1][j]+ flies_list[i][j+flies_catch-1] +flies_list[i+1][j+1]

            max_flies = max(max_flies, flies)
    print(f"#{test} {max_flies}")
