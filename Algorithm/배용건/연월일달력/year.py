T = int(input())

for tc in range(1, T+1):
    num = input()
    year = num[:4]
    month = num[4:6]
    day = num[6:8]
    
    month_dict ={
        "01" : [1, 31],
        "02" : [1, 28],
        "03" : [1, 31],
        "04" : [1, 30],
        "05" : [1, 31],
        "06" : [1, 30],
        "07" : [1, 31],
        "08" : [1, 31],
        "09" : [1, 30],
        "10" : [1, 31],
        "11" : [1, 30],
        "12" : [1, 31],
    }
    
    if not(1 <= int(month) <= 12):
        print (f"#{tc} -1")
        continue
    
    if month_dict[month][0] <= int(day) <= month_dict[month][1]:
        print (f"#{tc} {year}/{month}/{day}")
    else:
        print (f"{tc} -1")

