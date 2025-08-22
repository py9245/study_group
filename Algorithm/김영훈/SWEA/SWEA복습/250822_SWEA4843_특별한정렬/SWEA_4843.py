# 22:39 ~ 22:48

test = int(input())

for t in range(1, test+1):
    n = int(input())
    num = list(map(int, input().split()))
    num.sort()
    nl = []
    for i in range(1, n+1):
        nl.append(num[-(i)])
        nl.append(num[i-1])
        if len(nl) == 10:
            break
    print(f"#{t} {' '.join(map(str, nl))}")