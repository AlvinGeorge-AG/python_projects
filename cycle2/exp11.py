#print fibonacci seris 0,1,1,2,3,5,8,13,...n
lastno=int(input("Enter the value of n:"))
a=1
b=0
c=0
count=0
while count<=lastno:
    print(c,end=',')
    c=a+b
    a=b
    b=c
    count+=1