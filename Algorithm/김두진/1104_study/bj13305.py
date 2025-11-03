n = int(input())
city_leng = list(map(int,input().split()))
price = list(map(int,input().split()))

min_price = 0
oil = 0

for i in range(len(price)):
    for j in range(len(city_leng)):
        min_price += price[i]

print(min_price)