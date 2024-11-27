my_list = []
num_tuples = int(input("Enter the number of tuples: "))
# Input each tuple
for i in range(num_tuples):
    element1 = input("Enter the first element of tuple {}: ".format(i+1))
    element2 = len(element1)
    my_list.append((element1, element2))
    my_list=sorted(my_list,key=lambda x:x[1])
print(my_list)
