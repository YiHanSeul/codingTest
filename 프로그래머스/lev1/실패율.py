def solution(N, stages):
    answer = []
    fails = []
    
    for i in range(len(stages)):
        fail=0
        cnt=0
        max=0
        for j in range(len(stages)):
            if stages[i] == stages[j]:
                cnt+=1
            if stages[j]>=stages[i]:
                max+=1
        fail=cnt/max
        fails.append(fail)

    print(fails)
    print(stages)
        

    return answer


stages=[2, 1, 2, 6, 2, 4, 3, 3]
solution(5,stages)