#condition solving

#1/largest among three numbers

a=int(input())
b=int(input())
c=int(input())

if a>=b and a>=c:
    print("a larger number")
elif b>=a and b>=c:
    print("b lerger number")
else:
    print("lerger number c")

#2/ Quader identfier

x=int(input())
y=int(input())
if x>0 and y>0:
    print("1st quadrant")
elif x<0 and y>0:
    print("2nd quadarnt")
elif x<0 and y<0:
    print("3rd quadarnt")
elif x>0 and y<0:
    print("4th quadarnt")

#3/Age classifier

age=int(input("choices your age: "))
if age>=0 and age<=1:
    print("infant")
elif age>=2 and age<=3:
    print("toddler")
elif age>=4 and age<=12:
    print("child")
elif age>=13 and age<=19:
    print("teenager")
elif age>=20:
    print("adult")

#4 BMI Calculator bmi=wight/(hight**2)

wight=int(input())
hight=int(input())
bmi=wight/(hight**2)
if bmi<=18.5:
    print("underwight")
elif bmi<=25:
    print("normal")
elif bmi>=30:
    print("overhight")

#5/Temperature convertr

c=int(input())
if c>0:
    f=(c*9/5)+32
    print(f)
elif c<0:
    k=c+273
    print(k)
else:
    print("temparetur 0c")

#6/ simpe calculator

a=int(input())
b=int(input())
op=input()
if op=="+":
    print(a+b)
elif op=="-":
    print(a-b)
elif op=="*":
    print(a*b)
elif op=="/":
    if b!=0:
       print(a/b)