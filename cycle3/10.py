#Find the largest digit in a number( use while and if )
num=input('Enter a Number :')
count=0
larg=0
while count<len(num):
    if int(num[count])>larg:
        larg=int(num[count])
    count+=1
print(larg)        