n=int(input())

def solve(a):
    for i in range(2,int(a**(1/2))+1):
        if(a%i==0):
            return False
    return True

def solve1(a):
    lenA=len(a)
    tmp=lenA//2
    for i in range(tmp):
        if(a[i]!=a[-1-i]):
            return False
    return True

while True:
    if solve(n) and solve1(str(n)) and not n==1:
        print(n)
        exit()
    n+=1