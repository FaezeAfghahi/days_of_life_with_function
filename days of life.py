"""
چاپ روزهای سپری شده عمر تا به امروز با احتساب سالهای کبیسه
"""

d = int(input("day of your birth?"))
m = int(input("month of your birth?"))
y = int(input("year of your birth?"))

dd = int(input("this day?"))
mm = int(input("this month?"))
yy = int(input("this year?"))

s =365
l =[]
n=1210
c=1
e=0
st = 0
while n<1500:
    if c<8:
        n=n+4
        l.append(n)
        c=c+1
    else:
        n=n+5
        l.append(n)
        c=1
for i in range(0,len(l)):
    if l[i]==y:
        s = s+1
for j in range(y,yy):
    for i in range(0,len(l)):
        a = l[i]
        if j == a:
            print(j,'kabise year')
            st = st+1
print(st,"day of kabise year")
if mm<=6:
    dd = (mm-1)*31 +dd
if mm > 6:
    dd = (mm-7)*30 +186 +dd
if m<=6:
    d = (m-1)*31 + d
if m > 6:
    d = (m-7)*30 +186 + d
if d>=dd:
    r = d-dd
    print(r,"days that remain to birthday")
if d<dd:
    r = s-dd+d
    print(r,"days that remain to birthday")
yy = yy - y 
dd = (((yy*365)+st)+dd)-d
print(dd,"days of life")
