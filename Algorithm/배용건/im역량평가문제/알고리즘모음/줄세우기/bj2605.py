import sys
sys.stdin = open('input.txt','r')
# 첫번째로 줄을 선 학생은 무조건 0번을 받아 제일 앞에 줄을 선다
# 첫번째 학생을 만든 리스트에서 디폴트로 먼저 넣고 시작하기

# 두번째 줄을 선 학생은 

# 0번을 뽑으면 그대로 (본인 인덱스 그대로)

# 1번을 뽑으면 자기 인덱스 앞에 사람의 앞으로 감

# 세번째 줄을 선 학생은 

# 0번을 뽑으면 자기 인덱스 그대로

# 뽑은 번호만큼 본인 인덱스에서 앞으로 간다


N = int(input())
line_num = list(map(int, input().split())) 
student = list(range(1,N + 1))
real_line = []




for j in range(N):
    # if line_num[j] == 0:
    #     real_line[j] = student[j]
    # if line_num[j] != 0:
    real_line.insert(len(real_line)-line_num[j], student[j])
print(*real_line)
    



