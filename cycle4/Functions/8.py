#Recursive function to multiply two positive numbers.
def rmult(a,b):
    if b==0:
        return 0
    else:
        return a+rmult(a,b-1)
print(rmult(5,3))