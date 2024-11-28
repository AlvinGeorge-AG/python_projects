N=int(input("Enter the number of lines :"))
if N<=26:
    for i in range(N):
        c=0
        f=ord('A')
        while c<=i:      
            g=chr(f)
            print(g,end=' ')
            c=c+1
            f=f+1
        print()
else:
    print('! ERROR !\n N should be less than or equal to 26')            