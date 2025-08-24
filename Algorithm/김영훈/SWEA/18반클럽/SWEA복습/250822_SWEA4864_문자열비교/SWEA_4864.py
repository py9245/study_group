# 22 : 51 ~ 22 : 53

test = int(input())

for t in range(1, test+1):
    n1 = input()
    n2 = input()
    cnt = 0
    if n1 in n2:
        cnt = 1
    print(f"#{t} {cnt}")