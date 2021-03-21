a=input("Enter 1st string:")
b=input("Enter 2nd string:")
x=a[0:2]
a=a.replace(a[0:2],b[0:2])
b=b.replace(b[0:2],x)
print(a,b)
