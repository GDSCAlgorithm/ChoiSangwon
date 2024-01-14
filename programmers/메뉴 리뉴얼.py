from itertools import combinations
from collections import Counter
def solution(orders, course):
    answer = []
    for i in course:
        arr=[]
        for j in orders:
            tmp = sorted(j)
            arr.extend(list(combinations(tmp,i)))
        count = Counter(arr)
        b=list(count.values())
        if(len(b)>1):
            num = max(b)
            if(num<2):
                continue
            for i in count.items():
                if(i[1]==num):
                    answer.append(''.join(i[0]))
        else:
            continue
    qqq=sorted(answer)
    return qqq