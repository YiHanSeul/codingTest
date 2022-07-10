def solution(progresses, speeds):
    cnt=0
    answer = []
    print(progresses)
    print(len(progresses))
    print(progresses+3)

    # 100채울때까지 반복하는 코드
    for i in progresses[i]>=100:
        progresses[i]=progresses[i]+speeds[i]
        progresses[i+1]=progresses[i+1]+speeds[i+1]
        progresses[i+2]=progresses[i+2]+speeds[i+2]
        if progresses>=100:
            for j in progresses[j]<100:
                if progresses[j]>=100:
                    cnt+=1;
                    answer.append(cnt)
                cnt=0
            j=0
        i=0
    print(answer)
    return answer

progresses=[93, 30, 55]
speeds=[1, 30, 5]
solution(progresses,speeds)
