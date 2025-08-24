# 21:14분 답
from collections import deque
import sys
sys.stdin = open('C:\\Users\\user\\Desktop\\git\\algorism\\SWEA\\18반클럽\\1_A형\\250824_SWEA5658_보물상자비밀번호\\5658_input.txt','r')

T = int(input())

for test_case in range(1, T+1):
    num, target_idx = map(int, input().split())  # 리스트갯수, 회전 횟수
    rotate_num = int(num / 4)  # 4각형이라 나누기 4
    # 근데 n = 16이면 4개 나와야되지않음? 왜 5개임?
    num_queue = deque(list(input()))  # 리스트 받는거 데큐로

    set_list = set({})  # 중복 안돼서
    for _ in range(rotate_num):  # 한 변의 넘버 갯수
        result = ""
        for idx in range(1, num+1):  # 리스트 만큼 다 돌아
            result += num_queue[idx-1]  # 도는 동안 계속 넣어
            if idx % rotate_num == 0:  # 한 변의 길이가 되면
                set_list.add(result)  # 셋리스트에 넣네
                result = ""  # 그러고 초기화 다음 변에 넘버들 넣네
        num_queue.rotate(1)  # rotate함수는 deque에서 리스트를 좌우로 회전 가능 1이면 오른쪽 한칸 이동
        # 아 그러면 이동한거에서 0 인덱스를 다시 하니까 문제대로 되네
        # 반복문 돌릴 생각이었는데 안그래도 되네 개꿀
    
    num_list = []
    for item in set_list:
        num_list.append(int(item, 16))
        # 아 이거 16진수 이렇게도 가능했지 함수 안써도된다

    num_list.sort(reverse= True)
    # 내림차순

    print(f"#{test_case} {num_list[target_idx-1]}")
