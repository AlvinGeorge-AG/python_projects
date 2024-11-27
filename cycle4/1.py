#Write a function to check whether the given number is even or odd. ( return True or False)
def odd_no():
    "Returns True if an Odd number"
    n=int(input("Enter a number :"))
    if n%2==0:
        R=False
    else:
        R=True
    return R
print(odd_no())
        
