#to find the  greatest common diviser of two numbers
def gdc(a,b):
    if a>b:
        min=b
        max=a
    else:
        min=a
        max=b
    if min==0:
        return max
    else:
        return gdc(min,max%min)
print(gdc(24,10))    
