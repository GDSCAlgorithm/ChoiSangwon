def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        answer.append('%*s'%(n,str(bin(arr1[i]|arr2[i])).replace('0b','').replace('1','#').replace('0',' ')))
    return answer