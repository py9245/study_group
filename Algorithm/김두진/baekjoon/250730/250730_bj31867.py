N = int(input())
K = int(input())

hol = 0
zzac = 0

for i in str(K):
    if int(i) % 2 == 1:
        hol += 1
    if int(i) % 2 == 0:
        zzac += 1

if hol > zzac :
    print(1)
elif zzac > hol :
    print(0)
else:
    print(-1)