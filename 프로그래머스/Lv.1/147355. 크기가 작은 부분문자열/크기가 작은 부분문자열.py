def solution(t, p):
    answer = 0
    for i in range(len(t)):
        if int(p) >= int(t[i:i + len(p)]) and len(t[i:i + len(p)]) == len(p):
            answer += 1
    
    return answer