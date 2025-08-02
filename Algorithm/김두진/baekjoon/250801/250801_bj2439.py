import sys
n = int(sys.stdin.readline())

for i in range(n):
    star = "*"*(i+1)
    print(star.rjust(n))