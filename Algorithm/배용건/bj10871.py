N, X = map(int, input().split())
A = list(map(int, input().split()))
x_list = 0

for i in A:
    if i < X :
        x_list = i
        
        print(x_list, end=" ")