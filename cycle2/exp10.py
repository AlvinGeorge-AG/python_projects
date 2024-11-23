#to count the number of letters ,digits ,uppercase ,and lowercase letters in a string
strinf=input("Enter a string :")
no_cout=0
no_upper=0
no_lower=0
no_letter=0
for i in strinf:
    if i.isdigit():
        no_cout+=1
    if i.isupper():
        no_upper+=1    
    if i.islower():
        no_lower+=1    
    if i.isalpha():
        no_letter+=1
w=(strinf.split(' '))    
print('Number of digits :',no_cout)  
print("Number of Upper case letters :",no_upper)  
print('Number of lower case letters :',no_lower)
print('Number of letters :',no_letter)
print('Number of words :',len(w))