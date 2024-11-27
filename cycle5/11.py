#Write a program to read N words and display them in the increasing order of their lengths. The length of each word is also to be displayed.
N=int(input('How many words you want to enter :'))
dic=[]
for i in range(N):
    W=input('Enter the word :')
    dic.append((W,len(W)))
    dic=sorted(dic)
    dictt={i:dic[i] for i in dic }
print(dictt)  
    
