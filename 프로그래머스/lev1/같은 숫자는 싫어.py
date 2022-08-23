def solution(arr):
    answer = []
    temp =[]
    for i in range(len(arr)):
        if i==0:
            temp.append(arr[i])
            answer.append(arr[i])
        else:
            if temp[-1]==arr[i]:
                temp.append(arr[i])
            else:
                answer.append(arr[i])
                temp.append(arr[i])
    return answer



arr=[1,1,3,3,0,1,1]
solution(arr)