#largest of 3 numbers
a=int(input("Enter the 1st no:"))
b=int(input("Enter the 2st no:"))
c=int(input("Enter the 3st no:"))
if a>b:
    if a>c:
        print(a,"is the largest number")
    else:
        print(c,"is the largest number") 
else:
    if b>c:
        print(b,"is the largest number")
    else:
        print(c,"is the largest number")
