#Check whether the given character is alphabet or digit 
char=input("Enter the character :")
if char.isalpha():
    print("The character ",char,"is an Alphabet")
elif char.isdigit():
    print("The character",char,"is a digit")    