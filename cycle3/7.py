#to print all prime numbers less than 1000
#using nested for loops
h=set()
g=set()
for i in range(2,1000):
    g.add(i)
    for j in range(2,1000):
        if i%j==0:
            if i!=j:
                h.add(i)
print(sorted(g.difference(h)))