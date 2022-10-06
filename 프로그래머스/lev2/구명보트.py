from collections import deque

def solution(people, limit):
    answer = 0
    people.sort()
    people=deque(people)
    
    while len(people)>=1:
        if people[0] +people[-1] <=limit and len(people)>1:
            people.pop()
            people.popleft()
            answer+=1
        else:
            people.pop()
            answer+=1 
        #50,50,70,80
    return answer