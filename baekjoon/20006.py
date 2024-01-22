p,m = map(int, input().split())

res=[]
for i in range(p):
    l,n =input().split()
    l = int(l)
    if(len(res)==0):
        res.append([(l,n)])
        continue
    flag=True
    for j in range(len(res)):
        if len(res[j])==m:
            continue
        if abs(res[j][0][0]-l)<=10:
            res[j].append((l,n))
            flag = False
            break
    if flag:
        res.append([(l,n)])

for i in res:
    i.sort(key=lambda x: x[1])
    if(len(i)==m):
        print('Started!')
    else:
        print('Waiting!')
    
    for l,n in i:
        print(l,n)