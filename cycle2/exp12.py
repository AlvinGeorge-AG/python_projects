#to count the number of vowel characters in a string
string=input("Enter a string :")
vow="aeiou"
count=0
for i in string:
    if i in vow:
        count+=1


