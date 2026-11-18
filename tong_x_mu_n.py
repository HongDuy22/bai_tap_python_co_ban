n = int(input("hãy nhập một số n: "))
while n < 0:
    n = int(input("hãy nhập lại số n bằng số dương: "))
x = int(input("hãy nhập một số x: "))
while x < 0:
    x = int(input("hãy nhập lại x bằng số dương: "))
tong = 0
for i in range(1,n+1): # vd:n=3 thì chạy từ 1,2,3 (chạy 3 lần)
    tong = tong + x ** (2*i)
    print(tong)
print(f"S(x,n) là {tong}")
    
    
    
