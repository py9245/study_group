T = int(input())

for T in range(1, T+1):
    a , b = map(int, input().split()) 
    print(f"#{T} {int(a/b)} {a%b}")