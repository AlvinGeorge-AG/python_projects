#to print the following  series using loop
# 1,3,5,7,9,
#50, 45,40,35,30,25,20,15,10,5,0
n=int(input("Enter a final number n :"))
for i in range(1,n+1,2):
    print(i,end=',')
print()    
for j in range(50,-1,-5):
    print(j,end=',')

# print()
# print()