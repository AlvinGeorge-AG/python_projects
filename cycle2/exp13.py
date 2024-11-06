# #to remove all vowel characters from a string
stringf=(input("Enter a string :")).lower()
vow='aeiou'
newstr=''   
for i in range(len(stringf)):
    if stringf[i] not in vow:
        newstr+=stringf[i]
print(newstr)        

