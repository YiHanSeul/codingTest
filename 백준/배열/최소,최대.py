n=int(input())
number =list(map(int,input().split()))
max=number[0]
min=number[0]
for i in number:
    if max<i:
        max=i
    if min>i:
        min=i

print(min,max)
