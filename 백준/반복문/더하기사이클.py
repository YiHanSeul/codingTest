n=int(input());

result=n
i=0
while True:
    a=result//10
    b=result%10
    sum=(a+b)%10
    result=(b*10)+sum
    i+=1
    if(n==result):
        break
print(i)
   