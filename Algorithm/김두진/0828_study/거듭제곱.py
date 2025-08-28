for test_case in range(1,11):
    T = int(input())
    n,m = map(int,input().split())

    def zegob(n,m):
        ans = 1
        for _ in range(m):
            ans *= n
        return ans

    print(f'#{T} {zegob(n,m)}')