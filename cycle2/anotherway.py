# # from math import factorial as f
# # from math import pi
# # print('cos(x)=1-(x^2/2!)+(x^4/4!)-(x^6/6!)+...+((-1)**n)*(x^n/n!)')
# # n=int(input('Enter the value of n:'))
# # X=float(input('Enter the value of x :'))
# # y=X*(pi/180)
# # cosine=1
# # s=-1
# # for i in range(2,n+1,2):
# #     T=((s))*((y**i)/(f(i)))
# #     cosine+=T
# #     s=s*(-1)
# # print(cosine)    


# # # to find the factorial of a number using for loop
# # n=int(input("Enter a number :"))
# # y=1
# # for i in range(1,n+1):
    
# #     if n==0:
# #         pass
# #     else:
       
# #         y*=i
# # print(y)        
# # 
# my_list = [('ple', 2), ('banana', 5), ('cherry', 10)]

# # Sort the list by the second element of each tuple
# sorted_list = sorted(my_list, key=lambda x: x[0])

# print(sorted_list)
#Write a function that returns True if a given number is prime and False otherwise.Use this function to print all prime numbers less than N. Read N. Use the same function to print n'th prime number.
n=int(input("Enter a number :"))
lt=[]



for i in range(2,n):
    lt.append(i)


print(lt)
#print(filter(prime,))
