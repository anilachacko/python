ls=[]
nmbr=int(input("Enter the limit:"))
print("Enter",nmbr,"colors:")
for i in range(nmbr):
    a=input()
    ls.append(a)
print(ls)
print( "%s %s"%(ls[0],ls[-1]))
