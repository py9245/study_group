# Test = int(input())

# for test in range(1, Test + 1):
#     nums =[]
#     for n in range(3):
#         nums.append(list(map(int, input().split())))
#     jung = 0
#     yeok = 0
#     hang = 0
#     yeol = 0
#     max_num = 0
#     max_num2 = 0
#     for i in range(len(nums)):
#         for j in range(len(nums)):
#             hang += int(nums[i][j])
#             if (i == j):
#                 jung += nums[i][j]
#             if (len(nums) - 1 - i >= 0 and j >보다 크면 ):
#                 yeok += nums[i][len(nums) - 1 - i]
#             print(hang, jung, yeok, "행 정 역")
#             max_num = max(hang, jung, yeok)
#             print(max_num, "행 정 역 맥스")
#     for j in range(len(nums)):
#         for i in range(len(nums)):
#             yeol += nums[j][i]
#             print(yeol, "열")
#             max_num2 = max(max_num2, yeol)
#             print(max_num2, "열 맥스")
#     max_num = max(max_num, max_num2)
#     print(max_num)

# Sum 파일이 최종
