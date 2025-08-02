import sys
n = int(sys.stdin.readline()) # 정수를 받아옴.

num = []    #빈 배열을 만들어줌. -> 첫번째 줄 말고 그 다음으로 한 줄씩 출력되는 정수를 넣기 위함.

for _ in range(n): # 처음으로 받은 정수 길이만큼, 개행처리가 된 정수들을 빈 배열에 담기.
    num.append(int(sys.stdin.readline()))

num.sort() # 받은 배열에서 정렬하기. 

for nn in num: # 정렬된 배열에서 , 하나씩 뽑아서 출력하면서 , 개행처리하기.
    sys.stdout.write(f'{nn}\n')

# 어떻게 해야 할지 생각은 났는데, 문득  sys.stdin.readline이 생각이 나서
# 찾아보면서 해보고 gpt한테도 힌트를 받으면서 했습니다
# 처음 써보는거라 구글링과 gpt를 많이 봤네요.