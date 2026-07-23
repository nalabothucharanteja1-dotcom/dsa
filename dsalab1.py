"""Marks= int(input("enter your marks:"))
Grade="F"
if Marks>=90:
    print("your grade is A")
    Grade="A"
elif Marks>=80 and Marks<90:
    print("your Grade is B")
    Grade="B"
elif Marks>=70 and Marks <80:
    print("your Grade is C")
    Grade= "C"
elif Marks>=60 and Marks<70:
    print("your grade is D")
    Grade= "D"
elif Marks<60:
    print("your grade is F. better luck next time")
    Grade="F"
"""
"""
num=int(input("enter your number:"))
duplicate=num
reverse=0
tem=len(str(num))
for i in range (tem):
    r=num%10
    reverse=reverse*10+r
    num=num//10
print(reverse)
if duplicate==reverse:
    print("number is palindrome")
else:
    print("not a palindrome")
"""
"""
num=int(input("enter a number"))
while num>0:
    print(num)
    num=num-1
"""
"""
age=int(input("enter you age:"))
if age>=18:
    print("eligible for vote")
else:
    t=18-age
    print(f"not eligible to vote. wait for {t} years")
"""
"""
counter=0
while counter<2:
    print("inside loop")
    counter=counter+1
else:
    print("this is else")
"""
"""
num=int(input("enter your number:"))
tem=len(str(num))
duplicate=num
reverse=0
for i in range (tem+1):
    r=num%10
    reverse=reverse+r**tem
    num=num//10
print(reverse)
if reverse==duplicate:
    print("nuber is armstrong number")
else:
    print("not a armstrong")
"""

