scccd = input("hãy nhập số căn cước công dân: ")
kq = True
if len(scccd) != 12:
     kq = False
else:
    for i in scccd:
        if i < "0" or i > "9":
            kq = false
            break
if kq==True:
    print("Hợp lệ")
else:
    print("không hợp lệ")

     