#simple desktop calculator
a=float(input("Enter first no:"))
b=float(input("enter second no:"))
print('specify the operator:')
print("""
1=Addition
2=substraction
3=multiplication
4=division
5=Reminder
""")
oper=int(input("Enter operator:"))
#operations
match oper:
    case 1:
        s=a+b
        print("Addition :",s)
    case 2:
        subs=a-b
        print("substraction :",subs)
    case 3:
        mult=a*b
        print("multiplication :",mult)
    case 4:
        if b!=0:
            divi=a/b
            print("division :",divi)
        else:
            print("Division by zero not defined")    
    case 5:
        if b!=0:
            modu=a%b
            print("Reminder :",modu)
        else:
            print("Division by zero not defined")
    case _:
        print("Error")
            
            