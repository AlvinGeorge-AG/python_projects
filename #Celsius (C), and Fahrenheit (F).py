#Celsius (C), and Fahrenheit (F)
print("Temperature converter")
while True:
    print("""
            1=celsius to fahrenheit
            2=fahrenheit to celsius
            3=Exit""")
    ask=int(input("Enter the choice :"))
    if ask==1:
        cel=float(input("Enter the temperature in degree celsius :"))
        #C = (°F - 32) × 5/9] 
        #so °F=cel(9/5)+32
        fah=(cel*(9/5)+32)
        print("Temperature in fahrenheit is ",fah)
    elif ask==2:
        #C = (°F - 32) × 5/9] 
            far=float(input("Enter the temperature in degree fahrenheit :"))
            cel=((far-32)*(5/9))
            print("Temperature in celsius is ",cel)
    elif ask==3:
         break        
    else:
         print("Please enter valid choice")        


































"""check=input("Do you want to convert celsius to fahrenheit ,[y/n]")
while check=='y'or check=='n':
    if check=='y':
        cel=float(input("Enter the temperature in degree celsius :"))
        #C = (°F - 32) × 5/9] 
        #so °F=cel(9/5)+32
        fah=(cel*(9/5)+32)
        print("Temperature in fahrenheit is ",fah)
    else:
        check=input("Do you want to convert fahrenheit to celsius ,[y/n]")
        if check=='y':
            #C = (°F - 32) × 5/9] 
            far=float(input("Enter the temperature in degree fahrenheit :"))
            cel=((far-32)*(5/9))
            print("Temperature in celsius is ",cel)
    continue
while check!='y' or check!='n':
     print("Please enter yes[y] or no[n] !!")               
     break"""





