# # 3: 12
# import sys
# sys.stdin = open("1209_input.txt", "r")
#
# test = int(input())
#
# for t in range(1, test+1):
#     num = int(input())
#     abi = []
#     max_num = 0
#     min_num = float('inf')
#     for n in range(num):  # 더하기할 횟수만큼 범위를 받음
#         abi.append(list(map(int, input().split())))
#
#     p = int(input())  # 박스 크기
#
#     pp = [int(input()) for _ in range(p)]
#     print(pp)
#     box = [0]*5001  # 박스 만듦
#
#     for a, b in abi:  # 받은 범위만큼 더하기
#         # max_num = max(max_num, a, b)
#         # min_num = min(min_num, a, b)
#         for su in range(a, b+1):
#             box[su] += 1
#     print(f"#{t}")
#     for i in range(num):
#         for bus_stop in set(pp):
#             if abi[i][0] <= bus_stop <= abi[i][1]:
#                 box[bus_stop] += 1
#
#     answer = []
#     for bus_stop in pp:
#         answer.append(str(box[bus_stop]))
#
#     print(f'#{t} {" ".join(answer)}')
import sys
from collections import defaultdict

# sys.stdin = open('1209_input.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())  # 버스 노선의 개수
    but_routes = [list(map(int, input().split())) for _ in range(N)]  # 버스 노선의 개수만큼 반복하며, 각 노선의 시작과 끝 정류장을 입력받는다.
    P = int(input())  # 지나는지 확인할 버스 정류장의 개수
    p_list = [int(input()) for _ in range(P)]

    result = defaultdict(int)
    # 주어진 버스 노선 순회
    for i in range(N):
        # 확인해야 하는 정류장이 버스 노선의 범위 안에 들면, 해당 정류장에 경유하는 버스 노선 수 추가
        # 중복된 정류장이 제공될 수 있으므로, 중복을 제거해서 추가해준다.
        for bus_stop in set(p_list):
            if but_routes[i][0] <= bus_stop <= but_routes[i][1]:
                result[bus_stop] += 1
                # 주어진 순서에 맞게 순회하면서 정답 형태로 변환

    answer = []
    for bus_stop in p_list:
        answer.append(str(result[bus_stop]))

    # 출력 형식에 맞게 언패킹 후 출력
    print(f'#{tc} {" ".join(answer)}')

    # set 해야 됨