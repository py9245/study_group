n = int(input())
a = list(map(str,input().split()))
b = list(map(str,input().split()))

x =int(''.join(a))
y =int(''.join(b))

if x < y :
    print(x)
elif x > y :
    print(y)
elif x == y :
    print(x)