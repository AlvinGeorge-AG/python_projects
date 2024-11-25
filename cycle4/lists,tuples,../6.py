#Read a binary string and count the number of 1's and 0's .Use a dictionary to store the result.
strn=input("Enter a Binary number :")
store={'Number of zeros':0,'Number of Ones':0}
a=0
b=0
for i in strn:
    if int(i)==0:
        a+=1
    else:
        b+=1
store['Number of Ones']=b
store['Number of zeros']=a
print(store)