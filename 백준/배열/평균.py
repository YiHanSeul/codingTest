cnt=int(input())
arr=list(map(int,input().split()))
result=[]
for i in arr:
    result.append(round(i/max(arr)*100,2))
print(sum(result)/len(result))
