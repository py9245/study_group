t = int(input())
for t in range(1,t+1):
    a , s = input().split()
    a= int(a)
    
    result = ""
    for ch in s:
        result += ch * a
    print(result)