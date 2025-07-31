while True:
    a = input()
    count = 0
    if a == '#':
        break
    for i in range(len(a)):
        if a[i] == 'a' or a[i] == 'A' or a[i]=='e' or a[i]=='E' or a[i] =='i'or a[i] == 'I' or a[i] == 'o' or a[i]=='O' or a[i] == 'u' or a[i]=='U':
            count+=1
    print(count)

## upper 나 lower로 활용해서 카운트 할려 했는데, 오늘은 머리가 멈춘거 같습니다..