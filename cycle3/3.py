N=int(input("Enter the number of lines :"))
for i in range(N):
    c=0
    for j in range(1,N+1,2):
        a=j
        print(a*'*',end=' ')
    print()    