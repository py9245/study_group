from collections import deque

for t in range(1, 11):
    N = int(input())
    nums = deque(sorted(map(int, input().split())))
    cnt = N
    lgnum = deque()
    smnum = deque()
    while cnt :
        num = nums.pop()
        if nums[-1] == num :
            if not lgnum :
                lgnum.append(num - 1)
            else :
                num2 = lgnum.popleft()
                lgnum.append(num2 - 1)
                nums.append(num)
        else :
            nums.append(num - 1)
        num = nums.popleft()
        if nums[0] == num :
            if not smnum :
                smnum.append(num + 1)
            else :
                num2 = smnum.popleft()
                smnum.append(num2 + 1)
                nums.appendleft(num)
        else :
            nums.appendleft(num + 1)
    print(f"#{t} {max(max(nums),max(lgnum))-min(min(nums),min(smnum))}")
    #
    #