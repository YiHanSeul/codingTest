def solution(k):
    answer = []
    num ={0:6,1:2,2:5,3:5,4:4,5:5,6:6,7:3,8:7,9:6}
    temp=[]
    for i in num:
        if k==num[i]:
            answer.append(i)
        elif k>num[i] :
            temp.append(i)
    print(answer)
    print("Temp",temp)

    for i in temp:
        for j in temp:
            if num[i]+num[j]==k:
                answer.append(int(str(i)+str(j)))

    print("answer",answer)            
    return len(answer)

solution(6)