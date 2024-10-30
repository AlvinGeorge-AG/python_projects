#to remove all vowel characters from a string
stringf=input("Enter a string :")
y=list(stringf)
print(y)
for j in y:
    if j in ['e','i','a','u']:
        y.remove(j)
    if 'o' in y:
        y.remove('o')        
newstr=''.join(y)
print("Old string :",stringf)
print("New string :",newstr)



