# # to check whether the number given is an amstrong number
# t=0
# i=0
# numb=input("enter a 3 digit number :")
# y=list(numb)
# while i in range(0,len(y)):
#     z=(int(y[i]))**3
#     t=t+z
#     i=i+1
# # print(y)
# # print(t)    
# if t==int(numb):
#     print("The given number is a 3 digit Amstrong Number")
# else:
#     print("The given number is not a 3 digit Amstrong Number")
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

