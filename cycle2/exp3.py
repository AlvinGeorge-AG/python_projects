# to find the numbers between 10 and 1000 that are divisible by 13 but not by 3
listt=[]
for i in range(10,1000):
    if i%13==0 and i%3!=0:
        listt.append(i)
print("The numbers are :",listt)        
       