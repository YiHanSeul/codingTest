from typing import Counter


def solution(s):
    answer = 0
    result=[]
    s=int(s)
    n = list(map(int,str(s)))
    
    count=Counter(n)
    print(count)
    print(dict(count))
    test =dict(count)
    for i in test:
        if test[i] >=3:
            result=test.append()
        
    print(result)



    return answer



s="12223"
solution(s);
