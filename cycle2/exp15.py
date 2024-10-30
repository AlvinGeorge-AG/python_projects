#understanding string methods
strf='Python rules!'
#convert the string to upper case
print(strf.upper())
#Locate the position of the string "rules!"
print('Index of "rules!" :',strf.index("rules!"))
#replace the exclamation mark with a question
#convert strf to a list
U=list(strf)
U[12]="?"
newstr=''.join(U)
print("New String :",newstr)
