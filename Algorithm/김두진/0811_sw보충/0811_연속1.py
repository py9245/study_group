# 그리디(욕심쟁이) 알고리즘
# 완전탐색으로 풀면 모든 경우의 수를 탐색해야하니까 시간이 오래걸림(시간초과)
# 최적의 선택을 하는 것.
# 나만의 전략대로 문제를 푼다.

# 전략 : '1'이 등장하면 counting하면서 최대값 갱신



# N개의 0과 1로 이루어진 수열에서 연속한 1의 개수 중 최대값을 출력하는 프로그램을 만드시오.

# 입력
# 첫 줄에 테스트케이스 개수 T, 다음 줄부터 테스트케이스별로 첫 줄에 수열의 길이 N, 다음 줄에 N개의 0과1로 구성된 수열이 공백없이 제공된다.
# 1<=T<=10, 10<=N<=1000

# 출력
# #과 테스트케이스 번호, 빈칸에 이어 답을 출력한다.

# 입력 예
# 3
# 10
# 0011001110
# 10
# 0000100001
# 10
# 0111001111

# 출력 예
# #1 3
# #2 1
# #3 4

# 내가 쓴 코드
T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    st = input().strip()
    m_count = 0
    count = 0

    for ch in st:
        if ch == '1':
            count += 1 # 1찾으면 현재카운트 1증가
            m_count = max(m_count,count) # 현재 카운트와 맥스카운트 비교하여 더 큰 수를 맥스카운트에 저장
        else: 
            count = 0 # 1은 덩어리로 있으니, 0만나면 현재 카운트 다시 초기화

    print(f'#{test_case} {m_count}')

# 강사님 코드
# T = int(input())
# for tc in range(1,T+1):
#     n = int(input())
#     sequence = input()

#     max_cnt = 0
#     cnt = 0
#     # for문 순회 1. 인덱싱 방식
#     # 2. interator 방식 순회
#     for seq in sequence: # 파이써닉한 방식()
#         if seq == '1':
#             count += 1 # counting
#             max_cnt = max(max_cnt,count) # 최대값 갱신
#         else:
#             count = 0
#     print(f'#{tc} {max_cnt}')
