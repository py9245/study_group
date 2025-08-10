N, K = map(int, input().split())

nums = list(map(int, input().split()))
ans = 0

for i in range(len(nums) - K + 1):
    total = 0
    for k in range(K):
        total += nums[i + k]
    ans = max(ans, total)
print(ans)