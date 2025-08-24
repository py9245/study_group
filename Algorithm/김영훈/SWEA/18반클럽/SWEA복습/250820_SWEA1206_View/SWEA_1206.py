# 8시 47분 시작
# 9시 12분 끝(패스)

for t in range(1, 11):
    n = int(input())
    build = list(map(int, input().split()))
    cnt = 0
    for i in range(2, n-2):
        mb = max(build[i-2:i])
        nmb = max(build[i+1:i+3])
        # print(mb,nmb, '\n', build[i])
        if build[i] == max(build[i-2:i+3]):
            cnt += build[i] - max(mb, nmb)
    # print(mb)
    print(f"#{t} {cnt}")    

# 10
# 0 0 254 185 76 227 84 175 0 0

# 10
# 0 0 254 185 76 227 84 175 0 0
# 10
# 0 0 251 199 176 27 184 75 0 0
# 11
# 0 0 118 90 243 178 99 100 200 0 0