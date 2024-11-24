# to find the sum of  numbers in the range between upper and lower bound
def sumf():
    a=int(input("Enter the lower bound :"))
    b=int(input("Enter the higher bound :"))
    sum=0
    for i in range(a+1,b):
        sum+=i
    return sum
print(sumf()) 
# sumf()   #function calling


