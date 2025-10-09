import sys
sys.stdin = open('.txt','r')


def b_c(n, k):
    dp = [[0] * (k+1) for _ in range(n+1)]

    for i in range(n+1):
        for j in range(min(i,k) + 1):
            if j == 0 or j == i:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
        
    return dp[n][k]


T = int(input())
for tc in range(1, T + 1):
    n, a, b = map(int, input().split())
