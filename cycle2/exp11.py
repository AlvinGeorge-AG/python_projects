#read n numbers and find the sum of odd and even numbers seperately
n=int(input("How many number do you want to enter :"))
o=[]
for i in range(0,n):
    ask=int(input("Enter the number :"))
    o.append(ask)
# print(o)
i=0
even=[]
odd=[]
while i in range(0,len(o)):
    if (o[i])%2==0:
        even.append(o[i])
    else :
        odd.append(o[i])   
    i=i+1    
# print('odd :',odd)
# print('even :',even)
print('Sum of odd numbers ',sum(odd))
print('Sum of even numbers ',sum(even))
