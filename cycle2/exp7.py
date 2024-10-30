#to find he sum of digits of a number
i=0
x=0
numb=input("enter a number :")
y=list(numb)

while i in range(0,len(y)):
    x=x+int(y[i])
    i=i+1
print(x)    
print(y)