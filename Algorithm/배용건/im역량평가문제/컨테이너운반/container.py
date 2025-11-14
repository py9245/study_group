T = int(input())
 
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    weights = list(map(int, input().split()))  # 1 5 3
    trucks = list(map(int, input().split())) # 8 3
 
    weights.sort(reverse=True) # 5 3 1
    trucks.sort(reverse=True) # 3 8
     
    total_weight = 0
 
 
    w_idx, t_idx = 0, 0
 
    while w_idx < N and t_idx < M:
        if trucks[t_idx] >= weights[w_idx]:
            total_weight += weights[w_idx]
            w_idx += 1
            t_idx += 1
        else:
            w_idx += 1
 
    print(f"#{tc} {total_weight}")