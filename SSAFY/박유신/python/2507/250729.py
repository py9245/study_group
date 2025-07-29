a = 1
b = 2

def en():
    a = 10
    c = 3

    def lo(c):
        print(a, b, c)
    lo(500)
    print(a, b, c)
en()
print(a, b)