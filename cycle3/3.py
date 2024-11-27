
N=int(input("Enter the number of lines :"))
for i in range(0,N+(N-1),2):
    num='*'
    print(' '*(N-i+(N-2)),end='')
    for j in range(i+1):
        print(num,end=' ')
    print()    