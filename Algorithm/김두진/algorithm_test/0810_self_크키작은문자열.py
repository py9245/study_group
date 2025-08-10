t = input()
p = input()

len_t = len(t)
len_p = len(p)
arr = []
result = 0

for i in range(len_t - len_p + 1):
    arr.append(int(t[i:i+len_p]))

for k in range(len(arr)):
    if arr[k] <= int(p):
        result += 1

print(result)