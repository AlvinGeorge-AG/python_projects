#divisiblity by 3 and 7
#Check whether the given number is divisible by 3 and 7
numb=int(input("Enter a number:"))
if numb%3==0 and numb%7==0:
    print("The number",numb," is divisible by both 7 and 3!")
else:
    print("The number",numb," is not divisible by both 7 and 3!")
