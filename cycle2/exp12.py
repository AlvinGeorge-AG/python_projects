#to count the number of vowel characters in a string
string=input("Enter a string :")
w=string.count('a')
r=string.count('e')
t=string.count('i')
p=string.count('o')
q=string.count('u')
y=w+r+t+p+q
print(y)
# lt=[]
# for i in range(0,len(string)):
#     vowel=['a','e','i','o','u']
#     if string[i] in vowel:
#         w=(string).count(vowel[i])
#         lt.append(w)
# print(sum(lt))        