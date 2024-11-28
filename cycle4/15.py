#.Write a recursive function to calculate the power of a number ( x^n)
n=int(input("Enter a number :"))
p=int(input("Enter the power :"))
def pn(n,p):
    if p==0:
        return 1
    else:
        return n*pn(n,p-1)
    
print(pn(n,p))    
