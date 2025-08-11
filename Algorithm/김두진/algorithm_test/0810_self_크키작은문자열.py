t = input()
p = input()

len_t = len(t)  # 문자열로 받아오니 , 길이로 변수 설정
len_p = len(p) #  4번줄과 같습니다.
arr = [] # p길이만큼의 단어를 잘라서 담을 리스트 초기화
result = 0 # p보다 작거나 같은 애들을 카운트 할 변수 초기화

for i in range(len_t - len_p + 1):
    arr.append(int(t[i:i+len_p])) # i번 반복하면서, arr에 p의 길이만큼 문자를 잘라 리스트에 추가

for k in range(len(arr)):   #잘라서 만들어진 리스트의 길이만큼 순회
    if arr[k] <= int(p):    # p보다 작거나 같은애들을 조건 확인하면서 
        result += 1 # reuslt에 1씩 추가.

print(result)   # 카운트 된 값 추가.