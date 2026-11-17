n =int(input("hãy nhập một số nguyên: "))
tich=1
while n ==0:
    n = int(input("hãy nhập lại và là số nguyên: "))
for i in range(1,n+1):
    tich=tich * i
print(f"{n}!={tich}")