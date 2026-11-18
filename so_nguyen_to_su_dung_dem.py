n = int(input("hãy nhập một số: "))
dem=0
for i in range(1,n+1):
    if n%i==0:
        dem=dem+1
if dem==2:
    print("True")
else:
    print("false")
    