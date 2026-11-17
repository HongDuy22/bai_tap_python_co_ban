m = float(input("hãy nhập chiều cao: "))
kg = float(input("hãy nhập cân nặng: "))
while m < 0:
    m = float(input("hãy nhập lại chiều cao vì chiều cao là số dương: "))
while kg < 0:
    kg = float(input("hãy nhập lại cân nặng vì cân nặng là số dương: "))
def bmi(m,kg):
    tich = kg/m**2
    return tich
print(f"Tỉ số cân nặng và chiều cao là {bmi(m,kg):.2f}")