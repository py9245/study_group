# 이준영30 20 : 15 답 20: 55 끝
from collections import deque
import sys
sys.stdin = open('C:\\Users\\user\\Desktop\\git\\algorism\\SWEA\\18반클럽\\1_A형\\250824_SWEA4130_특이한자석\\4130_input.txt', 'r')

T = int(input())

for test_case in range(1, T +1):
    rt_cnt = int(input())  # 회전 횟수
    magnet_list = [deque(map(int, input().split())) for _ in range(4)]
    rt_queue = deque(tuple(map(int, input().split())) for _ in range(rt_cnt)) # 방향

    while rt_queue:  # 회전 받은 게 있으면
        cm, cr = rt_queue.popleft()  # 회전 리스트에서 첫번째부터 자석, 회전방향 넣음
        rotate_info = [False] * 4  # ???
        queue = deque([(cm, cr)])  # 자석번호, 회전 방향 데큐형식으로 넣음?
        rotate_info[cm-1] = cr  # false에 회전 방향

        delta_list = (-1, 1)  # 델타 리스트 
        while queue:  # BFS? | 데큐(자석번호, 회전방향) 있으면
            current_magnet, current_rotate = queue.popleft()  # 현재 기준 회전 시작
            #  자석 번호,      회전 방향 꺼냄
            current_magnet_idx = current_magnet - 1

            for delta in delta_list:  # 델타 탐색 두번 함??
                next_magnet_idx = current_magnet_idx + delta  # 아 이거 앞뒤 자석?
                if 0 <= next_magnet_idx < 4:  # 델타 탐색이 범위 이내 라면 | 자석?
                    if not rotate_info[next_magnet_idx]:  # 방문 정보  False면 실행 True면 안하고
                        if current_magnet_idx < next_magnet_idx:  # 현재 기준 오른쪽 자석과 비교
                            if magnet_list[current_magnet_idx][2] != magnet_list[next_magnet_idx][6]:  # 오른쪽 자석과 연결된거 비교
                                rotate_info[next_magnet_idx] = current_rotate * -1
                                # 아 내 자석 방향이랑 앞뒤 자석은 반대가 돼야지
                                # 그리고 false에 값넣어서 방문처리함
                                # 잘 이해안됨
                                queue.append((next_magnet_idx + 1, rotate_info[next_magnet_idx]))  # 다음 자석 번호, 회전방향
                # current_magnet_idx(자석 인덱스번호), next_magnet_idx(현재자석기준 앞뒤자석)
                # rotate_info(False), current_rotate(시계, 반시계 방향)
                        elif next_magnet_idx < current_magnet_idx:  # 현재 기준 왼쪽 자석과 비교
                            if magnet_list[current_magnet_idx][6] != magnet_list[next_magnet_idx][2]:
                                rotate_info[next_magnet_idx] = current_rotate * -1
                                queue.append((next_magnet_idx + 1, rotate_info[next_magnet_idx]))

        for rotate in range(4):
            magnet_list[rotate].rotate(rotate_info[rotate])
            # ??? 머임 이거? 점수 내는 거 같은데 어케 함

    sum = 0
    cal_list = [1, 2, 4, 8]
    for idx in range(4):
        sum += magnet_list[idx][0] * cal_list[idx]
    print(f"#{test_case} {sum}")
