
def solution(n, lost, reserve):
    answer = 0

    
    lost=sorted(lost)
    reserve=sorted(reserve)
    
    reserve1=list(set(reserve)-set(lost))
    lost1=list(set(lost)-set(reserve))
    print(reserve1,lost1)
    answer=n-len(lost1)
    for i in lost1:
        for j in range(len(reserve1)):
            if i-1 ==reserve1[j]:
                answer+=1
                reserve1.pop(j)
                break
            elif i+1 == reserve1[j]:
                reserve1.pop(j)
                answer+=1
                break
    print(answer)
    return answer


n=5
lost=[2,4]
reserve=[1,2,5]

solution(n,lost,reserve)