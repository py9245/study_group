def delete(lst):
    return list(dict.fromkeys(lst)) # dict.fromkeys() : 기존 리스트의 순서를 지켜주면서 중복값 제거

tes = [1, 2, 3, 4, 3, 2, 1]
result = delete(tes)
print(tes)
print(result)