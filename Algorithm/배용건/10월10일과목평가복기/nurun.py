import sys
sys.stdin = open('algo1_sample_in.txt','r')

def find_set(x):
    if x != p[x]:
        p[x] = find_set(p[x])
    return p[x]

def union(x, y):
    px = find_set(x)
    py = find_set(y)

    if px != py:
        if rank[px] > rank[py]:
            p[py] = px

        elif rank[px] < rank[py]:
            p[px] = py
        
        else:
            p[py] = px
            rank[px] += 1
            



T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    edges = []

    p = list(range(N + 1))
    rank = [0] *(N + 1)

    for _ in range(M):
        x, y, cost = map(int, input().split())
        edges.append((x, y, cost))

    edges.sort(key=lambda x: x[2])  # [2] 3번째 인덱스 기준으로   정렬을 진행 즉 가중치(비용) 기준으로 정렬함 

    total = 0

    count = 0

    for a, b, cost in edges:
        if find_set(a) != find_set(b):
            union(a, b)
            total += cost
            count += 1
            if count == N - 1:
                break
    roots = set(find_set(i) for i in range(1, N + 1)) # set 은 중복제거이기에 i 만큼 순회할때 대표자를 찾고 중복제거한다.
    if len(roots) > 1:
        print(f"#{tc} -1")    
    else:
        print(f"#{tc} {total}")
