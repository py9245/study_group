import sys

sys.stdin = open("251016_boj2042.txt", "r")

N, M, K = map(int, input().split())

nums = [int(input()) for _ in range(N)]
seg_tree = [0] * (N * 4)


def build(n, s, e):
    if s == e:
        seg_tree[n] = nums[s]
        return seg_tree[n]

    mid = (s + e) // 2
    left = build(n * 2, s, mid)
    right = build(n * 2 + 1, mid + 1, e)
    seg_tree[n] = left + right
    return seg_tree[n]


def chang(n, s, e, fn, val):
    if fn < s or fn > e:
        return
    seg_tree[n] += val
    if s != e:
        mid = (s + e) // 2
        chang(n * 2, s, mid, fn, val)
        chang(n * 2 + 1, mid + 1, e, fn, val)


def find(n, s, e, fs, fe):
    if fe < s or e < fs:  # 완전히 벗어남
        return 0
    if fs <= s and e <= fe:  # 완전히 포함됨
        return seg_tree[n]
    mid = (s + e) // 2

    return find(n * 2, s, mid, fs, fe) + find(n * 2 + 1, mid + 1, e, fs, fe)


print(build(1, 0, N - 1))
chang(1, 0, N - 1, 4, 10 - nums[4])
print(seg_tree[1])
print(find(1, 0, N - 1, 3, 4))
