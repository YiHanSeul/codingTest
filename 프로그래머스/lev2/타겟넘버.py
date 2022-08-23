def solution(numbers, target):
    sup= [0]
    for i in numbers:
        sub = []
        for j in sup : 
            sub.append(j+i)
            sub.append(j-i)
        sup = sub
    return  sup.count(target)

number=[1,1,1,1,1]
target=3
solution(number,target);