#understanding string methods
strf='Python rules!'
#convert the string to upper case
print('Uppercase :',strf.upper())
#Locate the position of the string "rules!"
#print('Index of "rules!" :',strf.index("rules!"))
print('position :',strf.find("rules!"))
#replace the exclamation mark with a question
newstr=strf.replace('!','?')
print("Replaced data :",newstr)
