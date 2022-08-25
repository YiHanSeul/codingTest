def solution(sizes):
    answer = 0
    sort=[]
    minval=[]
    maxval=[]

    for i in sizes:
        sort.append(sorted(i))
        print(sort)
    for i,j in sort:
        minval.append(i)
        maxval.append(j)

    print(max(minval),max(maxval))
    answer=max(minval)*max(maxval)
    return answer



sizes=[[60, 50], [30, 70], [60, 30], [80, 40]]
solution(sizes)