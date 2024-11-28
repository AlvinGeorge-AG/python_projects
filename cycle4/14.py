# write a recrusive function reverse a string
stri=input("Enter the string :")
def strr(stri):
    news=""
    count=len(stri)
    while count>0:
        news=news+stri[count-1]
        count-=1
    return news
print(strr(stri))
