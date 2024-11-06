#to remove all vowel characters from a string
stringf=(input("Enter a string :")).lower()
y=list(stringf)
# j=(stringf)
# print(stringf)
# print(y)
for i in range(0,len(stringf)):
    if y[i] in ['e','i','a','u','o']:
        y.remove(y[i])
    # if 'o' in y:
    #     y.remove('o')  
      
newstr=''.join(y)
print("Old string :",stringf)
print("New string :",newstr)
