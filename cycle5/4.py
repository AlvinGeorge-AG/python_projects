n1=int(input('Enter the number of elements in the first list :'))
l1=[]
l2=[]
even=[]
odd=[]
for i in range(n1):
    ask=int(input("Enter the number :"))
    l1.append(ask)
n2=int(input('Enter the number of elements in the second list :'))    
for i in range(n2):
    ask=int(input("Enter the number :"))
    l2.append(ask)
#even    
for i in range(len(l1)):
    if l1[i]%2==0:
        even.append(l1[i])
for i in range(len(l2)):
    if l2[i]%2==0:
        even.append(l2[i])
even=sorted(even)
#odd
for i in range(len(l1)):
    if l1[i]%2!=0:
        odd.append(l1[i])
for i in range(len(l2)):
    if l2[i]%2!=0:
        odd.append(l2[i])
odd=sorted(odd)
print(odd)
print(even)
print(even+odd)
        
    
