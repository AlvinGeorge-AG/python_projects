from random import randint
def captcha_generator(n):
    chrs = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    captcha=""
    for i in range(n):
        captcha+=chrs[randint(0,61)]
    return captcha
captcha =captcha_generator(5)
print(captcha)
userinp=input("Enter the captcha seen :")
if  captcha==userinp:
    print("CAPTCHA MATCHED")
else:
    print("CAPTCHA NOT MATCHED")      
