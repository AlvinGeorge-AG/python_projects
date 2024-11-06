#Check whether the given character is a vowel character
char =input("Enter a letter :")
if char in ['a','e','i','o','u']: #used membership operator in
    print('The letter ',char,',is a vowel')
else:
    print('The letter ',char,', is not a vowel')    