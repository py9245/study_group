
t = int(input())

for i in range(t) :
    temp = list(map(int, input().split()))
    x = round(statistics.mean(temp))
    print('#{0} {1}'.format(i+1, x))