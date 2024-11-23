#to find he sum of digits of a number
numb=input("enter a number :")
i=0
sum_no=0
while i<len(numb):
    sum_no+=int(numb[i])
    i+=1
print('Sum :',sum_no)    
