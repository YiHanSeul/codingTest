arr=[]

for i in range(10):
    na=int(input())%42

    if na not in arr:
        arr.append(na)

print(len(arr))