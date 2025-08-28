T = int(input())
for tc in range(1, T + 1):
    string = list(input())
    s = ''
    
    for i in range(30):
        if string[0:i+2] == string[i+2:i+4+i] :
            
            s = string[0:i+2]
            break
        
    print(f"#{tc} {len(s)}")