Test = int(input())

for test in range(1, Test+1):
    X = int(input())
    num_list = list(map(int, input().split()))
    num_list.sort()
    cache = [] # 결과값 임시저장
    for jegue in range(5): # 재귀느낌
        cache.append(str(num_list[-1*(jegue+1)]))
        cache.append(str(num_list[jegue]))

    result = ' '.join(cache)
    print(f"#{test} {result}")