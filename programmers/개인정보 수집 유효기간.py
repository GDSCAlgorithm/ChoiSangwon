from datetime import datetime

def isAvailable(date,terms,today):
    year, month, day = [int(x) for x in date.split('.')]
    todayYear, todayMonth, todayDay = [int(x) for x in today.split('.')]
    if(day==1):
        terms-=1
        day=28
    else:
        day-=1
    month += terms
    year += (month-1) // 12
    month = month % 12
    if(month==0):
        month=12
    a = datetime(year,month,day)
    b = datetime(todayYear, todayMonth, todayDay)
    return a<b
    
def solution(today, terms, privacies):
    answer = []
    term = {}
    for i in terms:
        a=i.split();
        term[a[0]]=int(a[1])
    for i in range(len(privacies)):
        res = privacies[i].split()
        if(isAvailable(res[0],term[res[1]],today)):
            answer.append(i+1)
            
    return answer