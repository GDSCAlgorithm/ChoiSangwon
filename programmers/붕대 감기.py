def solution(bandage, health, attacks):
    maxTime = attacks[-1][0]
    curHealth=health
    curBandageTime=0
    
    for i in range(1,maxTime+1):
        if(curHealth<=0):
            return -1
        if(i==attacks[0][0]):
            curBandageTime=0
            curHealth-=attacks[0][1]
            del attacks[0]
            continue
        curHealth+=bandage[1]
        curBandageTime+=1
        if(curBandageTime==bandage[0]):
            curHealth+=bandage[2]
            curBandageTime=0
        if(curHealth>health):
            curHealth=health
    
    if(curHealth<=0):
        return -1
    return curHealth
