# Program to check whether the given number is a valid mobile number or not using functions.
# Rules:
# 1. Every number should contain exactly 10 digits.
# 2. The first digit should be 7 or 8 or 9
def mobile_number():
    N=input("Enter the mobile number :")
    f=['7','8','9']
    if N[0] in f:
        if len(N)==10:
            R="The Mobile number is Active "
        else:
            R="The Mobile number is Fake !"     
    else:
        R="The Mobile number is Fake !"  
    return R 
print(mobile_number())         