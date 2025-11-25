import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, input().strip())) for _ in range(n)]

    mid = n // 2
    sum_num = 0
    for i in range(n):
        if i <= mid:
            start = mid - i
            end = mid + i
        else:
            start = mid - (n - 1 - i)
            end = mid + (n - 1 - i)
        
        for j in range(start, end + 1):
            sum_num += arr[i][j]
    print(f"#{tc} {sum_num}")
