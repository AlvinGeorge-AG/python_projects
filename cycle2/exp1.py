n=int(input("How many number you want to enter :"))
i=0
summ=[]
while i<n:
    ask=float(input("Enter the number :"))
    summ=summ.append(ask)
    i=i+1
print("Max :",max(summ))    
print("Min :",min(summ))    
print("Sum :",sum(summ))
print('Average :',(sum(summ)/len(summ)))