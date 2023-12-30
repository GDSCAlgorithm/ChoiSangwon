from itertools import combinations_with_replacement
def solution(n, info):
    arr=[0,1,2,3,4,5,6,7,8,9,10]
    b=list(combinations_with_replacement(arr,n))
    c=[]
    count=0
    for i in range(len(b)):
        l=0
        a=0
        for j in range(11):
            if(info[j]<b[i].count(10-j)):
                l+=10-j
            elif(info[j]>=b[i].count(10-j) and info[j]!=0):
                a+=10-j
        if(l<a):
            continue
        elif(l>a):
            if(count<l-a):
                count=l-a
                c=b[i]
        else:
            continue
    answer=[0,0,0,0,0,0,0,0,0,0,0]
    if(len(c)==0):
        return [-1]
    for i in range(len(c)):
        answer[10-c[i]]+=1
    return answer