#to print the following  series using for loop
# 1,3,5,7,9,
#50, 45,40,35,30,25,20,15,10,5,0
n=int(input("Enter the value of n :"))
for i in range(1,n+1,2):
    print(i,end=',')
print() 
for j in range(50,-1,-5):
    print(j,end=',')
print()    

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