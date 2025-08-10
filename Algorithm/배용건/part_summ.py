N, K = map(int, input().split()) # N,K 를 입력받는다

nums = list(map(int, input().split())) # 리스트를 입력받는다
ans = 0 # 최대값 변수 초기화

for i in range(len(nums) - K + 1): #시작 인덱스를 순회하기 위한 for 문 그래서 인덱스의 범위를 순회
    total = 0
    for k in range(K): # i 부터 k값을 더하기 위해 for 문 순회
        total += nums[i + k]
    ans = max(ans, total)
print(ans)