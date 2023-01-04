#Jalase 4
num1=int(input("Adad aval ra vared konid: "))
num2=int(input("Adad dovom ra vared konid: "))
STR=input("az beine D va U entekhab konid: ")
if(num1>num2):
    B1=num1
    B2=num2
else:
    B1=num2
    B2=num1
if(STR=='u' or STR =='U'):
    for i in range(B1,B2+1):
        print(i)
elif(STR=='d' or STR =='D'):
    for i in range(B2,B1+1):
        print(i)
else:
    print("Voroodi eshtebah ast!")

Name=["ABC","DEF","GHI"]
x=Name[0]
print(x)

Y=len(Name)
print(Y)

for i in Name:
    print(i)

Name.append("JKL")
Name.pop(0)
print(Name)

name=[]
for i in range(0,5):
    STR=input("Enter Names: ")
    name.append(STR)
for i in name:
    print(i)
    
temp=0
num=[]
for i in range(0,101):
    STR=input("Enter Numbers: ")
    num.append(int(STR))
for i in num:
    if(i>temp):
           temp=i
print(temp)

c=0
temp=0
num=[]
for i in range(0,101):
    STR=input("100 adad vared konid: ")
    num.append(int(STR))
for i in num:
    if(i>temp):
           temp=i
for i in num:
    if(i==temp):
        c+=1
print("Bozorg tarin : ",temp," tedad tekrar: ",c)

import random
from random import randint
from random import seed
temp=0
Num=[]
for i in range(0,100):
    Num.append(random.randint(0,100))
for i in Num:
    for j in Num:
        if(i>j):
            temp=i
            i=j
            j=temp
print(Num)

def Calc(X,Y):
    Z=X+Y
    print(Z)
A=int(input("Enter First Number: "))
B=int(input("Enter Second Number: "))
Calc(A,B)

def calc(x,y):
    z=x+y
    return z
a=int(input("Enter First Number: "))
b=int(input("Enter Second Number: "))
c=calc(a,b)
print(c)

def BMM(x, y):
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            bmm = i 
    return bmm

num1 = int(input("Enter First Number: ")) 
num2 = int(input("Enter Second Number: ")) 
BM=BMM(num1, num2)
print("BMM=", BMM(num1, num2))
print("KMM=",(num1*num2)/BM)

import math
def distance(x1 , y1 , x2 , y2):
    return math.sqrt(math.pow(x2 - x1, 2) +
                math.pow(y2 - y1, 2) * 1.0)
h=int(input("X1 ra vared konid: "))
i=int(input("X2 ra vared konid: "))
j=int(input("Y1 ra vared konid: "))
k=int(input("Y2 ra vared konid: "))
print("%.6f"%distance(h, i ,j, k))
