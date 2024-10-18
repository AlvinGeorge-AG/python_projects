#Check whether the given string is palindrome.( learn slicing )
# z='MALAYALAM'
# zz=z[::-1]
y=input("Enter the string :")
yy=y[::-1]
if y==yy:
    print("The give string,",y,"is a Palindrome!")
else:
    print("The given string is not a Palindrome!")    
