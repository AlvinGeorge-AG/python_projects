#Check whether the given string is palindrome.( learn slicing )
# z='MALAYALAM'
# zp=z[::-1]
y=input("Enter the string :")
yp=y[::-1]
if y==yp:
    print("The given string,",y," is a Palindrome!")
else:
    print("The given string is not a Palindrome!")    
#