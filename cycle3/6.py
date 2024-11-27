#Pascals Triangle
N=int(input("Enter n :"))
for i in range(N+1):
    num=1
    print(' '*(N-i),end='')
    for j in range(i+1):
        print(num,end=' ')
        num=num*(i-j)//(j+1)
    print()    