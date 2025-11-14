t = int(input())
for test_case in range(1, t + 1) :
    data=list(map(int, input().split()))
    s = sum([x for x in data if x % 2 == 1])
    print(f'#{test_case} {s}')