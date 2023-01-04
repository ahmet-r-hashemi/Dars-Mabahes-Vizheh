#پروژه درس مباحث ویژه برنامه ای که محیط و مساحت و حجم اشکال هندسی را پیدا کند یا ساختار سوییچ کیس
import math
num=int(input("یک عدد از 1 تا 9 وارد کنید: "))
match num:
    case 1:
        print("دایره: ")
        r = float(input("شعاع را وارد کنید: "))
        print("مساحت: ",(r*r)*math.pi)
        print("محیط: ",(r*2)*math.pi)
    case 2:
        print("مربع: ")
        s = float(input("ضلع را وارد کنید: "))
        print("مساحت: ",s*s)
        print("محیط: ",s*4)
    case 3:
        print("Mosalas: ")
        b1 = float(input("ضلع اول: "))
        b2 = float(input("ضلع دوم: "))
        b3 = float(input("ضلع سوم: "))
        if b1>b2 and b1>b3:
            b=b1
        elif b2>b1 and b2>b3:
            b=b2
        elif b3>b1 and b3>b2:
            b=b3
        else:
            b=b2
        h = float(input("ارتفاع راوارد کنید: "))
        print("مساحت: ",(b*h)/2)
        print("محیط: ",b1+b2+b3)
    case 4:
        print("Zoozanaghe: ")
        sb = float(input("قاعده کوچ را وارد کنید: "))
        bb = float(input("قاعده بزرگ را وارد کنید:    "))
        ss = float(input("ساق کوچک را وارد کنید:    "))
        bs = float(input("ساق بزرگ را وارد کنید:    "))
        h = float(input("ارتفاع راوارد کنید:         "))
        print("مساحت: ",((sb+bb)/2)*h)
        print("محیط: ",(sb+bb)+(ss+bs))

    case 5:
        print("چندضلعی منتظم: ")
        ns = float(input("تعداد اضلاع: "))
        ls = float(input("طول یکی از اضلاع: "))
        a = float(input("کوچکترین فاصله تا مرکز چندضلعی را وارد کنید: "))
        print("مساحت: ",((ns*ls*a)/2))
        print("محیط: ",ns*ls)
    case 6:
        print("مربع: ")
        l = float(input("طول را وارد کنید: "))
        w = float(input("عرض را وارد کنید: "))
        print("مساحت: ",l+w)
        print("محیط: ",(l+w)*2)
    case 7:
        print("کره: ")
        r = float(input("شعاع را وارد کنید: "))
        print("حجم: ",((4/3)*math.pi)*(r**3))
    case 8:
        print("مخروط: ")
        r = float(input("شعاع را وارد کنید: "))
        h = float(input("ارتفاع راوارد کنید: "))
        print("حجم: ",((math.pi*(r**2))*(h/3)))
    case 9:
        print("بیضی: ")
        _max = float(input("شعاع بزرگ را وارد کنید: "))
        _min = float(input("شعاع کوچک را وارد کنید: "))
        print("مساحت: ",(_max * _min)*math.pi)
        print("محیط: ",((2*math.pi)*((_max**2)+(_min**2)/2)**0.5))
