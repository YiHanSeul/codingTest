def solution(nums):
    answer = 0
    print(set(nums))

    if len(set(nums)) >len(nums)/2:
        answer =int(len(nums)/2)
    else:
        answer=len(set(nums))
    
    print(answer)
    return answer




nums=[3,1,2,3]
solution(nums)