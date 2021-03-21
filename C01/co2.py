cu=int(input("Enter current year: "))
fi=int(input("Enter final year: "))
list=[]
for i in range(cu,fi+1):
    if(i%4==0 and i%100!=0) or i%400==0:
            list.append(i)
print(list)
