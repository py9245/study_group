### 프로그램은 제대로 돌아가는데 경우의 수가 너무
### 커서 시간 초과가 납니다. 
### 접근을 다르게 해봐야 할것 같습니다.
n, l = map(int, input().split())

aaa = 0
ans = 9999

ans_list = []


for i in reversed(range(n)):
    sum_max = 0
    seq = []
    for j in reversed (range(i+1)):
        sum_max += j
        seq.append(j)
        if sum_max == n and ans > len(seq) >= l:    
            ans = len(seq)
            ans_list = seq
            break
        elif sum_max > n:
            break
    if ans == l:
        break


# 정답의 길이가 l보다 작다면 -1 출력
if len(ans_list) < l:
    ans_list = -1

print (ans_list)