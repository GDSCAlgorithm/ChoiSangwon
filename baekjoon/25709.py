from collections import deque

n = int(input())
q = deque()

q.append((n,0))

while len(q)!=0:
    c,count = q.pop()
    if(c<0):
        continue
    if(c==1):
        print(count+1)
        exit(0)
    if(c==0):
        print(count)
        exit(0)
    
    q.append((c-1,count+1))

    if(str(c).count("1")!=0):
        tmp = list(str(c))
        for i in range(len(tmp)):
            if(tmp[i]=='1'):
                q.append((int(str(c)[0:i]+str(c)[i+1:]),count+1))   
