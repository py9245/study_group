# num = int(input())

# num_list = [1]*int(num)
# cnt = 0
# for clap in range(0,len(num_list)):
#     num_list[clap] += cnt
#     if(3, 6, 9 이면 ):
#         -출력
#     elif(clap+1 이 3 이 아니면):
#         end = ' '
# for clap in range(1,int(num)+1):
#     if(str)
#     print(str(clap))
num = int(input())

num_list = [1]*num
cnt = 0
A = ''
for cl_num in range(0, len(num_list)):
    num_list[cl_num]+=cnt
    cnt+=1
print(num_list, type(num_list))
# num_list.split(',')
for nl in num_list:
    print(nl, type(nl))
    if(str(nl) == '3' or str(nl) =='6' or str(nl) == '9'):
        A += '-'
    else:
        A+=str(nl)
# for clap in num_list:
#     if (clap == 3 or clap == 6 or clap == 9):
#         clap = '-'
    
print(A)



# print(A)