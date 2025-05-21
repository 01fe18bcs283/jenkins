def factors(n):
    l=[]
    for i in range(1,n+1):
        if n%i==0:
            l.append(i)
    return l

n = int(input("enter the number:"))
l2=factors(n)
print(f"factors of {n} is {l2}")