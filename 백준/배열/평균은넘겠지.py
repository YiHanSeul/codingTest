n = int(input())

max=0
min=0
result=0
for i in range(n):
    arr=list(map(int,input().split()))
    avg=(sum(arr)-arr[0])/arr[0]
    
    for i in range(2,len(arr)):
        if(i>avg):
            max+=1
    result=max/(len(arr)-1)*100
    print(result)
    max,min,avg=0,0,0
    arr.clear()
    
    