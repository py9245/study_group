# 2:15 ~ 3:00
test = int(input())

for t in range(1, test+1):
    n, m = map(int, input().split())
    container = list(map(int, input().split()))
    truck = list(map(int, input().split()))
    short = min(len(container), len(truck))
    container.sort()
    truck.sort()
    container.reverse()
    truck.reverse()

    # print(container)
    # print(truck)
    weight = 0

    for i in range(short):

        for j in range(short):
            # if i+j <= short:
                if truck[i] >= container[j]:
                    weight += container[j]
                    # print(truck[i], ' ijijijijijijji')
                    # print(container[j], 'ccccccccccccccc')
                    
                    container[j] = 51
                    break
                    # truck[j] = 0
                    # print(container[i])
                else:
                    continue
    print(f"#{t} {weight}")