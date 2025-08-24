Test = int(input())

for test in range(1, Test+1):
    num = int(input())
    after = list(map(str, input().split()))
    before = list(map(str, input().split()))
    cnt = 0
    for idx, a in enumerate(after):
        if a != before[idx]:
            cnt += 1
            for jdx, b in enumerate(before):
                if idx+jdx < num:  # 전구 다르고 전구 범위 안넘으면
                    if after[idx+jdx] == '1':  # after 의 인덱스가 1이면
                        after[idx+jdx] = '0'
                    elif after[idx+jdx] == '0':
                        after[idx + jdx] = '1'
        elif a == before[idx]:
            pass
    print(f"#{test} {cnt}")