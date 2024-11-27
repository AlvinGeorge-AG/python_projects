check whether the given number is prime or not
n=int(input("Enter a number :"))
flag=True
for i in range(2,n):
    if n%i==0:
        flag=False
        break
if flag==True:
    print("prime Number")    
else:
    print('Not a prime')    
