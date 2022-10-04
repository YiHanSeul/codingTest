def solution(n):
    temp=0
    answer=bin(n).count('1')

    for i in range(n+1,1000000):
        temp=bin(i).count('1')
        if answer==temp:
            answer=i
            break
    return answer

solution(15)