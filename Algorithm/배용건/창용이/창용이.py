import sys
sys.stdin = open('s_input.txt', 'r')

def find_set(x):
    if x != p[x]:  # 부모와 내가 다르다면 대표자가 아니다
        p[x] = find_set(p[x])
        # 계속 돈다 대표자를 만날때 까지 ,
        # 만나면 대표자가 반환 되면서 모든 부모의 값이 대표자로 갱신된다.
    return p[x]

def union_set(x, y):
    #  x의 대표와 y의 대표를 가져온다.
    px = find_set(x)
    py = find_set(y)

    if px != py:  # 서로 다른 그룹일 경우에만 합친다.
        if rank[px] > rank[py]:
            p[py] = px  # 랭크 높은 쪽으로 낮은애가 붙는다
        elif rank[px] < rank[py]:
            p[px] = py
        else:
            p[py] = px
            rank[px] += 1  # 같은 경우에는 대장에 같은 랭크의 그룹이 붙기때문에
        # 결국 +1 는 대장 랭크 값



T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())

    city = [list(map(int, input().split())) for _ in range(M)]

    p = list(range(N+1))
    rank = [0] * (N+1)

    for x, y in city:
        union_set(x, y)  # 이거는 그룹화

    for i in range(1, N+1):
        p[i] = find_set(i)  # 꼭 해라잉  마지막 까지 부모찾기
        
    print(p)
    print(f"#{tc} {len(set(p)) - 1}")





