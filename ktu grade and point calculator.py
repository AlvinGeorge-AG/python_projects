#A simple program to calculate ktu grade and points
mark=int(input("Enter the marks out of 100 :"))
percentage =((mark)/100)*100
# print(percentage)
if percentage>=90:
    print("KTU GRADE POINT : 10")
    print("KTU GRADE : S")
elif 85<=percentage<90:
    print("KTU GRADE POINT :9")
    print("KTU GRADE  : A+")
elif 80<=percentage<85:
    print("KTU GRADE POINT :8.5")
    print("KTU GRADE  : A")
elif 75<=percentage<80:
    print("KTU GRADE POINT :8")
    print("KTU GRADE  : B+")
elif 70<=percentage<75:
    print("KTU GRADE POINT :7.5")
    print("KTU GRADE  : B")
elif 65<=percentage<70:
    print("KTU GRADE POINT :7")
    print("KTU GRADE  : C+")
elif 60<=percentage<65:
    print("KTU GRADE POINT :6.5")
    print("KTU GRADE  : C")
elif 55<=percentage<60:
    print("KTU GRADE POINT :6")
    print("KTU GRADE  : D")
elif 50<=percentage<55:
    print("KTU GRADE POINT :5.5")
    print("KTU GRADE  : P(PASS)")
# elif 85<=percentage<=90:
#     print("KTU GRADE POINT :9")
#     print("KTU GRADE  : A+")

