# a=1
# b=0
# c=0
# num=int(input("Enter the no of series: "))
# count=0
# while count<=num:
#     print(c,end=",")
#     c=a+b 
#     a=b
#     b=c
#     count+=1


#print fibonacci seris 0,1,1,2,3,5,8,13,...n
lastno=int(input("Enter the last number :"))
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