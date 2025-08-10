N, K = map(int,input().split())
nums = list(map(int,input().split()))
result = 0

for i in range(N -K + 1): # n과 k 각각 10과 2일 경우, n만큼 할 경우 밑에 k반복문에서 index 범위 에러가 뜸.
    total = 0   # k반복문에서 i기준으로 k번의 숫자들의 합을 담기
    for k in range(K):
        total += nums[i + k] # 현재 i번째 위치와, k의 위치를 더해, total에 담기.
    result = max(result, total) # 현재 result값ㅅ과, total값을 비교해, 더 큰 쪽을 result에 담기
print(result)