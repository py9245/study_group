test = int(input())

for t in range(1, test+1):
    n = int(input())
    m = list(map(int, input().split()))
    max_cnt = 0
    for i in range(n):
        cnt = 0
        box_far = n - i - 1
        for j in range(i+1, n):

            if m[i] <= m[j]:
                box_far -= 1
                cnt += 1
        # print(box_far, cnt, ' farfarfarfarfarfar')

        max_cnt = max(max_cnt, box_far)
    print(f"#{t} {max_cnt}")