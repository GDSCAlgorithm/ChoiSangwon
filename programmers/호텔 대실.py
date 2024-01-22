def changeStrToInt(time):
        return int(time[0:2]) * 60 + int(time[3:])

def solution(book_time):
    sort_time = sorted([[changeStrToInt(i[0]), changeStrToInt(i[1]) + 10] for i in book_time])
    res = []
    
    for i in sort_time:
        if len(res)==0:
            res.append(i)
            continue
        for j in range(len(res)):
            if(i[0] >= res[j][1]):
                res[j] = res[j]+i
                break
        else:
            res.append(i)
                
    return len(res)