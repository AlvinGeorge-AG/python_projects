#Compute nCr and nPr. Read 'n' and 'r'. Use your own factorial function ( recursive) and function to compute nCr and nPr.
n=int(input("Enter the value of n:"))
r=int(input("Enter the value of r:"))
def factorial(n):
    if n==1:
        return 1
    elif n==0:
        return 1
    else:
        return n*factorial(n-1)
print('''1-nCr\n2-nPr''')  
def nCr():
    "nCr(n) will return (n!/(r!(n-r)!)) ; n>=r"
    v=factorial(n)/((factorial(r))*factorial(n-r))
    return v
def nPr():
    v=(factorial(n))/(factorial(n-r))
    return v
H=int(input("Enter the choice (1 or 2):"))
if H==1:
    print(nCr())
else:
    print(nPr())    
