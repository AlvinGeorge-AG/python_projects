#Write a function that returns True if a given number is prime and False otherwise.Use this function to print all prime numbers less than N. 
# Read N. Use the same function to print n'th prime number.
n=int(input("Enter a number :"))
lt=[]
def prime(n):
    flag=True
    for i in range(2,n):
        if n==1:
            flag=False
        else:
            if n%i==0:
                flag=False
                break
            else:
                flag=True
    return flag
#subpart
print(prime(n))
lt=[]
for i in range(2,n):
    lt.append(i)
print(list(filter(prime,lt)))