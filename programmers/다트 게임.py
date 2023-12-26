def solution(dartResult):
    result = [0,0,0]
    a = ['S','D','T']
    cur=''
    cnt=0
    for i in range(len(dartResult)):
        if(dartResult[i]=='*'):
            if(cnt>1):
                result[cnt-1]*=2
                result[cnt-2]*=2
            else:
                result[cnt-1]*=2
            continue
        if(dartResult[i]=='#'):
            result[cnt-1]*=-1
            continue
        if(dartResult[i]<'0' or dartResult[i]>'9'):
            result[cnt]=int(cur)
            if(dartResult[i]=='D'):
                result[cnt]*=result[cnt]
            if(dartResult[i]=='T'):
                result[cnt]*=result[cnt]*result[cnt]
            cur=''
            cnt+=1
        else:
            cur+=dartResult[i]
        
    return sum(result)