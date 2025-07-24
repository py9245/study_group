N = list(map(int, input().split(','))) # split('.') , 기준으로 구분하기
for i in range(len(N)):
    a = N[i] * N[i]
    print(f'square({N[i]}) => {a}')