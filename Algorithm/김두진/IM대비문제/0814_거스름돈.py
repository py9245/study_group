T = int(input())
for test_case in range(1,T+1):
    m_lst = [50000,10000,5000,1000,500,100,50,10]
    t_lst = [0,0,0,0,0,0,0,0]
    money = int(input())

for idx,value in enumerate(m_lst):
    if money >= value :
        gu = money // value
        money = money - (value*gu)
        t_lst[idx] = gu
        
print(f'#{test_case}')
print(" ".join(map(str,t_lst)))