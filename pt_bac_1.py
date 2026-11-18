a = float(input("hãy nhập hệ số a: "))
b = float(input("hãy nhập hệ số b: "))
if a==0:
    if b==0:
        print("Phương trình vô số nghiệm")
    else:
        print("Phương trình vô nghiệm")
else:
    x = -b/a
    print("Phương trình có 1 nghiệm duy nhất x=",x)
