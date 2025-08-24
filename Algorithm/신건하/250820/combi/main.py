

def comb(arr, n):
    result = []
    if n == 1:
        return [[i] for i in arr]

    for i in range(len(arr)):
        elem = arr[i]
        for rest in comb(arr[i + 1:], n-1):
            result.append([elem] + rest)
    return result

# print (comb([1,2,3,4], 1))
print (comb([1,2,3,4], 2))
print (comb([1,2,3,4], 3))
# print (comb([1,2,3,4], 4))

print ("============================")

def perm(selected, remain):
    if not remain:
        print (selected)
    else:
        for i in range(len(remain)):
            select_i = remain[i]
            remain_list = remain[:i] + remain[i+1:]
            perm(selected + [select_i], remain_list)



perm([], [1, 2, 3])