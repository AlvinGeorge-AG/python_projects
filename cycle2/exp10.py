# to check whether the number given is an amstrong number
t=0
i=0
numb=input("enter a number :")
y=list(numb)
while i in range(0,len(y)):
    z=(int(y[i]))**3
    t=t+z
    i=i+1
# print(y)
# print(t)    
if t==int(numb):
    print("The given number is an Amstrong Number")
else:
    print("The given number is not an Amstrong Number")


