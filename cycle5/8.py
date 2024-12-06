#To find the frequency of occurance of a character in a string using dictionary
inp=input("Enter the string :")
dic={}
for i in inp:
    if i in dic:
        dic[i]+=1
    else:      
        dic[i]=1
print(dic)    
