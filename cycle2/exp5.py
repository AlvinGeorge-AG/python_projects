# to find the factorial of a number using for loop
n=int(input("Enter a number :"))
y=0
for i in range(0,n+1):
    y=y+n*(n-1)
print(y)    