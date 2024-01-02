from collections import Counter

def solution(str1, str2):
    str1=str1.upper()
    str2=str2.upper()
    
    res1 = [str1[i] + str1[i+1] for i in range(len(str1)-1) if str1[i].isalpha() and str1[i+1].isalpha()]
    res2 = [str2[j] + str2[j+1] for j in range(len(str2)-1) if str2[j].isalpha() and str2[j+1].isalpha()]

    counter1 = Counter(res1)
    counter2 = Counter(res2)
    
    inter = list((counter1 & counter2).elements())
    union = list((counter1 | counter2).elements())
    
    
    if len(union) == 0 and len(inter) == 0:
        return 65536
    else:
        return int(len(inter) / len(union) * 65536)
    