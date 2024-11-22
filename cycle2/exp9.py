#check whether the given number is prime or not
n=int(input("Enter a number :"))
for i in range(1,n+1):
    if n%i==0:
        print("The no is not a prime")
        break

