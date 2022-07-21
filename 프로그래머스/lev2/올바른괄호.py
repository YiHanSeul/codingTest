def solution(s):
    answer = True

    cnt=0
    if s[0]==')':
        return False
    if s[-1]=='(':
        return False
    for i in s:
        if(i=='('):
            cnt+=1
        else:
            cnt-=1
    if cnt!=0:
        answer= False
    

    print(answer)
    return True


s=[')', '(', ')','(']
solution(s)
