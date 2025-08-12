Test = int(input())

for test in range(1, Test+1):
    num = int(input())
    after = list(map(str, input().split()))
    before = list(map(str, input().split()))
    cnt = 0
    for idx, a in enumerate(after):
        if a != before[idx]:

            for jdx in range(num):
                if idx+jdx < num:  # 전구 범위 안넘게
                    if after[idx+jdx] == 1:  # after 의 인덱스가 1이면
                        for kdx in range(after[idx+jdx], after[-1]):
                            after[kdx] = 0
                            cnt += 1
                    elif after[idx+jdx] == 0:
                        for kdx in range(after[idx+jdx], after[-1]):
                            after[kdx] = 1
                            cnt += 1
        elif a == before[idx]:
            pass
    print(cnt, after, before)