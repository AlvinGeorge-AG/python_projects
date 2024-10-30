#decimal to binary and binary to decimal convertion
num=int(input("Enter a Decimal number :"))
numt=num
y=""
while True:
    if num/2==0:
        break
    else:
        y=y+str(num%2)
        num=num//2
print('The binary form of',numt,'is :',y[::-1])
