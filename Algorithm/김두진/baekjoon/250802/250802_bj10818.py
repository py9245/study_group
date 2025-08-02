import sys
n = sys.stdin.readline()
m = list(map(int,sys.stdin.readline().split()))

sys.stdout.write(str(min(m)) + " " + str(max(m)))