import sys
sys.stdin = open("input (1).txt","r")

# grade 인덱스를 맞추기 위해 10의 배수이기에 10을 나눠서 일정 배율로 나눌수 있는 부분이 필요했다



T = int(input())
grade = ['A+','A0','A-','B+','B0','B-','C+','C0','C-','D']
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    total = 0
    score_list = []
    for tc_2 in range(N):
        a, b, c = map(int, input().split())
        total_score = (a * 0.35) + (b * 0.45) + (c * 0.2)
        total += total_score
        score_list.append(total_score)

    result = score_list[K-1]
    k_score = total // result
    score_list.sort(reverse=True)
    
    for i in range(N):
        if score_list[i] == result:
            grade_idx = grade[i // (N // 10)]
    print(f"#{tc} {grade_idx}")
