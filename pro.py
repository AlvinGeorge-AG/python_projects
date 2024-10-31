init_h=float(input("Enter the initial height :"))
bindex=float(input("Enter the bouncing index :"))
no=float(input("enter the number of bouncing :"))
count=0
final_dis=0
while count<no:
    final_dis+=init_h
    new_h=init_h*bindex
    count+=1
    init_h=new_h 
    final_dis+=new_h 

round(final_dis,2)
print("total distance travelled :",final_dis)    
