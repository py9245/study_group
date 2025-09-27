import heapq
from bisect import bisect_left

# 전역 상태
N = 0
M = 0
intervals = []        # intervals[r] = [(s,e), ...]  (start 오름차순)
current_len = []      # 각 행의 현재 max 빈 길이
buckets = []          # 길이축 0..M, 각 버킷은 "행 번호" min-heap
len_count = []        # 각 길이에 현재 속한 "유효 행" 수 (통계용; 실선택엔 의존 X)
pos = {}              # mId -> (r, a, b)

def _recompute_len(r):
    if not intervals[r]:
        return 0
    # 한 행당 구간 수 ≤ 61 → 선형 max 충분
    return max(e - s + 1 for s, e in intervals[r])

def init(n, m):
    global N, M, intervals, current_len, buckets, len_count, pos
    N, M = n, m
    intervals = [[(0, M - 1)] for _ in range(N)]
    current_len = [M] * N
    buckets = [[] for _ in range(M + 1)]
    len_count = [0] * (M + 1)
    len_count[M] = N
    for r in range(N):
        heapq.heappush(buckets[M], r)
    pos = {}

def writeWord(mId, mLen):
    global intervals, current_len, buckets, len_count, pos
    if mLen > M:
        return -1

    # mLen..M의 모든 버킷 top을 확인해 "행 번호가 가장 작은" 후보를 고른다.
    best_row = None
    best_L = None
    for L in range(mLen, M + 1):
        h = buckets[L]
        if not h:
            continue
        # stale 정리
        while h and current_len[h[0]] != L:
            heapq.heappop(h)
        if h:
            rr = h[0]  # peek
            if best_row is None or rr < best_row:
                best_row = rr
                best_L = L

    if best_row is None:
        return -1

    # 선택된 버킷에서 실제 pop
    hsel = buckets[best_L]
    while hsel and current_len[hsel[0]] != best_L:
        heapq.heappop(hsel)
    if not hsel or hsel[0] != best_row:
        # 드물게 경합 시 재시도
        return writeWord(mId, mLen)
    r = heapq.heappop(hsel)

    # 행 내부: 왼쪽부터 첫 길이 ≥ mLen 구간 사용
    row_list = intervals[r]
    seg_idx = -1
    for i, (s, e) in enumerate(row_list):
        if e - s + 1 >= mLen:
            seg_idx = i
            break
    if seg_idx == -1:
        # 모순 방지: 길이 재계산 및 재삽입 뒤 재시도
        oldL = current_len[r]
        newL = _recompute_len(r)
        if newL != oldL:
            len_count[oldL] -= 1
            len_count[newL] += 1
            current_len[r] = newL
            heapq.heappush(buckets[newL], r)
        else:
            heapq.heappush(buckets[oldL], r)
        return writeWord(mId, mLen)

    s, e = row_list[seg_idx]
    a = s
    b = s + mLen - 1
    pos[mId] = (r, a, b)

    # 왼쪽부터 채우므로 오른쪽 조각만 남음
    if b < e:
        row_list[seg_idx] = (b + 1, e)
    else:
        row_list.pop(seg_idx)

    # 길이 이동
    oldL = current_len[r]
    newL = _recompute_len(r)
    if newL != oldL:
        len_count[oldL] -= 1
        len_count[newL] += 1
        current_len[r] = newL
        heapq.heappush(buckets[newL], r)
    else:
        heapq.heappush(buckets[oldL], r)

    return r

def eraseWord(mId):
    global intervals, current_len, buckets, len_count, pos
    info = pos.pop(mId, None)
    if info is None:
        return -1
    r, a, b = info

    lst = intervals[r]
    # start 기준 삽입 위치
    i = bisect_left(lst, (a, b))

    ns, ne = a, b
    # 왼쪽 이웃과 병합
    if i > 0 and lst[i - 1][1] + 1 == ns:
        ns = lst[i - 1][0]
        i -= 1
        lst.pop(i)
    # 오른쪽 이웃과 병합
    if i < len(lst) and ne + 1 == lst[i][0]:
        ne = lst[i][1]
        lst.pop(i)

    lst.insert(i, (ns, ne))

    oldL = current_len[r]
    newL = _recompute_len(r)
    if newL != oldL:
        len_count[oldL] -= 1
        len_count[newL] += 1
        current_len[r] = newL
        heapq.heappush(buckets[newL], r)
    else:
        heapq.heappush(buckets[oldL], r)

    return r
