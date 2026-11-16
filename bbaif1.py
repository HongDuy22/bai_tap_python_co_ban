name = input("hãy nhập họ và tên: ")
mssv = input("hãy nhập mssv: ")
diem = float(input("hãy nhập điểm rèn luyện: "))
def diem_hanh_kiem(diem):
    if diem >= 90:
        return "Có hạnh kiểm xuất sắc"
    elif diem >=80 and diem <90:
        return "Có hạnh kiểm tốt"
    elif diem >=65 and diem<80:
        return "Có hạnh kiểm khá"
    elif diem>=50 and diem<65:
        return "Có hạnh kiếm trunh bình"
    else:
        return "Có hạnh kiểm yếu"
print(diem_hanh_kiem(diem))
        