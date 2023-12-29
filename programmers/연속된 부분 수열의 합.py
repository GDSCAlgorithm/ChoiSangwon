def solution(sequence, k):
    res=[]
    end=0
    eachSum=0
    for start in range(len(sequence)):
        while eachSum<k and end<len(sequence):
            eachSum+=sequence[end]
            end+=1
        if (eachSum==k):
            res.append([start,end-1])
        eachSum-=sequence[start]

    res=sorted(res, key=lambda pair: (abs(pair[1] - pair[0]), pair[0]))
    return res[0]