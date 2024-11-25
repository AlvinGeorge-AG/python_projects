#Read names of 'n' students into a list and sort them in alphabetical order
N=int(input("Enter the number of students :"))
lt=[]
for i in range(N):
    ask=input("Enter the name of student :")
    lt.append(ask)
    lt.sort()
print(lt)