#.Write a Python program to read list of positive integers and separate the prime and composite numbers into two different list.( Use a function to check primality)
def prime(n):
    flag=True
    for i in range(2,n):
        if n%i==0:
            flag=False
            break
    if n==1:
        return False
    if flag==True:
        return True
    else:
        return False  
N=int(input("How many numbers you want to enter :"))
lt=[]
pr=[]
co=[]
for i in range(N):
    n=int(input('Enter the number :'))
    if n==1:
        continue
    if prime(n)==True:
        pr.append(n)
    else:
        co.append(n)
print('prime =',pr)
print('composite =',co)
