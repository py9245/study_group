import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    money = int(input())

    m_list = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

    money_cnt = [0] * len(m_list)
    money_case = money
    
    for i in range(len(m_list)):
        
        if money_case >= m_list[i]:
            money_cnt[i] = money_case // m_list[i]
            money_case = money_case % m_list[i] 
        
        

    print(f"#{tc}")
    print(*money_cnt)
    