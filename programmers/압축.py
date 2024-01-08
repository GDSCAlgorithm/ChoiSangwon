def solution(msg):
    answer = []
    dic = {chr(i + 64): i for i in range(1, 27)}
    last_index = 26 
    i = 0
    result = []
    while i < len(msg):
        for j in range(len(msg), i, -1):
            if msg[i:j] in dic:
                answer.append(dic[msg[i:j]])
                if j < len(msg):
                    last_index += 1
                    dic[msg[i:j+1]] = last_index
                i = j - 1
                break
        i += 1
    return answer