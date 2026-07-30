p=int(input("enter the principle growth:"))
n=int(input("enter the no.of years:"))
def power(p,n):
    if n==0:
        return 1
    else:
        return p*power(p,n-1)
power(p,n)
pow(p,n)
print(f"power of p,n is {power(p,n)}")
print(pow(p,n))
