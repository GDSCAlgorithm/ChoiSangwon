def solve(a,start,count):
    tmp = count//3
    if tmp==0:
        return
    for i in range(tmp+start,start+tmp*2):
        a[i]=' '
    solve(a,start,tmp)
    solve(a,start+tmp*2,tmp)

while True:
    try:
        n=int(input())
        arr=['-']*(3**n)
        solve(arr,0,3**n)
        print("".join(arr))
    except EOFError:
        break