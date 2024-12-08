what=int(input("The occurance of which value you need :"))
def occ_list(lt):
    if len(lt)==1:
        if lt[0]==what:
            return lt[0] +': 1'
    else:
        for i in lt:
            if i==what:
                n+=0
                print(i,n)
            return occ_list(lt.pop())   
N=[1,2,3,4,5]         
print(occ_list(N))            

