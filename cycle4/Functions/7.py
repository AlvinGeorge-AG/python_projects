#Recursive function to add two positive numbers.
def rsum(a, b):
    if b == 0:
        return a
    else:
        return rsum(a + 1, b - 1)
print(rsum(10,5))    