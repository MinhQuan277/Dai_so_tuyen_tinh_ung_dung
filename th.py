# lưu ý về các phép toán xử lý trên list
danhsach1 = [1., 3.]
danhsach2 = [5., 7.]
danhsach = danhsach1 + danhsach2
print("kết quả là :",danhsach)
# kết quả : [1.0, 3.0, 5.0, 7.0]
danhsach_gapdoi = 2* danhsach
print("kết quả là :",danhsach_gapdoi)
# kết quả : [1.0, 3.0, 5.0, 7.0, 1.0, 3.0, 5.0, 7.0]
danhsach_nhan = danhsach*2
print("kết quả là :", danhsach_nhan)
# Kết quả là : [1.0, 3.0, 5.0, 7.0, 1.0, 3.0, 5.0, 7.0]
danhsach_chia = danhsach / 2
print("kết quả là :",danhsach_chia)
# kết quả là lỗi do list kh thực hiện được phép chia

# Ghép các danh sách bằng lệnh zip:
mon_hoc = ["ToanCC", "DSTT", "ToanRR", "LaptrinhCB"] 
thu_tu = [2, 3, 4, 1] 
diem_so = [10, 9, 8, 7] 
anh_xa = list(zip(thu_tu, mon_hoc, diem_so)) 
print(anh_xa)
# kết quả là : [(2, 'ToanCC', 10), (3, 'DSTT', 9), (4, 'ToanRR', 8), (1, 'LaptrinhCB', 7)]
tap_hop = set(anh_xa)
print(tap_hop)
# kết quả là : [(2, 'ToanCC', 10), (3, 'DSTT', 9), (4, 'ToanRR', 8), (1, 'LaptrinhCB', 7)]
lay_TT, lay_monhoc , lay_diem = zip(*anh_xa)
print(lay_monhoc)
# kết quả là : ('ToanCC', 'DSTT', 'ToanRR', 'LaptrinhCB')

# Lệnh thực thi một tập tin python
mylist = [100, 200, 300]
a, b, c = mylist
print (a, b, c)
execfile('d:/thucthi1.py') 
# kết quả laf : 100, 200, 300

# Định nghĩa Symbol và các phép toán hình thức (symbolic)
from sympy import Symbol 
x = Symbol('x') 
f = x + x + x + 2 
print(f)
#kết quả là : 3*x + 2
a = Symbol('Noi')
b = Symbol('Chim')
3*b + 7*a
# kết quà là : 3*Chim + 7*Noi
print(a.name)
# kết quà là : 'Noi'
print(b.name)
# kết quà là : 'Chim'

from sympy import Symbol
x = Symbol('x')
y = Symbol('y')
s = x*y + y*x
print(s)
# kết quả là : 2*x*y
p = x*(x + 2*x)
print(p)
#kết quả là : 3*x**2

# Đặt nhân tử chung và khai triển biểu thức 
from sympy import factor
bieuthuc = x**3 - y**3
factor(bieuthuc)
# kết quả là : (x - y)*(x**2 + x*y + y**2)




