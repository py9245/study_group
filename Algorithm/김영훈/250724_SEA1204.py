T = int(input())
A = int(input())
Max = 0
for t in range(1, T+1):
    N = list(map(int, input().split()))
    for n in range(1, 101):
        B = 0
        B = N.count(n)
        Max = max(Max, B)
    print(f"#{t}", Max)

# 최빈수의 횟수를 구해서 최빈수를 출력해보려 합니다.(1번 결과 17 -> 17번 나온 숫자 찾기)
# #1 17 결과 나온 후 N = list(map(int, '''input()'''.split())) -> EOFError: EOF when reading a line
# 소요 시간 = 50분