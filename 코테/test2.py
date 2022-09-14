user_input=input()
x=int(user_input.split(' ')[0])
y=int(user_input.split(' ')[1])
p=int(user_input.split(' ')[2])

for i in range(p):
    if x>y:
        y+=1
        p-=1
    else:
        x+=1
        p-=1
if x>y:
    print(y*2)
else :
    print(x*2)

