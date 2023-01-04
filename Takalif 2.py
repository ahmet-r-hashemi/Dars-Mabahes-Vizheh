#Jalase 2
num1=int(10)
num2=int(5)
print("{}=={}:{}".format(num1,num2,num1==num2))
print("{}!={}:{}".format(num1,num2,num1!=num2))
print("{}<>{}:{}".format(num1,num2,num1!=num2))
print("{}<{}:{}".format(num1,num2,num1<num2))

Resault=(5&3)
print(Resault)
resault=(5/3)
print(resault)

print(5^3)

x=10<<2
print(x)
y=10>>2
print(y)

print(5 in [8, 3, 5, 20])
print(5 not in [8, 3, 5, 20])

number1=5
number2=6
print(number1 is number2)
print(number1 is not number2)

name=input("Esm Ra Vared Konid: ")
age=input("Sen Ra Vared Konid: ")

A=15
B=16
if(A>B):
    print("A>B")
else:
    print("A<B")

Num1=int(input("adad aval ra vared konid: "))
Num2=int(input("adad dovom ra vared konid: "))
if Num1/Num2==0:
    print("bakhsh pazir")
else:
    print("gheyre ghabel taghsim")

_num1=int(input("adad aval ra vared konid: "))
_num2=int(input("adad dovom ra vared konid: "))
_num3=int(input("adad sevom ra vared konid: "))
if((_num1+_num2>_num3) and (_num1+_num3>_num2) and (_num3+_num2>_num1)):
    print("Mohit: ",(_num1+_num2+_num3))
else:
    print("Mosalas NEMISAZAND")
