test = int(input())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
#10t시45분 시작
# 2시간 되기 전 찐막,,
for tc in range(1, test+1):
    road_length = int(input())
    start_r , start_c = map(int, input().split())
    road = [list(map(int, input().split())) for _ in range(road_length)]
    cnt = 1
    for i in range(road_length):
        for j in range(road_length):
            next_num = [] # 값 비교할거 고도값
            next_r = [] # 다음 위치 저장 [i , j]
            now_r = [start_r, start_c] #현재 인덱스 저장  제일 마지막 초기화 됨
            
            for k in range(4): # 현재 위치로부터 4방향 검사 없으면 프로그램 끝 cnt 반환
                if 0 <= now_r[0]+dx[k] < road_length and 0 <= now_r[1]+dy[k] < road_length: # 범위 확인
                    # if road[now_r[0]+dx[k]][now_r[1]+dy[k]] < road[now_r[0]][now_r[1]]: #다음 위치가 지금 위치보다 작으면 실행
                    next_num.append(road[now_r[0]+dx[k]][now_r[1]+dy[k]]) # 값을 넣음 초기화
                    next_r.append([now_r[0]+dx[k], now_r[1]+dy[k]]) # 위치를 넣음 초기화
                    # print(next_r, "안 다음 위치")
            if min(next_num) > road[now_r[0]][now_r[1]] or next_num == []: # next_num 빈 테스트 케이스 없음
                break
            elif min(next_num) < road[now_r[0]][now_r[1]] or next_num[0] < road[now_r[0]][now_r[1]]:
                # print(next_r, "밖 다음 위치")
                # print(road[now_r[0]][now_r[1]])
                A = next_num.index(min(next_num)) # 최솟값의 인덱스 구함
                start_r, start_c = next_r[A] # 그 인덱스 넣음
                # print(start_c, start_r)
                # print(start_r, start_c,next_r[A], "스시스시")
                cnt += 1
                
            # 지금 위치보다 작은게 없으면 프로그램 끝    
    print(f"#{tc} {cnt}")
# start_r, start_c = 0, 0
# now_r = [start_r, start_c]
# print(now_r)

            
    #         #제일 낮은 걸로 이동 min 
    #         if 

    #     #     제일 낮은 걸로 이동

    #     # if 더 낮은 거 없으면 브레이크




#50분
#     test = int(input())
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# for tc in range(1, test+1):
#     road_length = int(input())
#     start_r , start_c = map(int, input().split())
#     road = [list(map(int, input().split())) for _ in range(road_length)]
#     cnt = 1
#     for i in range(road_length):
#         for j in range(road_length):
#             next_num = [] # 값 비교할거
#             now_r = [start_r, start_c] #현재 인덱스 저장 
#             next_r = [] # 다음 위치 저장
#             for k in range(4):
#                 if 0 <= now_r[0]+dx[k] < road_length and 0 <= now_r[1]+dy[k] < road_length: # 범위 확인
                    
#                     next_num.append(road[now_r[0]+dx[k]][now_r[1]+dy[k]]) # 값을 넣음
#                     next_r.append([now_r[0]+dx[k], now_r[1]+dy[k]]) # 위치를 넣음


#                 if road[now_r[0]+dx[k]][now_r[1]+dy[k]] > road[now_r[0]][now_r[1]]: # 다음 위치가 지금 위치보다 크면 브레이코
#                     break
#                 elif road[now_r[0]+dx[k]][now_r[1]+dy[k]] < road[now_r[0]][now_r[1]]: #다음 위치가 지금 위치보다 작으면 실행
#                     A = next_num.index(min(next_num)) # 최솟값의 인덱스 구함
#                     start_r, start_c == next_r[A] # 그 인덱스 넣음
#                     cnt += 1
    
#     print(cnt)

#12시 7분 50개중 44개

# test = int(input())
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# for tc in range(1, test+1):
#     road_length = int(input())
#     start_r , start_c = map(int, input().split())
#     road = [list(map(int, input().split())) for _ in range(road_length)]
#     cnt = 1
#     for i in range(road_length):
#         for j in range(road_length):
#             next_num = [] # 값 비교할거 고도값
#             next_r = [] # 다음 위치 저장 [i , j]
#             now_r = [start_r, start_c] #현재 인덱스 저장  제일 마지막 초기화 됨
            
#             for k in range(4): # 현재 위치로부터 4방향 검사 없으면 프로그램 끝 cnt 반환
#                 if 0 <= now_r[0]+dx[k] < road_length and 0 <= now_r[1]+dy[k] < road_length: # 범위 확인
#                     # if road[now_r[0]+dx[k]][now_r[1]+dy[k]] < road[now_r[0]][now_r[1]]: #다음 위치가 지금 위치보다 작으면 실행
#                         next_num.append(road[now_r[0]+dx[k]][now_r[1]+dy[k]]) # 값을 넣음 초기화
#                         next_r.append([now_r[0]+dx[k], now_r[1]+dy[k]]) # 위치를 넣음 초기화
            
#             if min(next_num) > road[now_r[0]][now_r[1]]:
#                 break
#             elif min(next_num) < road[now_r[0]][now_r[1]]:
#                 # print(road[now_r[0]][now_r[1]])
#                 A = next_num.index(min(next_num)) # 최솟값의 인덱스 구함
#                 start_r, start_c = next_r[A] # 그 인덱스 넣음
#                 # print(start_r, start_c,next_r[A], "스시스시")
#                 cnt += 1
                
             
# #             # 지금 위치보다 작은게 없으면 프로그램 끝    
#     print(f"#{tc} {cnt}")