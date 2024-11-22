# # to check whether the number given is an amstrong number
numb=input("enter a 3 digit number :")
count=0
num=0
while count<len(numb):
    num+=int(numb[count])**3
    count+=1
if num==int(numb):
    print("The given number is a 3 digit Amstrong Number")
else:
    print("The given number is not a 3 digit Amstrong Number")

