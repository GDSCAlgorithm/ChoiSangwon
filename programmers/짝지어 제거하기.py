from collections import deque

def solution(s):
    q = deque()
    for i in range(len(s)):
        if(len(q)==0 or s[i]!=q[len(q)-1]):
            q.append(s[i])
        elif(s[i]==q[len(q)-1]):
            q.pop()
    return 1 if len(q)==0 else 0