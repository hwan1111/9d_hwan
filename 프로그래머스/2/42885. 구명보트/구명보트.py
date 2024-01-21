def solution(people, limit):
    people.sort()
    answer = 0
    s, e = 0, len(people) - 1

    while s <= e:
        if people[s] + people[e] <= limit:
            s += 1
        
        e -= 1

        answer += 1

    return answer