N , M = map(int, input().split())
pay_list = list(map(int, input().split()))
pay_num = 0
for i in range(N-M+1):
    pay = 0
    for k in range(M):
        pay += pay_list[i+k]
    pay_num = max(pay_num,pay)
print(pay_num)