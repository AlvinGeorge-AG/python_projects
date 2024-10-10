#simple desktop calculator
a=float(input("Enter first no:"))
b=float(input("enter second no:"))
print('specify the operator:')
print("""
1=Addition
2=substraction
3=multiplication
4=division
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
        divi=a/b
        print("division :",divi)
        