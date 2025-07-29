N = int(input())
F = int(input())

N = (N//100)*100

while(N%F != 0):
    N+=1

N = N%100

if(N<10):
    print(f"0{N}")
else:
    print(f"{N}")