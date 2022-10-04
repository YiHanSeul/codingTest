def solution(A,B):
    answer = 0

    A.sort()
    B.sort()
    B.reverse()

    for i in range(len(A)):
        answer+=(A[i]*B[i])
    return answer

solution([1,4,2],[5,4,4])
solution([1,2],[3,4])

# zip함수 써서 활용가능
#def getMinSum(A,B):
#return sum(a*b for a, b in zip(sorted(A), sorted(B, reverse = True)))