num = 0

while True:
    num = int(input("Enter a number: "))

    if num > 4000 or num <= 0:
        print("Enter a number between 0 and 4000!")
    else:
        break

o_num = num
n_th = 0
n_h = 0
n_t = 0
n = 0
r_num = ""

if num >= 1000:
    n_th = int(num / 1000)
    num = num % 1000
if num >= 100:
    n_h = int(num / 100)
    num = num % 100
if num >= 10:
    n_t = int(num / 10)
    num = num % 10
if num >= 1:
    n = round(num)

#1000 - 4000
if n_th >= 1 and n_th < 4:
    r_num += ("M"*n_th)
#100 - 900
if n_h >= 1 and n_h < 4:
    r_num += ("C"*n_h)
elif n_h == 4:
    r_num += "CD"
elif n_h == 5:
    r_num += "D"
elif n_h > 5 and n_h < 8:
    r_num += "D" + ("C"*(n_h-5))
elif n_h == 8:
    r_num += "DCCC"
elif n_h == 9:
    r_num += "CM"
#10 - 90
if n_t >= 1 and n_t < 4:
    r_num += ("X"*n_t)
elif n_t == 4:
    r_num += "XL"
elif n_t == 5:
    r_num += "L"
elif n_t > 5 and n_t < 8:
    r_num += "L" + ("X"*(n_t-5))
elif n_t == 8:
    r_num += "LXXX"
elif n_t == 9:
    r_num += "XC"
#1 - 9
if n >= 1 and n < 4:
    r_num += ("I"*n)
elif n == 4:
    r_num += "IV"
elif n == 5:
    r_num += "V"
elif n > 5 and n < 8:
    r_num += "V" + ("I"*(n-5))
elif n == 8:
    r_num += "VIII"
elif n == 9:
    r_num += "IX"
     
print(str(o_num) + " = " + r_num)