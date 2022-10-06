def solution(brown, yellow):
    answer = []
    if yellow>3:
        for i in range(1,brown+1):
            if (i*2)+(yellow/i)*2+4==brown:
                answer.append(int(yellow/i+2))
                answer.append(i+2)
                print(answer)
                break
            
    else:
        answer.append(yellow+2)
        answer.append(3)
        print(answer)
    return answer

solution(24,24)