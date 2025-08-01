from collections import deque


T = int(input())

for tc in range(T):
    N, M, K, A, B = map(int, input().split())
    a_time = list(map(int, input().split()))
    b_time = list(map(int, input().split()))
    k_time = list(map(int, input().split()))
    
    rec_desk = [-1] * N  #시간이 흐르는거 확인용[]
    rec_visited = [[] for _ in range(N)] # 몇번 손님이 있는지 확인용 [[1],[]]
    rep_desk = [-1] * M
    rep_visited = [[] for _ in range (M)]
    
    
    rec_wait_man = deque([]) # 접수 창구 대기자1
    rep_wait_man = deque([]) # 수리 창구 대기자
    end_man = 0
    visited_man = [[] for _ in range (K+1)] # 사람별 방문한 창구 저장
    
    tt = 0
    while True:
        
        # 정비소 오는 시간
        for i in range (K):
            if tt == k_time[i]:
                rec_wait_man.append(i+1)
            elif tt < k_time[i]:
                break
                
        # 접수 데스크 입장
        for i in range(N):
            if not rec_visited[i] and rec_wait_man: #대기하는 사람이 있고 창구가 비어있어야함
                rec_visited[i] = rec_wait_man.popleft()
                visited_man[rec_visited[i]].append(i + 1) # 몇번 사람이 몇번 창구 이용했는지 저장
                rec_desk[i] = a_time[i]
    
        # 수리 데스크 입장
        for i in range (M):
            if not rep_visited[i] and rep_wait_man:
                rep_visited[i] = rep_wait_man.popleft()
                visited_man[rep_visited[i]].append(i+1) # 몇번 사람이 몇번 창구 이용했는지 저장
                rep_desk[i] = b_time[i]
        
        # 시간 지남
        for i in range (N): #접수 창구
            if rec_desk[i] > 0:
                rec_desk[i] -= 1
                if rec_desk[i] == 0 and rec_visited[i]:
                    rep_wait_man.append(rec_visited[i])
                    rec_desk[i] = -1
                    rec_visited[i] = 0
            
        for i in range (M): #수리 창구
            if rep_desk[i] > 0:
                rep_desk[i] -= 1
                if rep_desk[i] == 0:
                    end_man += 1
                    rep_desk[i] = -1
                    rep_visited[i] = 0
                
        tt += 1
        if end_man == K:
            break
    
    ans = 0
    for i in range(K+1):
        if [A, B] == visited_man[i]:
            ans += i
    if ans == 0:
        ans = -1
    print (f"#{tc+1} {ans}")