# 첫번째 방법
a = input()              
b = input().split()

result = ''

for ch in a:
    if ch in b:
        result += ch.lower()
    else:
        result += ch

print(result)

# 두번째 방법
a = input()
b = set(input().split())  

result = []  

for ch in a:
    if ch in b:
        result.append(ch.lower())
    else:
        result.append(ch)

print(''.join(result))