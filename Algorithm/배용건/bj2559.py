N , K = map(int, input().split())
temp_list = list(map(int, input().split()))
temp_sum = 0
for i in range(N-K+1):
    temp = 0
    for k in range(K):
        temp += temp_list[i+k]
    temp_sum = max(temp,temp_sum)
print(temp_sum)