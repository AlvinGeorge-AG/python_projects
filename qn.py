from random import*
vow=[56,17,32,21,37]
v=[56,17,32,21,37]
h=0
while  h<120:
    # for i in range(121):
        shuffle(vow)
        if vow!=v:
            h+=1
            print(h,vow)
        else:
            continue
