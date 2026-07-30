def fact(n):
    if n==0:
        return 1
    elif n==1:
        return 1
    else:
        return n*fact(n-1)
n=int(input("enter the number of parcels:"))
fact(n)
print(f"the no of ways parcel can be arranged is {fact(n)}")
