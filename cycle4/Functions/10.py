#Write a recursive function to generate n'th Fibonacci number.Use this function to generate Fibonacci series.
#fibonacci series 0 1 1 2 3 5 8 13....
def fibo(n):
    if n==1:
        return 0
    if n==2:
        return 1
    if n==3:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)
print(fibo(4))