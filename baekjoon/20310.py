res = input()
one_len = res.count('1')
zero_len = len(res)-one_len
count=0
i=0
while True:
    if(count==one_len//2):
        break
    if(res[i]=='1'):
        res = res[:i]+res[i+1:]
        count+=1
        continue
    i+=1
i=len(res)-1
count=0
while True:
    if(count==zero_len//2):
        break
    if(res[i]=='0'):
        res = res[:i]+res[i+1:]
        count+=1
        i-=1
        continue
    i-=1
print(res)
