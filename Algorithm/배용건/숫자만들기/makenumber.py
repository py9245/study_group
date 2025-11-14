import math
import sys
sys.stdin = open('sample_input1.txt', 'r')



def dfs(cnt, value, plus, minus, mul, div):
    global max_res, min_res




 # 종료조건 (선택을 할때, 선택을 안할때때)
    if cnt == N:
        max_res = max(max_res, value)
        min_res = min(min_res, value)
        return

    num = num_list[cnt]

    if plus > 0:
        dfs(cnt + 1, value + num, plus - 1, minus, mul, div)

    if minus > 0:
        dfs(cnt + 1, value - num, plus, minus - 1, mul, div)

    if mul > 0:
        dfs(cnt + 1, value * num, plus, minus, mul - 1, div)

    if div > 0:  # (음수일때 다르게 처리해야함)
        if value < 0:
            dfs(cnt + 1, -(-value // num), plus, minus, mul, div - 1)
        else:
            dfs(cnt + 1, value // num, plus, minus, mul, div - 1)

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    plus, minus, mul, div = map(int, input().split())
    num_list = list(map(int, input().split()))
    max_res = 0
    min_res = float('inf')

    dfs(1, num_list[0], plus, minus, mul, div)
    print(f"#{tc} {max_res - min_res}")