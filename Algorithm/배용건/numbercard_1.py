T = int(input())

for test_case in range(1, T + 1):
    N = int(input())

    bin_list = [0] * 10  # 숫자카드 각 장수 확인용 빈리스트

    card_A = str(input())  # 리스트처럼 활용하기 위해 문자열로 받아옴

    for i in card_A:  # 숫자 하나씩 받아옴
        bin_list[int(i)] += 1  # 해당 숫자에 맞는 인덱싱 넘버에 1추가

    max_list = max(bin_list)  # 최대 장수 확인

    # print (f'#{test_case} {bin_list1} {max_list}')

    for i in range(10):  # 최대 장수인 카드숫자 확인 위한 for문
        if bin_list[i] == max_list:
            bin_list1 = i

    print(f'#{test_case} {bin_list1} {max_list}')