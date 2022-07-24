from string import ascii_uppercase


def solution(name):
    answer = 0
    # 알파벳을 나열함  오름차순으로
    alpha=list(ascii_uppercase)    
    print(alpha)

    cnt=0
    cnt2=0
    for i in name:
        #가깝게 갈수있는 alpha를 찾는 for문
        for j in alpha:
            cnt+=1
            if j==name:
                break
        for k in reversed(alpha):
            cnt2+=1
            if k==name:
                break
        answer=answer+min(cnt,cnt2)
        cnt,cnt2=0,0
    print(answer-1)

    return answer

name="J"
solution(name)