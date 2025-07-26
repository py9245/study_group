arr = [2, 4, 6, 8, 10]
print(arr)
def found(n):
    if n in arr:
        print(f"{n} => True")
    else:
        print(f"{n} => False")

found(5)
found(10)