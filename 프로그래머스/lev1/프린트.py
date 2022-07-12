def solution(priorities, location):
    answer = 0
    indexArr = []
    for i in range(len(priorities)):
        indexArr.append(i)
    #print(indexArr)
    
    copyArr = priorities.copy()
    #print(copyArr)

    
    for j in range(1,len(priorities)):
        if priorities[0]<copyArr[j]:
            priorities.append(priorities.pop(0))                
            indexArr.append(indexArr.pop(0))
        else :
            priorities.pop(0)
        print(priorities)
        
    return answer

#Test

priorities=[2, 1, 3, 2,3]
location=2
solution(priorities,location)