import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    arr.sort(key= lambda x : x[1])
    start = 0
    cnt = 0
    for s, e in arr:
        if start <= s:
            cnt += 1
            start = e
    print(f"#{tc} {cnt}")
    