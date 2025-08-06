planet = {'ZRO' : 0, 'ONE' : 1, 'TWO' : 2, 'THR' : 3, 'FOR' : 4, 'FIV' : 5, 'SIX' : 6, 'SVN' : 7, 'EGT' : 8, 'NIN' : 9}
planet_num = {0 : 'ZRO', 1: 'ONE', 2: 'TWO', 3: 'THR', 4 :'FOR' ,5 : 'FIV' ,6 : 'SIX' ,7  : 'SVN' ,8 :'EGT', 9: 'NIN'}


# var = {v : k for k, v in planet.items()}
Test = int(input())
for test in range(1, Test+1):
    change_p = []
    change_pn = []
    X_num = input()
    planet_length = input().split()
    for pla in planet_length:
        change_p.append(planet[pla])
    change_p.sort()
    for cp in change_p:
        change_pn.append(planet_num[cp])
    print(f"#{test} \n{' '.join(change_pn)}")
