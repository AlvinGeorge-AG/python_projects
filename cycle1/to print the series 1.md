#to print the series 1,2,4,7,11,16,.... using while loop
a=1
b=0
c=0
count=1
lt=[1]
no=int(input("Enter the numbers you want to enter :"))
while count<=no:
    count+=1
    c=a+count
    lt.append(c)
    a=c
print(lt)    
    
    
    
