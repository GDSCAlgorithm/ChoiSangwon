from functools import cmp_to_key

def cmpFile(a,b):
    if a[0].upper() > b[0].upper():
        return 1
    elif a[0].upper() < b[0].upper():
        return -1
    else:
        if int(a[1]) > int(b[1]):
            return 1
        elif int(a[1]) < int(b[1]):
            return -1
    return 0

def solution(files):
    answer = []
    res=[]
    for i in files:
        head=0
        number=0
        for j in range(len(i)):
            if head==0 and '0'<=i[j]<='9':
                head=j
            if head!=0 and number==0 and ('0'>i[j] or i[j]>'9'):
                number=j
        if(number==0):
            number=len(i)
        answer.append([i[:head],i[head:number],i[number:]])
    answer.sort(key=cmp_to_key(cmpFile))
    
    for head,number,tail in answer:
        res.append(head+number+tail)
    return res