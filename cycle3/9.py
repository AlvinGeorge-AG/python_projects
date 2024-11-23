#Print the digit in words
digit=input('Enter a Number :')
for i in digit:
    match int(i):
        case 1:
            print('One ',end='')
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
            print('Seven ',end='') 
        case 8:
            print('Eight ',end='') 
        case 9:
            print('Nine ',end='')
        case 0:
            print('Zero ',end='')                                  