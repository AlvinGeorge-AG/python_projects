#Print the digit in words
digit=input('Enter a Number :')
for i in digit:
    match int(i):
        case 1:
            print('one ',end='')
        case 2:
            print('Two ',end='')
        case 3:
            print('Three ',end='')
        case 4:
            print('Four ',end='')
        case 5:
            print('Five ',end='')
        case 6:
            print('Six ',end='')
        case 7:
            print('seven ',end='') 
        case 8:
            print('eight ',end='') 
        case 9:
            print('nine ',end='')
        case 0:
            print('zero ',end='')                                  