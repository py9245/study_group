# 피보나치 수 DP 코드 구현 예시


def fibo_dp(n):
    if n <= 1:
        return n  # 종료조건
    
    dp = [0] * (n + 1)  # [0,0,0,0,0,0,0,0,0 ...]
    dp[1] = 1  # [0,1,0,0,0,0,0,0,0,0,0 ...]

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    return dp[n]