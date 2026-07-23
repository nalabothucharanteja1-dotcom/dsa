"""def greet():
    print("hello")
greet()"""
"""
def greet(name):
    print("hello", name)
greet("tej")
"""
"""
def square(num):
    result=num*num
    return result
print("square:", square(9))
"""
"""
import math
square_root=math.sqrt(8)
print("square root:", square_root)
power=pow(5,9)
print("5 to power 9", power)
"""
"""
def greet(name,message="hello"):
    print(message, name)
greet("Alice", "good morning")
greet("jonny", "morning")
"""
"""
def add(*numbers):
    return sum(numbers)
print(add(1,2,3,4))
"""
"""
def greet(**words):
    for key,values in words.items():
        print(f"{key}:{values}")
greet(name="john", greeting="hello")
"""
"""
def fact(x):
    if x==1:
        return 1
    else:
        return (x*fact(x-1))
num=int(input("enter number:"))
print(fact(num))
"""
"""
def natural_sum(n):
    if n<=1:
        return n
    else:
        return n+natural_sum(n-1)
num=int(input("enter number to add:"))
print(natural_sum(num))
"""
"""
def fibo(n):
    if n<=1:
        return n
    else:
        return (fibo(n-1)+fibo(n-2))
num=int(input("enter a number:"))
print(fibo(num))
"""
"""
message="hello"
def hi():
    message="hi"
    print (message)
print(hi())
print(message)
"""
