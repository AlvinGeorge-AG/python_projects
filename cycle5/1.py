#Read 'n' numbers into a list and find the min,max,sum and average.
n=int(input("How many number you want to enter :"))
i=0
lt=[]
while i<n:
    ask=float(input(f"Enter the number :"))
    lt.append(ask)
    i=i+1
print(lt)    
print("Max :",max(lt))    
print("Min :",min(lt))    
print("Sum :",sum(lt))
print('Average :',(sum(lt)/len(lt)))