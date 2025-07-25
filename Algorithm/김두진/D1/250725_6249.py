num_str = input()
num_int = int(num_str)

for j in range(num_int - 1):
    print(j,end=' ')
print()
for i in range(10) :
    print(num_str.count(str(i)) , end = ' ')