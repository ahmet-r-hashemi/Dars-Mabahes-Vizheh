#Jalase 3
for i in range(101):
    print(i)
for i in range(100, -1 , -1):
    print(i)

txt={'Emel','Zahra','Mahtab'}
for text in txt:
    print(text)

for index,text in enumerate(txt):
    print(index, text)

TXT=input("Enter a String: ")
for i in TXT:
    print(i)

for i in range(5):
    print(i)

num1=int(input("Adad aval ra vared konid: "))
num2=int(input("Adad dovom ra vared konid: "))
if num2>num1:
    temp=num1
    num1=num2
    num2=temp
for i in range(num2,num1):
    print(i)

for i in range(1,5):
    print('*'* i)

for i in range(1,5):
    for j in range(i):
        print('*', end="    ")
    print()

for i in range(1,10):
    for j in range(1,10):
        print(i*j,end= "\t")
    print("\n")

Sum=0
for i in range(0,101,2):
        Sum+=i
print(Sum)

b=1
a=int(input("Enter a Number: "))
a+=1
for i in range(1,a,1):
    b=b*i
print(b)kiju
