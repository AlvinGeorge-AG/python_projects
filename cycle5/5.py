#Implement the set operation on two sets ( Union, intersection, difference and symmetric difference)
A={1,2,3,4,5,6,7}
B={5,6,7,8,9}
print(A.union(B))# elements are added
print(A.difference(B))#common elements removed
print(A.intersection(B))#common elements are maintained
print(A.symmetric_difference(B))# elements which are not common are printed