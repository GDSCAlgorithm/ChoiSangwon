def solution(lottos, win_nums):
    answer = [6,6,5,4,3,2,1]
    zero = 0
    count = 0
    for i in range(len(lottos)):
        if(lottos[i]==0):
            zero+=1
        if(lottos[i] in win_nums):
            count+=1
        
    return [answer[zero+count],answer[count]]