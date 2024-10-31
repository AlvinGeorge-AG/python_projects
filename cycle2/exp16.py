#decimal to binary and binary to decimal convertion
print(" 1 . Convert decimal value to binary \n 2 . Convert binary value to decimal")
cho=int(input('Enter the choice (1/2):'))
if cho==1:
    num=int(input("Enter a Decimal number :"))
    numt=num
    y=""
    while True:
        if num/2==0:
            break
        else:
            y=y+str(num%2)
            num=num//2
    print('The binary form of ',numt,'is :',y[::-1])
elif cho==2:
    num=int((input("Enter the binary form :")))
    decimalNu=0
    position=0
    while num!=0:
        bit=num%10
        decimalNu+=bit*(2**(position))
        num=num//10
        position+=1
print('The corresponding decimal number is :',decimalNu)







