n= int(input())
arr=[]
cnt=0
sum=0
for i in range(n):
    score=input()
    for i in score:
        if i=='O':
            cnt+=1
            sum=sum+cnt
        elif i=='X':
            cnt=0
    print(sum)
    cnt=0
    sum=0