#Write a program to read N words and display them in the increasing order of their lengths. The length of each word is also to be displayed.
N=int(input('How many words you want to enter :'))
d={}
for i in range(N):
    W=input('Enter the word :')
    d[W]=len(W)
    sorted_dic= sorted([(key,value) for (value ,key) in d.items()])
print(sorted_dic)  
    
