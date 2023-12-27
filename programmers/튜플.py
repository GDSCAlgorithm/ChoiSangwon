def solution(s):
    ddd={}
    answer = []
    #입력받은 문자열은 인덱싱해서 리스트로 만들어줌
    arr=s[2:-2:].split('},{')
    for i in arr:
        a=i.split(',')
        #str을 int로 바꿔줌
        for j in range(len(a)):
            a[j]=int(a[j])
        ddd[len(a)]=a
    #크기가 1인 것 부터 확인하면서 answer배열에 안들어가 있으면 넣고 다음으로 넘어감.
    for i in range(1,len(ddd)+1):
        for j in range(len(ddd[i])):
            if(ddd[i][j] not in answer):
                answer.append(ddd[i][j])
                break
    return answer