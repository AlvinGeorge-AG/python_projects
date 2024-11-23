#Write a program  that lets the user enter the initial height of the ball, bounciness index and the number 
# of times the ball is allowed to continue bouncing. Output should be the totaldistance traveled by the ball.
init_h=float(input("Enter the initial height :"))
index=float(input("Enter the bounciness index :"))
times=int(input('Enter number of times the ball bounces :'))
count=0
totalh=init_h
newh=0
while count<times:
    totalh+=newh
    newh=init_h*index
    init_h=newh
    totalh+=newh
    count+=1
print('Total height the ball travelled :',round(totalh,2))

