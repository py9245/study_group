import sys
a = int(sys.stdin.readline())
b = list(map(int,sys.stdin.readline().split()))

sum = 0
av = 0
for i in range(len(b)):
    m = max(b)
    sum += (b[i]/m)*100
    av = sum/len(b)
print(format(av,".2f"))