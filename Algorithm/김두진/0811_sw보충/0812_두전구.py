# # DAT 알고리즘
# T = int(input())

# for tc in range(1, T + 1):
#     A, B, C, D = map(int, input().split())

#     X_dat = [0] * 101 # 최대값이 100이기 때문
#     Y_dat = [0] * 101

#     # X 전구가 켜진 시간대 dat에 기록
#     for i in range(A + 1, B + 1):
#         X_dat[i] = 1 # i 값을 dat의 인덱스로 썼다

#     # Y 전구가 켜진 시간대 dat에 기록
#     for i in range(C + 1, D + 1):
#         Y_dat[i] = 1

#     cnt = 0
#     for i in range(101):
#         if X_dat[i] == 1 and Y_dat[i] == 1: cnt += 1

#     print(f'#{tc} {cnt}')

    # -------------------
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    a,b,c,d = map(int,input().split())
    start = max(a,c)
    end = min(b,d)
    answer = end-start if end-start>0 else 0
    print(f"#{test_case} {answer}")