H=int(input())
M=int(input())


if H>0:
    if M>45:
        M-=45
    else:
        H-=1
        M+=15
elif H==0:
    if M>45:
        M-=45
    else:
        H=23
        M+=15
print(H,M)
    
    
