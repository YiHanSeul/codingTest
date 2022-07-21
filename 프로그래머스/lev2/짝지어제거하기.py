def solution(s):
    answer = -1
    arr=[]
    # string -> 배열로 만들기
    for i in range(len(s)):
        arr.append(s[i])
        if len(arr)>=2:
            if arr[-1] == arr[-2]:
                arr.pop()
                arr.pop()
    if len(arr)==0:
        answer=1
    else:
        answer
    return answer


s = 'cdcddee'
solution(s)