import sys
sys.stdin = open('input.txt','r')

N = int(input())
n_list = [list(map(int, input().split())) for _ in range(N)]
re_list = sorted(n_list, key=lambda x: (x[1],x[0]))

one_list = re_list[0]
cnt = 1
for a, b in re_list[1:]:
    if one_list[1] <= a:
        cnt += 1
        one_list = [a, b]

print(cnt)