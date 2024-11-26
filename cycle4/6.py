#Compute nCr and nPr. Read 'n' and 'r'. Use your own factorial function ( recursive) and function to compute nCr and nPr.
n=int(input("Enter the value of n:"))
r=int(input("Enter the value of r:"))
def factorial(n):
    if n==1:
        g=1
    elif n==0:
        g=1
    else:
        g=n*factorial(n-1)
    return g  
print('''1-nCr\n2-nPr''')  
def nCr():
    "nCr(n) will return (n!/(r!(n-r)!)) ; n>=r"
    v=factorial(n)/((factorial(r))*factorial(n-r))
    return v
def nPr():
    v=(factorial(n))/(factorial(n-r))
    return v
H=input("Enter the choice (1 or 2):")
if H==1:
    print(nCr())
else:
    print(nPr())    