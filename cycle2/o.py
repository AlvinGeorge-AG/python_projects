# y=1
# print(y//10)
#to print the series 1,2,4,7,11,16,.... using while loop
a=1
b=0
c=0
count=0
lt=[]
no=int(input("How many numbers you want to print:"))
while count<no:
    c=a+count
    lt.append(c)
    a=c
    count+=1
print((lt))