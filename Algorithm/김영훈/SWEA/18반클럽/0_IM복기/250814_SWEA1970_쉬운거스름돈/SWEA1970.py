test = int(input())

for t in range(1, test+1):
    n =int(input())
    a =[50000, 10000, 5000, 1000, 500, 100, 50, 10]
    b= [0]*8
    c = ''
    for a_idx, a_num in enumerate(a):
        if n >= a_num:
            b[a_idx] = n // a_num

        n = n % a_num
    c = ' '.join(map(str, b))
    
    print(f"#{t}")
    print(c)
