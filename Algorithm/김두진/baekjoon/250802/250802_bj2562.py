import sys
m = list(map(int,sys.stdin.read().split()))
print(max(m) , m.index(max(m))+1)