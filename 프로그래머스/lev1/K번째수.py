def solution(array, commands):
    answer = []
    temp=[]
    print(array)
    print(commands)

    
    for i,j,k in commands:
        print(i,j,k)
        slice = array[i-1:j]
        print("slice : ",slice)
        slice=sorted(slice)
        print("sortSlice: ",slice)
        for s in slice:
            temp.append(s)
            print("temp",temp)
        answer.append(temp[k-1])
        temp.clear()
        print("answer",answer)
        
        
    return answer



array=[1,5,2,6,3,7,4]
commands=[[2,5,3],[4,4,1],[1,7,3]]
solution(array,commands)