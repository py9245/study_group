# 250822 / 22:18 ~ 22:34

n = int(input())
clap = []
for i in range(1, n+1):
    clap.append(str(i))

for j in range(n):
    cnt = 0
    for k in clap[j]:
        if k == '3' or k == '6' or k == '9':
            cnt += 1
            clap[j] = ''.join('-'*cnt)
    
print(*clap)