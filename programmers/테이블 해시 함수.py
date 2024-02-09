def solution(data, col, row_begin, row_end):
    answer = 0
    data.sort(key=lambda x: (x[col-1], -x[0]))
    res=[]
    for i in range(row_begin-1,row_end):
        a=0
        for j in range(len(data[0])):
            a+=data[i][j] % (i+1)
        res.append(a)
    answer=res[0]
    for i in range(1,len(res)):
        answer=answer^res[i]
    
    return answer