#Print prime factors of a number. Use the function isPrime(n) for checking primality.
def isPrime(n):
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
N=int(input("Enter a number :"))
for j in range(2,N):
    if N%j==0:
        if isPrime(j)==True:
            
            print(j)
